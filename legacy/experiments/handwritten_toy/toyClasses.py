from tokenize import NAME, NUMBER
from std import Parser, Node
class statement():
    def __init__(self, part):
        self.part = part
    
    def translate(self):
        return f"{self.part.translate()}"

    def __repr__(self):
        return f"{self.part}"

class assignment():
    def __init__(self, target, expr):
        self.target = target
        self.expr = expr    
    
    def translate(self):
        return f"{self.target} := {self.expr.translate()}"

    def __repr__(self):
        return f"{self.target} = {self.expr}"

class target():
    def __init__(self, name):
        self.name = name
    
    def translate(self):
        return f"{self.name.string}"

    def __repr__(self):
        return f"{self.name.string}"

class expr():
    def __init__(self, left, right=None, operator=None):
        self.left = left
        self.right = right
        self.operator = operator

    def translate(self):
        return f"{self.left.translate()} {self.operator} {self.right.translate()}" if self.right else f"{self.left.translate()}"

    def __repr__(self):
        return f"{self.left} {self.operator} {self.right}" if self.right else f"{self.left}"

class term():
    def __init__(self, atom, term=None, operation=None):
        self.atom = atom
        self.term = term
        self.operation = operation
    
    def translate(self):
        return f"{self.atom.translate()} {self.operation} {self.term}" if self.operation else f"{self.atom.translate()}"

    def __repr__(self):
        return f"{self.atom} {self.operation} {self.term}" if self.operation else f"{self.atom}"

class atom():
    def __init__(self, term, isParen=False):
        self.term = term
        self.isParen = isParen
    
    def translate(self):
        return f"({self.term.string})" if self.isParen else f"{self.term.string}"

    def __repr__(self):
        return f"({self.term.string})" if self.isParen else f"{self.term.string}"

class ToyParser(Parser):

    def statement(self):
        if a := self.assignment():
            return statement(a)
        if e := self.expr():
            return statement(e)
        if i := self.if_statement():
            return statement(i)
        return None

    def expr(self):
        if t := self.term():
            pos = self.mark()
            if op := self.expect("+"):
                if e := self.expr():
                    return expr(t, e, "+")
            self.reset(pos)
            if op := self.expect("-"):
                if e := self.expr():
                    return expr(t, e, "-")
            self.reset(pos)
            return expr(t)
        return None

    def term(self):
        if t := self.atom():
            pos = self.mark()
            if op := self.expect("*"):
                if e := self.term():
                    return term(t, e, "*")
            self.reset(pos)
            if op := self.expect("/"):
                if e := self.term():
                    return term(t, e, "/")
            self.reset(pos)
            return term(t)
        return None

    def atom(self):
        if token := self.expect(NAME):
            return atom(token)
        if token := self.expect(NUMBER):
            return atom(token)
        pos = self.mark()
        if self.expect("("):
            if e := self.expr():
                if self.expect(")"):
                    return atom(e, True)
        self.reset(pos)
        return None

    def assignment(self):
        pos = self.mark()
        if ((t := self.target()) and
            self.expect("=") and
            (e := self.expr())):
            return assignment(t, e)
        self.reset(pos)
        return None

    def target(self):
        name = self.expect(NAME)
        return target(name)

    def if_statement(self):
        pos = self.mark()
        if (self.expect("if") and
            (e := self.expr()) and
            self.expect(":") and
            (s := self.statement())):
            return Node("if", [e, s])
        self.reset(pos)
        return None
