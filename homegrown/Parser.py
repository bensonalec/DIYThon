def memoize(func):
    def memoize_wrapper(self, *args):
        pos = self.mark()
        memo = self.memos.get(pos)
        if memo is None:
            memo = self.memos[pos] = {}
        key = (func, args)
        if key in memo:
            res, endpos = memo[key]
            self.reset(endpos)
        else:
            res = func(self, *args)
            endpos = self.mark()
            memo[key] = res, endpos
        return res
    return memoize_wrapper



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

    def loop(self, nonempty, func, *args):
        mark = self.mark()
        nodes = []
        while (node := func(*args)) is not None:
            nodes.append(node)
        if len(nodes) >= nonempty:
            return nodes
        self.reset(mark)
        return None

    def lookahead(self, positive, func, *args):
        mark = self.mark()
        ok = func(*args) is not None
        self.reset(mark)
        return ok == positive
    

