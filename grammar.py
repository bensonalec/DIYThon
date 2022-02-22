from __future__ import annotations

from abc import abstractmethod
from tokenize import String
from typing import (
    AbstractSet,
    Any,
    Dict,
    Iterable,
    Iterator,
    List,
    Optional,
    Set,
    Tuple,
    TYPE_CHECKING,
    Union,
)

keywords = [
    "'and'",
    "'as'",
    "'assert'",
    "'break'",
    "'class'",
    "'continue'",
    "'def'",
    "'del'",
    "'elif'",
    "'else'",
    "'except'",
    "'False'",
    "'finally'",
    "'for'",
    "'from'",
    "'global'",
    "'if'",
    "'import'",
    "'in'",
    "'lambda'",
    "'None'",
    "'nonlocal'",
    "'not'",
    "'or'",
    "'pass'",
    "'raise'",
    "'return'",
    "'True'",
    "'try'",
    "'while'",
    "'with'",
    "'yield'",
]

class GrammarError(Exception):
    pass


class GrammarVisitor:
    def visit(self, node: Any, *args: Any, **kwargs: Any) -> Any:
        """Visit a node."""
        method = "visit_" + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node, *args, **kwargs)

    def generic_visit(self, node: Iterable[Any], *args: Any, **kwargs: Any) -> None:
        """Called if no explicit visitor function exists for a node."""
        for value in node:
            if isinstance(value, list):
                for item in value:
                    self.visit(item, *args, **kwargs)
            else:
                self.visit(value, *args, **kwargs)


class Grammar:
    def __init__(self, rules: Iterable[Rule], metas: Iterable[Tuple[str, Optional[str]]]):
        self.rules = {rule.name: rule for rule in rules}
        self.metas = dict(metas)

    def __str__(self) -> str:
        return "\n".join(str(rule) for name, rule in self.rules.items())

    def __repr__(self) -> str:
        lines = ["Grammar("]
        lines.append("  [")
        for rule in self.rules.values():
            lines.append(f"    {repr(rule)},")
        lines.append("  ],")
        lines.append("  {repr(list(self.metas.items()))}")
        lines.append(")")
        return "\n".join(lines)

    def __iter__(self) -> Iterator[Rule]:
        yield from self.rules.values()


# Global flag whether we want actions in __str__() -- default off.
SIMPLE_STR = True


class Rule:
    def __init__(self, name: str, type: Optional[str], rhs: Rhs, memo: Optional[object] = None):
        self.name = name
        self.type = type
        self.rhs = rhs
        self.memo = bool(memo)
        self.visited = False
        self.nullable = False
        self.left_recursive = False
        self.leader = False
        rhs.set_rule_name(name)

    def is_loop(self) -> bool:
        return self.name.startswith("_loop")

    def is_gather(self) -> bool:
        return self.name.startswith("_gather")

    def __str__(self) -> str:
        if SIMPLE_STR or self.type is None:
            res = f"{self.name}: {self.rhs}"
        else:
            res = f"{self.name}[{self.type}]: {self.rhs}"
        if len(res) < 88:
            return res
        lines = [res.split(":")[0] + ":"]
        lines += [f"    | {alt}" for alt in self.rhs.alts]
        return "\n".join(lines)

    def __repr__(self) -> str:
        return f"Rule({self.name!r}, {self.type!r}, {self.rhs!r})"

    def __iter__(self) -> Iterator[Rhs]:
        yield self.rhs

    def nullable_visit(self, rules: Dict[str, Rule]) -> bool:
        if self.visited:
            # A left-recursive rule is considered non-nullable.
            return False
        self.visited = True
        self.nullable = self.rhs.nullable_visit(rules)
        return self.nullable

    def initial_names(self) -> AbstractSet[str]:
        return self.rhs.initial_names()

    def flatten(self) -> Rhs:
        # If it's a single parenthesized group, flatten it.
        rhs = self.rhs
        if (
            not self.is_loop()
            and len(rhs.alts) == 1
            and len(rhs.alts[0].items) == 1
            and isinstance(rhs.alts[0].items[0].item, Group)
        ):
            rhs = rhs.alts[0].items[0].item.rhs
        return rhs

    def collect_todo(self, gen) -> None:
        rhs = self.flatten()
        rhs.collect_todo(gen)


class Leaf:
    def __init__(self, value: str):
        self.value = value

    def __str__(self) -> str:
        return self.value

    def __iter__(self) -> Iterable[str]:
        if False:
            yield

    @abstractmethod
    def nullable_visit(self, rules: Dict[str, Rule]) -> bool:
        raise NotImplementedError

    @abstractmethod
    def initial_names(self) -> AbstractSet[str]:
        raise NotImplementedError


class NameLeaf(Leaf):
    """The value is the name."""

    def __str__(self) -> str:
        if self.value == "ENDMARKER":
            return "$"
        return super().__str__()

    def __repr__(self) -> str:
        return f"NameLeaf({self.value!r})"

    def nullable_visit(self, rules: Dict[str, Rule]) -> bool:
        if self.value in rules:
            return rules[self.value].nullable_visit(rules)
        # Token or unknown; never empty.
        return False

    def initial_names(self) -> AbstractSet[str]:
        return {self.value}
    def to_rule(self, varnum):
        if str(self.value).isupper():
            return f"(n{varnum} := self.{'expect' if self.value not in keywords else 'expect_keyword'}('{self.value}'))"
        else:
            return f"(n{varnum} := self.{self.value}())"


class StringLeaf(Leaf):
    """The value is a string literal, including quotes."""

    def __repr__(self) -> str:
        return f"StringLeaf({self.value!r})"

    def nullable_visit(self, rules: Dict[str, Rule]) -> bool:
        # The string token '' is considered empty.
        return not self.value

    def initial_names(self) -> AbstractSet[str]:
        return set()

    def to_rule(self, varnum):
        return f"self.{'expect_keyword' if self.value in keywords else 'expect'}({self.value})"


#TODO: Figure out how this should really be working
class Rhs:
    def __init__(self, alts: List[Alt]):
        self.alts = alts
        self.memo: Optional[Tuple[Optional[str], str]] = None

    def __str__(self) -> str:
        return " | ".join(str(alt) for alt in self.alts)

    def __repr__(self) -> str:
        return f"Rhs({self.alts!r})"

    def __iter__(self) -> Iterator[List[Alt]]:
        yield self.alts

    def set_rule_name(self, name: str) -> None:
        for i, alt in enumerate(self.alts):
            alt.set_rule_name_and_index(name, i)

    def nullable_visit(self, rules: Dict[str, Rule]) -> bool:
        for alt in self.alts:
            if alt.nullable_visit(rules):
                return True
        return False

    def initial_names(self) -> AbstractSet[str]:
        names: Set[str] = set()
        for alt in self.alts:
            names |= alt.initial_names()
        return names

    def collect_todo(self, gen) -> None:
        for alt in self.alts:
            alt.collect_todo(gen)

    def to_rule(self, varnum, fromGroup=True, synthNumber=None):
        if fromGroup:
            #NOTE: For some reason the -1 here is important?
            return f"(n{varnum} := self.synthetic_rule_{synthNumber}())"
        currentMethod = ""
        for alt in self.alts:
            currentMethod += '\t\tpos = self.mark()\n'
            currentMethod += f'\t\tif (True and\n'
            variables = []
            for item in alt.items:
                ruleString = item.to_rule(varnum)
                currentMethod += f"\t\t {ruleString} is not None and\n"
                if f"n{varnum} " in ruleString:
                    variables.append(f"n{varnum}")
                varnum += 1

            currentMethod += '\t\t   True):\n'
            currentMethod += f'\t\t\treturn {alt.rule_name}{alt.alt_index if not alt.rule_name.startswith("synthetic_rule_") else ""}({", ".join([x for x in variables])})\n'
            currentMethod += '\t\tself.reset(pos)\n'

        return currentMethod

class Alt:
    def __init__(self, items: List[NamedItem], *, icut: int = -1, action: Optional[str] = None):
        self.items = items
        self.icut = icut
        self.action = action

    def __str__(self) -> str:
        core = " ".join(str(item) for item in self.items)
        if not SIMPLE_STR and self.action:
            return f"{core} {{ {self.action} }}"
        else:
            return core

    def __repr__(self) -> str:
        args = [repr(self.items)]
        if self.icut >= 0:
            args.append(f"icut={self.icut}")
        if self.action:
            args.append(f"action={self.action!r}")
        return f"Alt({', '.join(args)})"

    def __iter__(self) -> Iterator[List[NamedItem]]:
        yield self.items

    def set_rule_name_and_index(self, name: str, index: int) -> None:
        self.rule_name = name
        self.alt_index = index

    def nullable_visit(self, rules: Dict[str, Rule]) -> bool:
        for item in self.items:
            if not item.nullable_visit(rules):
                return False
        return True

    def initial_names(self) -> AbstractSet[str]:
        names: Set[str] = set()
        for item in self.items:
            names |= item.initial_names()
            if not item.nullable:
                break
        return names

    def collect_todo(self, gen) -> None:
        for item in self.items:
            item.collect_todo(gen)


class NamedItem:
    def __init__(self, name: Optional[str], item: Item, type: Optional[str] = None):
        self.name = name
        self.item = item
        self.type = type
        self.nullable = False

    def __str__(self) -> str:
        if not SIMPLE_STR and self.name:
            return f"{self.name}={self.item}"
        else:
            return str(self.item)

    def __repr__(self) -> str:
        return f"NamedItem({self.name!r}, {self.item!r})"

    def __iter__(self) -> Iterator[Item]:
        yield self.item

    def nullable_visit(self, rules: Dict[str, Rule]) -> bool:
        self.nullable = self.item.nullable_visit(rules)
        return self.nullable

    def initial_names(self) -> AbstractSet[str]:
        return self.item.initial_names()
    
    def to_rule(self, varnum):
        return self.item.to_rule(varnum)

#TODO: Get Lookahead in a state it can actually be used in the parser, for now we'll not worry
class Lookahead:
    def __init__(self, node: Plain, sign: str):
        self.node = node
        self.sign = sign

    def __str__(self) -> str:
        return f"{self.sign}{self.node}"

    def __iter__(self) -> Iterator[Plain]:
        yield self.node

    def nullable_visit(self, rules: Dict[str, Rule]) -> bool:
        return True

    def initial_names(self) -> AbstractSet[str]:
        return set()
        

class PositiveLookahead(Lookahead):
    def __init__(self, node: Plain):
        super().__init__(node, "&")

    def __repr__(self) -> str:
        return f"PositiveLookahead({self.node!r})"

    def to_rule(self, varnum):
        try:
            func = f"self.{'expect' if self.node.value not in keywords else 'expect_keyword'}"
        except AttributeError:
            func = "self.expect"
        if str(self.node).isupper():
            atom = f"'{str(self.node)}'"
        else:
            atom = str(self.node)
        if type(self.node) != StringLeaf and str(self.node).islower():
            func = f"self.{self.node}"
            atom = ""
        if type(self.node) == Group:
            func = f"self.synthetic_rule_{self.node.synthNum}"
            atom = ""
        if type(self.node) == NameLeaf and self.node.value.islower():
            func = f"self.{self.node.value}"
            atom = ""
        return f"self.positive_lookahead({func}, {atom})"


class NegativeLookahead(Lookahead):
    def __init__(self, node: Plain):
        super().__init__(node, "!")

    def __repr__(self) -> str:
        return f"NegativeLookahead({self.node!r})"

    def to_rule(self, varnum):
        try:
            func = f"self.{'expect' if self.node.value not in keywords else 'expect_keyword'}"
        except AttributeError:
            func = "self.expect"
        if str(self.node).isupper():
            atom = f"'{str(self.node)}'"
        else:
            atom = str(self.node)
        if type(self.node) != StringLeaf and str(self.node).islower():
            func = f"self.{self.node}"
            atom = ""
        if type(self.node) == Group:
            func = f"self.synthetic_rule_{self.node.synthNum}"
            atom = ""
        if type(self.node) == NameLeaf and self.node.value.islower():
            func = f"self.{self.node.value}"
            atom = ""
        return f"self.negative_lookahead({func}, {atom})"


class Opt:
    def __init__(self, node: Item, synthNumber: int = None):
        self.node = node
        self.synthNumber = synthNumber

    def __str__(self) -> str:
        s = str(self.node)
        # TODO: Decide whether to use [X] or X? based on type of X
        if " " in s:
            return f"[{s}]"
        else:
            return f"{s}?"

    def __repr__(self) -> str:
        return f"Opt({self.node!r})"

    def __iter__(self) -> Iterator[Item]:
        yield self.node

    def nullable_visit(self, rules: Dict[str, Rule]) -> bool:
        return True

    def initial_names(self) -> AbstractSet[str]:
        return self.node.initial_names()

    def to_rule(self, varnum):
        if type(self.node) == Rhs:
            return f"({self.node.to_rule(varnum, True, self.synthNumber)} or True)"
        return f"({self.node.to_rule(varnum)} or True)"

class Repeat:
    """Shared base class for x* and x+."""

    def __init__(self, node: Plain):
        self.node = node
        self.memo: Optional[Tuple[Optional[str], str]] = None

    @abstractmethod
    def nullable_visit(self, rules: Dict[str, Rule]) -> bool:
        raise NotImplementedError

    def __iter__(self) -> Iterator[Plain]:
        yield self.node

    def initial_names(self) -> AbstractSet[str]:
        return self.node.initial_names()

class Repeat0(Repeat):
    def __str__(self) -> str:
        s = str(self.node)
        # TODO: Decide whether to use (X)* or X* based on type of X
        if " " in s:
            return f"({s})*"
        else:
            return f"{s}*"

    def __repr__(self) -> str:
        return f"Repeat0({self.node!r})"

    def nullable_visit(self, rules: Dict[str, Rule]) -> bool:
        return True

    def to_rule(self, varnum):
        try:
            func = f"self.{'expect' if self.node.value not in keywords else 'expect_keyword'}"
        except AttributeError:
            func = "self.expect"
        atom = f"'{str(self.node)}'"
        if type(self.node) != StringLeaf and str(self.node).islower():
            func = f"self.{self.node}"
            atom = ""
        if type(self.node) == Group:
            func = f"self.synthetic_rule_{self.node.synthNum}"
            atom = ""
        if type(self.node) == NameLeaf and self.node.value.islower():
            func = f"self.{self.node.value}"
            atom = ""
        return f"(n{varnum} := self.loop(False, {func}, {atom}))"

class Repeat1(Repeat):
    def __str__(self) -> str:
        s = str(self.node)
        # TODO: Decide whether to use (X)+ or X+ based on type of X
        if " " in s:
            return f"({s})+"
        else:
            return f"{s}+"

    def __repr__(self) -> str:
        return f"Repeat1({self.node!r})"

    def nullable_visit(self, rules: Dict[str, Rule]) -> bool:
        return False

    def to_rule(self, varnum):
        try:
            func = f"self.{'expect' if self.node.value not in keywords else 'expect_keyword'}"
        except AttributeError:
            func = "self.expect"
        atom = f"'{str(self.node)}'"
        if type(self.node) != StringLeaf and str(self.node).islower():
            func = f"self.{self.node.to_rule(varnum)}"
            atom = ""
        if type(self.node) == Group:
            func = f"self.synthetic_rule_{self.node.synthNum}"
            atom = ""
        if type(self.node) == NameLeaf and self.node.value.islower():
            func = f"self.{self.node.value}"
        return f"(n{varnum} := self.loop(True, {func}, {atom}))"

# NOTE: Theoretically never gets used?
class Gather(Repeat):
    def __init__(self, separator: Plain, node: Plain):
        self.separator = separator
        self.node = node

    def __str__(self) -> str:
        return f"{self.separator!s}.{self.node!s}+"

    def __repr__(self) -> str:
        return f"Gather({self.separator!r}, {self.node!r})"

    def nullable_visit(self, rules: Dict[str, Rule]) -> bool:
        return False

class Group:
    def __init__(self, rhs: Rhs, synthNum: int = None):
        self.rhs = rhs
        self.synthNum = synthNum

    def __str__(self) -> str:
        return f"({self.rhs})"

    def __repr__(self) -> str:
        return f"Group({self.rhs!r})"

    def __iter__(self) -> Iterator[Rhs]:
        yield self.rhs

    def nullable_visit(self, rules: Dict[str, Rule]) -> bool:
        return self.rhs.nullable_visit(rules)

    def initial_names(self) -> AbstractSet[str]:
        return self.rhs.initial_names()

    def to_rule(self, varnum):
        return self.rhs.to_rule(varnum, True, self.synthNum)

class Cut:
    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        return f"Cut()"

    def __str__(self) -> str:
        return f"~"

    def __iter__(self) -> Iterator[Tuple[str, str]]:
        if False:
            yield

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Cut):
            return NotImplemented
        return True

    def nullable_visit(self, rules: Dict[str, Rule]) -> bool:
        return True

    def initial_names(self) -> AbstractSet[str]:
        return set()

    def to_rule(self, varnum):
        return f"True"

Plain = Union[Leaf, Group]
Item = Union[Plain, Opt, Repeat, Lookahead, Rhs, Cut]
RuleName = Tuple[str, str]
MetaTuple = Tuple[str, Optional[str]]
MetaList = List[MetaTuple]
RuleList = List[Rule]
NamedItemList = List[NamedItem]
LookaheadOrCut = Union[Lookahead, Cut]
