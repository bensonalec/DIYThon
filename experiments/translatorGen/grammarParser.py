from collections import namedtuple
from tokenize import NAME, ENDMARKER, STRING, NEWLINE, COMMENT
from std import AtomRule, AtomString, AtomToken, Lookahead, Parser, Multiple, Optional, Commit, SynthRule

Rule = namedtuple("Rule", "Name Alts Translations")

class GrammarParser(Parser):
    rules = []
    synthNumber = 0
    def grammar(self):
        pos = self.mark()
        if r := self.rule():
            rules = [r]
            while r := self.rule():
                rules.append(r)
            if self.expect(ENDMARKER):
                self.rules.extend(rules)
                return rules
        self.reset(pos)
        return None

    def rule(self):
        pos = self.mark()
        if ((name := self.expect(NAME)) and self.expect(":") and (alts := self.alts())):
            currentRule = Rule(name.string, alts, [])
            if t := self.translation():
                currentRule.Translations.extend(t)
                return currentRule
        self.reset(pos)
        return None

    def alts(self):
        pos = self.mark()
        if (alt := self.alternative()):
            alts = [alt]
            tPos = self.mark()
            while(self.expect("|") and (alt := self.alternative())):
                alts.append(alt)
                tPos = self.mark()
            self.reset(tPos)
            return alts
        self.reset(pos)
        pos = self.mark()
        if (self.expect("|") and (alt := self.alternative())):
            alts = [alt]
            tPos = self.mark()
            while(self.expect("|") and (alt := self.alternative())):
                alts.append(alt)
                tPos = self.mark()
            self.reset(tPos)
            return alts
        self.reset(pos)
        return None

    def alternative(self):
        pos = self.mark()
        if i := self.item():
            items = [i]
            while i := self.item():
                items.append(i)
            return items
        self.reset(pos)
        return None

    def item(self):
        pos = self.mark()
        if ((self.expect('&')) and (atom := self.atom())):
            return Lookahead(True, atom)
        self.reset(pos)
        pos = self.mark()
        if ((self.expect('!')) and (atom := self.atom())):
            return Lookahead(False, atom)
        self.reset(pos)
        pos = self.mark()
        if ((atom := self.atom()) and self.expect('*')):
            return Multiple(True, atom)
        self.reset(pos)
        pos = self.mark()
        if ((atom := self.atom()) and self.expect('+')):
            return Multiple(False, atom)
        self.reset(pos)
        pos = self.mark()
        if ((atom := self.atom()) and self.expect('?')):
            return Optional(atom)
        self.reset(pos)
        pos = self.mark()
        if ((self.expect('[')) and (alt := self.alternative()) and (self.expect(']'))):
            return Optional(alt)
        self.reset(pos)
        pos = self.mark()
        if self.expect('~'):
            return Commit()
        self.reset(pos)
        pos = self.mark()
        if atom := self.atom():
            return atom
        self.reset(pos)
        return None

    def atom(self):
        pos = self.mark()
        if p := self.expect(NAME):
            return AtomRule(p.string) if p.string.islower() else AtomToken(p.string)
        self.reset(pos)
        pos = self.mark()
        if p := self.expect(STRING):
            return AtomString(p.string)
        self.reset(pos)
        pos = self.mark()
        if (self.expect('(') and (alts := self.alts()) and self.expect(')')):
            self.rules.append(Rule(f"synthetic_rule_{self.synthNumber}", alts, ["_"]))
            self.synthNumber += 1
            return SynthRule(alts, self.synthNumber-1)
        self.reset(pos)
        return None

    def translation(self):
        pos = self.mark()
        if (self.expect("{") and (a := self.translationAlternative())):
            alts = [a]
            tPos = self.mark()
            while(self.expect("|") and (a := self.translationAlternative())):
                alts.append(a)
                tPos = self.mark()
            self.reset(tPos)
            if self.expect("}"):
                return alts
        self.reset(pos)

    def translationAlternative(self):
        pos = self.mark()
        if i := self.translationItem():
            items = [i]
            while i := self.translationItem():
                items.append(i)
            return items
        self.reset(pos)
        return None

    def translationItem(self):
        pos = self.mark()
        if p := self.expect(NAME):
            return p.string
        self.reset(pos)
        pos = self.mark()
        if p := self.expect(STRING):
            return p.string
        self.reset(pos)
        return None

    def generateCode(self):
        output = ""
        output += f"from memo import memoize_left_rec\n"
        output += f"import tokenize\n"
        output += f"from std import Parser\n"
        nodes = []
        methods = []
        varNumber = 0
        if self.rules:
            for rule in self.rules:
                currentNode = ""
                currentMethod = ""
                #build node code
                for ind,translation in enumerate(rule.Translations):
                    variables = [x for x in translation if x.startswith('_')]
                    currentNode += f'class {rule.Name}{"0" if not rule.Name.startswith("synthetic_rule_") else ""}:\n'
                    currentNode += f'\tdef __init__(self, {", ".join([f"{x}" for x in variables])}{"," if len(variables) > 0 else ""} *rest):\n'
                    for var in variables:
                        currentNode += f'\t\tself.{var} = {var}\n'
                    currentNode += "\t\tpass\n"
                    currentNode += f'\tdef translate(self):\n'
                    currentNode += f'\t\treturn f"{"".join([f"{{self.{x}.translate() if type(self.{x}) != str else self.{x}}}" if x in variables else f"{{{x}}}" for x in translation])}"\n'
                nodes.append(currentNode)

                #build parsing method code
                currentMethod += "\t@memoize_left_rec\n"
                currentMethod += f'\tdef {rule.Name}(self):\n'
                for ind, alternative in enumerate(rule.Alts):
                    variables = []
                    tokenInfos = []
                    currentMethod += '\t\tpos = self.mark()\n'
                    currentMethod += f'\t\tif (True and\n'
                    for item in alternative:
                        # print(item.toRule(varNumber))
                        if type(item) in [AtomRule, AtomToken, Multiple]:
                            variables.append(f"n{varNumber}")
                        if type(item) in [AtomToken]:
                            tokenInfos.append(f"n{varNumber}")
                        ruleString = item.toRule(varNumber)
                        varNumber += 1
                        currentMethod += f"\t\t {ruleString} is not None and\n"
                    currentMethod += '\t\t   True):\n'
                    currentMethod += f'\t\t\treturn {rule.Name}{"0" if not rule.Name.startswith("synthetic_rule_") else ""}({", ".join([x if x not in tokenInfos else f"{x}.string" for x in variables])})\n'
                    currentMethod += '\t\tself.reset(pos)\n'
                currentMethod += '\t\treturn None\n'
                methods.append(currentMethod)
        output += "\n".join([x for x in nodes])
        output += "class ToyParser(Parser):\n"
        output += "\n".join([x for x in methods])
        print(output)