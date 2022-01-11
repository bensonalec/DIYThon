from tokenize import NAME, ENDMARKER, STRING, NEWLINE, TokenInfo

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
            self.tokens.append(next(self.tokengen))
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

    def mark(self):
        return self.tokenizer.mark()

    def reset(self, pos):
        self.tokenizer.reset(pos)

    def expect(self, arg):
        token = self.tokenizer.peek_token()
        if token.type == arg or token.string == arg:
            return self.tokenizer.get_token()
        return None


class GrammarParser(Parser):

    def start(self):
        if r := self.rules():
            pos = self.mark()
            if marker := self.expect(ENDMARKER):
                return Node("start", [r])
            self.reset(pos)
        return None

    def rules(self):
        if r := self.rule():
            pos = self.mark()
            if rSin := self.rules():
                return Node("rules", [r, rSin])
            self.reset(pos)
            return Node("rules", [r])
        return None

    def rule(self):
        pos = self.mark()
        if (n := self.expect(NAME) 
            and self.expect(":") 
            and (a := self.alts()) 
            and self.expect("{") 
            and (t := self.alt()) 
            and self.expect("}") 
            and self.expect(NEWLINE)
        ):
            return Node("rule", [n, a, t])
        self.reset(pos)
        return None

    def alts(self):
        if a := self.alt():
            pos = self.mark()
            if self.expect("|"):
                if aSin := self.alts():
                    return Node("alts", [a, aSin])
            self.reset(pos)
            return Node('alts', [a])
        return None 

    def alt(self):
        if i := self.items():
            return Node('alt', [i])
        return None

    def items(self):
        if i := self.item():
            pos = self.mark()
            if iSin := self.items():
                return Node('items', [i, iSin])
            self.reset(pos)
            return Node('items', [i])
        return None
    
    def item(self):
        pos = self.mark()
        if n := self.expect(NAME):
            return Node('item', [n])
        self.reset(pos)
        if s := self.expect(STRING):
            return Node('item', [s])
        return None
