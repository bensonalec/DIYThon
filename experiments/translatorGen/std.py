
from tokenize import TokenInfo, COMMENT, NEWLINE

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
                if token.type in (NEWLINE, COMMENT):
                    continue
                break
            self.tokens.append(token)
        return self.tokens[self.pos]

    def look_ahead(self, positive, func, *args):
        mark = self.mark()
        ok = func(*args) is not None
        self.reset(mark)
        return ok == positive

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

