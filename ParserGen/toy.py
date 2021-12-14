# This is @generated code; do not edit!
from token import NAME, NUMBER, STRING, NEWLINE, ENDMARKER
from memo import memoize, memoize_left_rec
from Node import Node
from Parser import Parser

class ToyParser(Parser):

    @memoize
    def start(self):
        self.show_rule('start', [['_synthetic_rule_0*']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (_synthetic_rule_0 := self.loop(False, self._synthetic_rule_0)) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('start', [_synthetic_rule_0])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize_left_rec
    def expr(self):
        self.show_rule('*' + 'expr', [['expr', "'<<'", "'<'", 'term'], ['expr', "'>>'", "'>'", 'term'], ['expr', "'<<'", 'term'], ['expr', "'>>'", 'term'], ['term']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (expr := self.expr()) is not None
            and self.show_index(0, 1)
            and self.expect('<<') is not None
            and self.show_index(0, 2)
            and self.expect('<') is not None
            and self.show_index(0, 3)
            and (term := self.term()) is not None
        ):
            self.show_index(0, 0, 4)
            retval = f"({expr} << {term}) | ({expr} >> (16 - {term}))"
            if retval is not None:
                return retval
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (expr := self.expr()) is not None
            and self.show_index(1, 1)
            and self.expect('>>') is not None
            and self.show_index(1, 2)
            and self.expect('>') is not None
            and self.show_index(1, 3)
            and (term := self.term()) is not None
        ):
            self.show_index(1, 0, 4)
            retval = f"({expr} >> {term}) | ({expr} << (16 - {term})) & 0xDDDDDF"
            if retval is not None:
                return retval
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and (expr := self.expr()) is not None
            and self.show_index(2, 1)
            and self.expect('<<') is not None
            and self.show_index(2, 2)
            and (term := self.term()) is not None
        ):
            self.show_index(2, 0, 3)
            retval = f"{expr} << {term}"
            if retval is not None:
                return retval
        self.reset(pos)
        if (True
            and self.show_index(3, 0)
            and (expr := self.expr()) is not None
            and self.show_index(3, 1)
            and self.expect('>>') is not None
            and self.show_index(3, 2)
            and (term := self.term()) is not None
        ):
            self.show_index(3, 0, 3)
            retval = f"{expr} >> {term}"
            if retval is not None:
                return retval
        self.reset(pos)
        if (True
            and self.show_index(4, 0)
            and (term := self.term()) is not None
        ):
            self.show_index(4, 0, 1)
            retval = term
            if retval is not None:
                return retval
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def term(self):
        self.show_rule('term', [['NUMBER']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (number := self.expect(NUMBER)) is not None
        ):
            self.show_index(0, 0, 1)
            retval = number . string
            if retval is not None:
                return retval
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_0(self):
        self.show_rule('_synthetic_rule_0', [['expr', 'NEWLINE']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (expr := self.expr()) is not None
            and self.show_index(0, 1)
            and (newline := self.expect(NEWLINE)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_0', [expr, newline])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None
