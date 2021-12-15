from tokenize import ERRORTOKEN, NL, COMMENT


class Tokenizer:
    def __init__(self, tokengen):
        """Call with tokenize.generate_tokens(...)."""
        self.tokengen = tokengen
        self.tokens = []
        self.pos = 0

    def mark(self):
        return self.pos

    def reset(self, pos):
        if pos == self.pos:
            return
        self.pos = pos

    def get_token(self):
        token = self.peek_token()
        self.pos += 1
        return token

    def peek_token(self):
        if self.pos == len(self.tokens):
            while True:
                token = next(self.tokengen)
                if token.type == ERRORTOKEN and token.string.isspace():
                    continue
                if token.type in (NL, COMMENT):
                    continue
                break
            self.tokens.append(token)
        return self.tokens[self.pos]
