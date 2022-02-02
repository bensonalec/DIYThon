
from tokenize import TokenInfo, COMMENT, NEWLINE, ERRORTOKEN

class Tokenizer:
    def __init__(self, tokengen):
        self.tokengen = tokengen
        self.tokens = []
        self.pos = 0

    def mark(self):
        return self.pos

    def reset(self, pos):
        self.pos = pos

    def get_token(self):
        token = self.peek_token()
        self.pos += 1
        return token

    def peek_token(self):
        if self.pos == len(self.tokens):
            while True:
                token = next(self.tokengen)
                if token.type in (COMMENT,) or (token.type == ERRORTOKEN and token.string == ' '):
                    continue
                break
            self.tokens.append(token)
        return self.tokens[self.pos]

class Node:
    def __init__(self, type, children):
        self.type = type
        self.children = children

    def __repr__(self):
        return f"({self.type}, {[x if type(x) != TokenInfo else x.string for x in self.children]})"

class Parser:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.memos = {}

    def mark(self):
        return self.tokenizer.mark()

    def reset(self, pos):
        self.tokenizer.reset(pos)

    def expect(self, arg):
        token = self.tokenizer.peek_token()
        if token.type == arg or token.string == arg:
            return self.tokenizer.get_token()
        return None

    def lookahead(self, positive, func, *args):
        mark = self.mark()
        ok = func(*args) is not None
        self.reset(mark)
        return ok == positive

    def loop(self, nonempty, func, *args):
        mark = self.mark()
        nodes = []
        while node := func(*args) is not None:
            nodes.append(node)
        if len(nodes) >= nonempty:
            return nodes
        self.reset(mark)
        return None


class Lookahead:
    def __init__(self, direction, sub):
        self.direction = direction
        self.sub = sub
    def toRule(self, varnumber):
        func = "self.expect"
        if(type(self.sub) not in [AtomToken, AtomString]):
            func = f"self.{self.sub}"
        if(type(self.sub) is AtomRule):
            self.sub = ""
        return f"self.lookahead({self.direction}, {func}, {self.sub})"

class Multiple:
    def __init__(self, base, sub):
        self.base = base
        self.sub = sub
    def toRule(self, varnumber):
        func = "self.expect"
        atom = self.sub
        if(type(self.sub) not in [AtomToken, AtomString]):
            func = f"self.{self.sub}"
            atom = ""
        if(type(self.sub) is SynthRule):
            func = f"self.synthetic_rule_{self.sub.synthNumber}"
            atom = ""
        return f"(n{varnumber} := self.loop({self.base}, {func}, {atom}))"

class Optional:
    def __init__(self, sub):
        self.sub = sub
    def toRule(self, varnumber):
        if type(self.sub) == list:
            toReturn = "(("
            itemList = []
            for item in self.sub:
                itemList.append(f"{item.toRule(varnumber)}")
            toReturn += " and ".join(itemList)
            toReturn += ") or True)"
            return toReturn
        else:
            return f"({self.sub.toRule(varnumber)} or True)"

class Commit:
    def __init__(self):
        pass
    def toRule(self, varnumber):
        return f"True"

class SynthRule:
    def __init__ (self, sub, synthNumber):
        self.sub = sub
        self.synthNumber = synthNumber

    def toRule(self, varnumber):
        return f"(n{varnumber} := self.synthetic_rule_{self.synthNumber}())"
    def __repr__(self):
        return f"synthetic_rule_{self.synthNumber}"
class AtomString:
    def __init__(self, sub):
        self.sub = sub
    def toRule(self, varnumber):
        return f"self.expect({self.sub})"
    def __repr__(self):
        return self.sub
class AtomRule:
    def __init__(self, sub):
        self.sub = sub
    def toRule(self, varnumber):
        return f"(n{varnumber} := self.{self.sub}())"
    def __repr__(self):
        return f"{self.sub}"
class AtomToken:
    def __init__(self, sub):
        self.sub = sub
    def toRule(self, varnumber):
        return f"(n{varnumber} := self.expect(tokenize.{self.sub}))"
    def __repr__(self):
        return f"tokenize.{self.sub}"
