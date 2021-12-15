from Parser import Parser, memoize
from token import *
class ToyParser(Parser):
    @memoize
    def start(self):
        pos = self.mark()
        if((synth1 := self.loop(False, self.synth1)) is not None):
            print(synth1)
            return ('start', [synth1])
        self.reset(pos)
        return None

    @memoize
    def expr(self):
        pos = self.mark()
        if( 
            (expr := self.expr()) is not None and
            (op := self.expect('<<')) is not None and
            (term := self.term()) is not None
        ):
            return ('expr', [expr, op, term])
        if( 
            (expr := self.expr()) is not None and
            (op := self.expect('>>')) is not None and
            (term := self.term()) is not None
        ):
            return ('expr', [expr, op, term])
        if(
            (term := self.term()) is not None
        ):
            return ('expr', [term])
        self.reset(pos)
        return None

    @memoize
    def term(self):
        pos = self.mark()
        if((number := self.expect(NUMBER)) is not None):
            return ('Term', number)
        self.reset(pos)
        return None

    @memoize
    def synth1(self):
        pos = self.mark()
        if (
            (expr := self.expr()) is not None and
            (newline := self.expect(NEWLINE)) is not None
        ):
            print(expr)
            return ('Synth', [expr])
        self.reset(pos)
        return None