# This is @generated code; do not edit!
from token import ASYNC, AWAIT, DEDENT, INDENT, NAME, NUMBER, STRING, NEWLINE, ENDMARKER, TYPE_COMMENT
from memo import memoize, memoize_left_rec
from Node import Node
from Parser import Parser

class PythonParser(Parser):

    @memoize
    def file(self):
        self.show_rule('file', [['[statements]', 'ENDMARKER']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and ((statements := self.statements()) is not None or True)
            and self.show_index(0, 1)
            and (endmarker := self.expect(ENDMARKER)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('file', [statements, endmarker])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def interactive(self):
        self.show_rule('interactive', [['statement_newline']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (statement_newline := self.statement_newline()) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('interactive', [statement_newline])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def eval(self):
        self.show_rule('eval', [['expressions', 'NEWLINE*', 'ENDMARKER']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (expressions := self.expressions()) is not None
            and self.show_index(0, 1)
            and (newline := self.loop(False, self.expect, NEWLINE)) is not None
            and self.show_index(0, 2)
            and (endmarker := self.expect(ENDMARKER)) is not None
        ):
            self.show_index(0, 0, 3)
            return Node('eval', [expressions, newline, endmarker])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def func_type(self):
        self.show_rule('func_type', [["'('", '[type_expressions]', "')'", "'->'", 'expression', 'NEWLINE*', 'ENDMARKER']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('(') is not None
            and self.show_index(0, 1)
            and ((type_expressions := self.type_expressions()) is not None or True)
            and self.show_index(0, 2)
            and self.expect(')') is not None
            and self.show_index(0, 3)
            and self.expect('->') is not None
            and self.show_index(0, 4)
            and (expression := self.expression()) is not None
            and self.show_index(0, 5)
            and (newline := self.loop(False, self.expect, NEWLINE)) is not None
            and self.show_index(0, 6)
            and (endmarker := self.expect(ENDMARKER)) is not None
        ):
            self.show_index(0, 0, 7)
            return Node('func_type', [type_expressions, expression, newline, endmarker])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def fstring(self):
        self.show_rule('fstring', [['star_expressions']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (star_expressions := self.star_expressions()) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('fstring', [star_expressions])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def type_expressions(self):
        self.show_rule('type_expressions', [['_synthetic_rule_1', "','", "'*'", 'expression', "','", "'**'", 'expression'], ['_synthetic_rule_3', "','", "'*'", 'expression'], ['_synthetic_rule_5', "','", "'**'", 'expression'], ["'*'", 'expression', "','", "'**'", 'expression'], ["'*'", 'expression'], ["'**'", 'expression'], ['_synthetic_rule_7']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (_synthetic_rule_1 := self._synthetic_rule_1()) is not None
            and self.show_index(0, 1)
            and self.expect(',') is not None
            and self.show_index(0, 2)
            and self.expect('*') is not None
            and self.show_index(0, 3)
            and (expression := self.expression()) is not None
            and self.show_index(0, 4)
            and self.expect(',') is not None
            and self.show_index(0, 5)
            and self.expect('**') is not None
            and self.show_index(0, 6)
            and (expression2 := self.expression()) is not None
        ):
            self.show_index(0, 0, 7)
            return Node('type_expressions', [_synthetic_rule_1, expression, expression2])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (_synthetic_rule_3 := self._synthetic_rule_3()) is not None
            and self.show_index(1, 1)
            and self.expect(',') is not None
            and self.show_index(1, 2)
            and self.expect('*') is not None
            and self.show_index(1, 3)
            and (expression := self.expression()) is not None
        ):
            self.show_index(1, 0, 4)
            return Node('type_expressions', [_synthetic_rule_3, expression])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and (_synthetic_rule_5 := self._synthetic_rule_5()) is not None
            and self.show_index(2, 1)
            and self.expect(',') is not None
            and self.show_index(2, 2)
            and self.expect('**') is not None
            and self.show_index(2, 3)
            and (expression := self.expression()) is not None
        ):
            self.show_index(2, 0, 4)
            return Node('type_expressions', [_synthetic_rule_5, expression])
        self.reset(pos)
        if (True
            and self.show_index(3, 0)
            and self.expect('*') is not None
            and self.show_index(3, 1)
            and (expression := self.expression()) is not None
            and self.show_index(3, 2)
            and self.expect(',') is not None
            and self.show_index(3, 3)
            and self.expect('**') is not None
            and self.show_index(3, 4)
            and (expression1 := self.expression()) is not None
        ):
            self.show_index(3, 0, 5)
            return Node('type_expressions', [expression, expression1])
        self.reset(pos)
        if (True
            and self.show_index(4, 0)
            and self.expect('*') is not None
            and self.show_index(4, 1)
            and (expression := self.expression()) is not None
        ):
            self.show_index(4, 0, 2)
            return Node('type_expressions', [expression])
        self.reset(pos)
        if (True
            and self.show_index(5, 0)
            and self.expect('**') is not None
            and self.show_index(5, 1)
            and (expression := self.expression()) is not None
        ):
            self.show_index(5, 0, 2)
            return Node('type_expressions', [expression])
        self.reset(pos)
        if (True
            and self.show_index(6, 0)
            and (_synthetic_rule_7 := self._synthetic_rule_7()) is not None
        ):
            self.show_index(6, 0, 1)
            return Node('type_expressions', [_synthetic_rule_7])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def statements(self):
        self.show_rule('statements', [['statement+']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (statement := self.loop(True, self.statement)) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('statements', [statement])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def statement(self):
        self.show_rule('statement', [['compound_stmt'], ['simple_stmts']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (compound_stmt := self.compound_stmt()) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('statement', [compound_stmt])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (simple_stmts := self.simple_stmts()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('statement', [simple_stmts])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def statement_newline(self):
        self.show_rule('statement_newline', [['compound_stmt', 'NEWLINE'], ['simple_stmts'], ['NEWLINE'], ['ENDMARKER']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (compound_stmt := self.compound_stmt()) is not None
            and self.show_index(0, 1)
            and (newline := self.expect(NEWLINE)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('statement_newline', [compound_stmt, newline])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (simple_stmts := self.simple_stmts()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('statement_newline', [simple_stmts])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and (newline := self.expect(NEWLINE)) is not None
        ):
            self.show_index(2, 0, 1)
            return Node('statement_newline', [newline])
        self.reset(pos)
        if (True
            and self.show_index(3, 0)
            and (endmarker := self.expect(ENDMARKER)) is not None
        ):
            self.show_index(3, 0, 1)
            return Node('statement_newline', [endmarker])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def simple_stmts(self):
        self.show_rule('simple_stmts', [['simple_stmt', "!';'", 'NEWLINE'], ['_synthetic_rule_9', "[';']", 'NEWLINE']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (simple_stmt := self.simple_stmt()) is not None
            and self.show_index(0, 1)
            and self.lookahead(False, self.expect, ';')
            and self.show_index(0, 2)
            and (newline := self.expect(NEWLINE)) is not None
        ):
            self.show_index(0, 0, 3)
            return Node('simple_stmts', [simple_stmt, newline])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (_synthetic_rule_9 := self._synthetic_rule_9()) is not None
            and self.show_index(1, 1)
            and (self.expect(';') is not None or True)
            and self.show_index(1, 2)
            and (newline := self.expect(NEWLINE)) is not None
        ):
            self.show_index(1, 0, 3)
            return Node('simple_stmts', [_synthetic_rule_9, newline])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def simple_stmt(self):
        self.show_rule('simple_stmt', [['assignment'], ['star_expressions'], ['return_stmt'], ['import_stmt'], ['raise_stmt'], ["'pass'"], ['del_stmt'], ['yield_stmt'], ['assert_stmt'], ["'break'"], ["'continue'"], ['global_stmt'], ['nonlocal_stmt']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (assignment := self.assignment()) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('simple_stmt', [assignment])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (star_expressions := self.star_expressions()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('simple_stmt', [star_expressions])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and (return_stmt := self.return_stmt()) is not None
        ):
            self.show_index(2, 0, 1)
            return Node('simple_stmt', [return_stmt])
        self.reset(pos)
        if (True
            and self.show_index(3, 0)
            and (import_stmt := self.import_stmt()) is not None
        ):
            self.show_index(3, 0, 1)
            return Node('simple_stmt', [import_stmt])
        self.reset(pos)
        if (True
            and self.show_index(4, 0)
            and (raise_stmt := self.raise_stmt()) is not None
        ):
            self.show_index(4, 0, 1)
            return Node('simple_stmt', [raise_stmt])
        self.reset(pos)
        if (True
            and self.show_index(5, 0)
            and self.expect('pass') is not None
        ):
            self.show_index(5, 0, 1)
            return Node('simple_stmt', [])
        self.reset(pos)
        if (True
            and self.show_index(6, 0)
            and (del_stmt := self.del_stmt()) is not None
        ):
            self.show_index(6, 0, 1)
            return Node('simple_stmt', [del_stmt])
        self.reset(pos)
        if (True
            and self.show_index(7, 0)
            and (yield_stmt := self.yield_stmt()) is not None
        ):
            self.show_index(7, 0, 1)
            return Node('simple_stmt', [yield_stmt])
        self.reset(pos)
        if (True
            and self.show_index(8, 0)
            and (assert_stmt := self.assert_stmt()) is not None
        ):
            self.show_index(8, 0, 1)
            return Node('simple_stmt', [assert_stmt])
        self.reset(pos)
        if (True
            and self.show_index(9, 0)
            and self.expect('break') is not None
        ):
            self.show_index(9, 0, 1)
            return Node('simple_stmt', [])
        self.reset(pos)
        if (True
            and self.show_index(10, 0)
            and self.expect('continue') is not None
        ):
            self.show_index(10, 0, 1)
            return Node('simple_stmt', [])
        self.reset(pos)
        if (True
            and self.show_index(11, 0)
            and (global_stmt := self.global_stmt()) is not None
        ):
            self.show_index(11, 0, 1)
            return Node('simple_stmt', [global_stmt])
        self.reset(pos)
        if (True
            and self.show_index(12, 0)
            and (nonlocal_stmt := self.nonlocal_stmt()) is not None
        ):
            self.show_index(12, 0, 1)
            return Node('simple_stmt', [nonlocal_stmt])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def compound_stmt(self):
        self.show_rule('compound_stmt', [['function_def'], ['if_stmt'], ['class_def'], ['with_stmt'], ['for_stmt'], ['try_stmt'], ['while_stmt'], ['match_stmt']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (function_def := self.function_def()) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('compound_stmt', [function_def])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (if_stmt := self.if_stmt()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('compound_stmt', [if_stmt])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and (class_def := self.class_def()) is not None
        ):
            self.show_index(2, 0, 1)
            return Node('compound_stmt', [class_def])
        self.reset(pos)
        if (True
            and self.show_index(3, 0)
            and (with_stmt := self.with_stmt()) is not None
        ):
            self.show_index(3, 0, 1)
            return Node('compound_stmt', [with_stmt])
        self.reset(pos)
        if (True
            and self.show_index(4, 0)
            and (for_stmt := self.for_stmt()) is not None
        ):
            self.show_index(4, 0, 1)
            return Node('compound_stmt', [for_stmt])
        self.reset(pos)
        if (True
            and self.show_index(5, 0)
            and (try_stmt := self.try_stmt()) is not None
        ):
            self.show_index(5, 0, 1)
            return Node('compound_stmt', [try_stmt])
        self.reset(pos)
        if (True
            and self.show_index(6, 0)
            and (while_stmt := self.while_stmt()) is not None
        ):
            self.show_index(6, 0, 1)
            return Node('compound_stmt', [while_stmt])
        self.reset(pos)
        if (True
            and self.show_index(7, 0)
            and (match_stmt := self.match_stmt()) is not None
        ):
            self.show_index(7, 0, 1)
            return Node('compound_stmt', [match_stmt])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def assignment(self):
        self.show_rule('assignment', [['NAME', "':'", 'expression', '[_synthetic_rule_10]'], ['_synthetic_rule_11', "':'", 'expression', '[_synthetic_rule_12]'], ['_synthetic_rule_13+', '_synthetic_rule_14', "!'='", '[TYPE_COMMENT]'], ['single_target', 'augassign', '~', '_synthetic_rule_15']])
        pos = self.mark()
        cut = False
        if (True
            and self.show_index(0, 0)
            and (name := self.expect(NAME)) is not None
            and self.show_index(0, 1)
            and self.expect(':') is not None
            and self.show_index(0, 2)
            and (expression := self.expression()) is not None
            and self.show_index(0, 3)
            and ((_synthetic_rule_10 := self._synthetic_rule_10()) is not None or True)
        ):
            self.show_index(0, 0, 4)
            return Node('assignment', [name, expression, _synthetic_rule_10])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (_synthetic_rule_11 := self._synthetic_rule_11()) is not None
            and self.show_index(1, 1)
            and self.expect(':') is not None
            and self.show_index(1, 2)
            and (expression := self.expression()) is not None
            and self.show_index(1, 3)
            and ((_synthetic_rule_12 := self._synthetic_rule_12()) is not None or True)
        ):
            self.show_index(1, 0, 4)
            return Node('assignment', [_synthetic_rule_11, expression, _synthetic_rule_12])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and (_synthetic_rule_13 := self.loop(True, self._synthetic_rule_13)) is not None
            and self.show_index(2, 1)
            and (_synthetic_rule_14 := self._synthetic_rule_14()) is not None
            and self.show_index(2, 2)
            and self.lookahead(False, self.expect, '=')
            and self.show_index(2, 3)
            and ((type_comment := self.expect(TYPE_COMMENT)) is not None or True)
        ):
            self.show_index(2, 0, 4)
            return Node('assignment', [_synthetic_rule_13, _synthetic_rule_14, type_comment])
        self.reset(pos)
        if (True
            and self.show_index(3, 0)
            and (single_target := self.single_target()) is not None
            and self.show_index(3, 1)
            and (augassign := self.augassign()) is not None
            and self.show_index(3, 2)
            and True
            and self.show_index(3, 3)
            and (_synthetic_rule_15 := self._synthetic_rule_15()) is not None
        ):
            self.show_index(3, 0, 4)
            return Node('assignment', [single_target, augassign, _synthetic_rule_15])
        self.reset(pos)
        if cut:
            self.show_index(0, 0, 0)
            return None
        self.show_index(0, 0, 0)
        return None

    @memoize
    def augassign(self):
        self.show_rule('augassign', [["'+='"], ["'-='"], ["'*='"], ["'@='"], ["'/='"], ["'%='"], ["'&='"], ["'|='"], ["'^='"], ["'<<='"], ["'>>='"], ["'**='"], ["'//='"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('+=') is not None
        ):
            self.show_index(0, 0, 1)
            return Node('augassign', [])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and self.expect('-=') is not None
        ):
            self.show_index(1, 0, 1)
            return Node('augassign', [])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and self.expect('*=') is not None
        ):
            self.show_index(2, 0, 1)
            return Node('augassign', [])
        self.reset(pos)
        if (True
            and self.show_index(3, 0)
            and self.expect('@=') is not None
        ):
            self.show_index(3, 0, 1)
            return Node('augassign', [])
        self.reset(pos)
        if (True
            and self.show_index(4, 0)
            and self.expect('/=') is not None
        ):
            self.show_index(4, 0, 1)
            return Node('augassign', [])
        self.reset(pos)
        if (True
            and self.show_index(5, 0)
            and self.expect('%=') is not None
        ):
            self.show_index(5, 0, 1)
            return Node('augassign', [])
        self.reset(pos)
        if (True
            and self.show_index(6, 0)
            and self.expect('&=') is not None
        ):
            self.show_index(6, 0, 1)
            return Node('augassign', [])
        self.reset(pos)
        if (True
            and self.show_index(7, 0)
            and self.expect('|=') is not None
        ):
            self.show_index(7, 0, 1)
            return Node('augassign', [])
        self.reset(pos)
        if (True
            and self.show_index(8, 0)
            and self.expect('^=') is not None
        ):
            self.show_index(8, 0, 1)
            return Node('augassign', [])
        self.reset(pos)
        if (True
            and self.show_index(9, 0)
            and self.expect('<<=') is not None
        ):
            self.show_index(9, 0, 1)
            return Node('augassign', [])
        self.reset(pos)
        if (True
            and self.show_index(10, 0)
            and self.expect('>>=') is not None
        ):
            self.show_index(10, 0, 1)
            return Node('augassign', [])
        self.reset(pos)
        if (True
            and self.show_index(11, 0)
            and self.expect('**=') is not None
        ):
            self.show_index(11, 0, 1)
            return Node('augassign', [])
        self.reset(pos)
        if (True
            and self.show_index(12, 0)
            and self.expect('//=') is not None
        ):
            self.show_index(12, 0, 1)
            return Node('augassign', [])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def global_stmt(self):
        self.show_rule('global_stmt', [["'global'", '_synthetic_rule_17']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('global') is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_17 := self._synthetic_rule_17()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('global_stmt', [_synthetic_rule_17])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def nonlocal_stmt(self):
        self.show_rule('nonlocal_stmt', [["'nonlocal'", '_synthetic_rule_19']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('nonlocal') is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_19 := self._synthetic_rule_19()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('nonlocal_stmt', [_synthetic_rule_19])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def yield_stmt(self):
        self.show_rule('yield_stmt', [['yield_expr']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (yield_expr := self.yield_expr()) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('yield_stmt', [yield_expr])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def assert_stmt(self):
        self.show_rule('assert_stmt', [["'assert'", 'expression', '[_synthetic_rule_20]']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('assert') is not None
            and self.show_index(0, 1)
            and (expression := self.expression()) is not None
            and self.show_index(0, 2)
            and ((_synthetic_rule_20 := self._synthetic_rule_20()) is not None or True)
        ):
            self.show_index(0, 0, 3)
            return Node('assert_stmt', [expression, _synthetic_rule_20])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def del_stmt(self):
        self.show_rule('del_stmt', [["'del'", 'del_targets', '&_synthetic_rule_21']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('del') is not None
            and self.show_index(0, 1)
            and (del_targets := self.del_targets()) is not None
            and self.show_index(0, 2)
            and self.lookahead(True, self._synthetic_rule_21)
        ):
            self.show_index(0, 0, 3)
            return Node('del_stmt', [del_targets])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def import_stmt(self):
        self.show_rule('import_stmt', [['import_name'], ['import_from']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (import_name := self.import_name()) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('import_stmt', [import_name])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (import_from := self.import_from()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('import_stmt', [import_from])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def import_name(self):
        self.show_rule('import_name', [["'import'", 'dotted_as_names']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('import') is not None
            and self.show_index(0, 1)
            and (dotted_as_names := self.dotted_as_names()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('import_name', [dotted_as_names])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def import_from(self):
        self.show_rule('import_from', [["'from'", '_synthetic_rule_22*', 'dotted_name', "'import'", 'import_from_targets'], ["'from'", '_synthetic_rule_23+', "'import'", 'import_from_targets']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('from') is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_22 := self.loop(False, self._synthetic_rule_22)) is not None
            and self.show_index(0, 2)
            and (dotted_name := self.dotted_name()) is not None
            and self.show_index(0, 3)
            and self.expect('import') is not None
            and self.show_index(0, 4)
            and (import_from_targets := self.import_from_targets()) is not None
        ):
            self.show_index(0, 0, 5)
            return Node('import_from', [_synthetic_rule_22, dotted_name, import_from_targets])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and self.expect('from') is not None
            and self.show_index(1, 1)
            and (_synthetic_rule_23 := self.loop(True, self._synthetic_rule_23)) is not None
            and self.show_index(1, 2)
            and self.expect('import') is not None
            and self.show_index(1, 3)
            and (import_from_targets := self.import_from_targets()) is not None
        ):
            self.show_index(1, 0, 4)
            return Node('import_from', [_synthetic_rule_23, import_from_targets])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def import_from_targets(self):
        self.show_rule('import_from_targets', [["'('", 'import_from_as_names', "[',']", "')'"], ['import_from_as_names', "!','"], ["'*'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('(') is not None
            and self.show_index(0, 1)
            and (import_from_as_names := self.import_from_as_names()) is not None
            and self.show_index(0, 2)
            and (self.expect(',') is not None or True)
            and self.show_index(0, 3)
            and self.expect(')') is not None
        ):
            self.show_index(0, 0, 4)
            return Node('import_from_targets', [import_from_as_names])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (import_from_as_names := self.import_from_as_names()) is not None
            and self.show_index(1, 1)
            and self.lookahead(False, self.expect, ',')
        ):
            self.show_index(1, 0, 2)
            return Node('import_from_targets', [import_from_as_names])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and self.expect('*') is not None
        ):
            self.show_index(2, 0, 1)
            return Node('import_from_targets', [])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def import_from_as_names(self):
        self.show_rule('import_from_as_names', [['_synthetic_rule_25']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (_synthetic_rule_25 := self._synthetic_rule_25()) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('import_from_as_names', [_synthetic_rule_25])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def import_from_as_name(self):
        self.show_rule('import_from_as_name', [['NAME', '[_synthetic_rule_26]']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (name := self.expect(NAME)) is not None
            and self.show_index(0, 1)
            and ((_synthetic_rule_26 := self._synthetic_rule_26()) is not None or True)
        ):
            self.show_index(0, 0, 2)
            return Node('import_from_as_name', [name, _synthetic_rule_26])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def dotted_as_names(self):
        self.show_rule('dotted_as_names', [['_synthetic_rule_28']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (_synthetic_rule_28 := self._synthetic_rule_28()) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('dotted_as_names', [_synthetic_rule_28])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def dotted_as_name(self):
        self.show_rule('dotted_as_name', [['dotted_name', '[_synthetic_rule_29]']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (dotted_name := self.dotted_name()) is not None
            and self.show_index(0, 1)
            and ((_synthetic_rule_29 := self._synthetic_rule_29()) is not None or True)
        ):
            self.show_index(0, 0, 2)
            return Node('dotted_as_name', [dotted_name, _synthetic_rule_29])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize_left_rec
    def dotted_name(self):
        self.show_rule('*' + 'dotted_name', [['dotted_name', "'.'", 'NAME'], ['NAME']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (dotted_name := self.dotted_name()) is not None
            and self.show_index(0, 1)
            and self.expect('.') is not None
            and self.show_index(0, 2)
            and (name := self.expect(NAME)) is not None
        ):
            self.show_index(0, 0, 3)
            return Node('dotted_name', [dotted_name, name])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (name := self.expect(NAME)) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('dotted_name', [name])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def if_stmt(self):
        self.show_rule('if_stmt', [["'if'", 'named_expression', "':'", 'block', 'elif_stmt'], ["'if'", 'named_expression', "':'", 'block', '[else_block]']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('if') is not None
            and self.show_index(0, 1)
            and (named_expression := self.named_expression()) is not None
            and self.show_index(0, 2)
            and self.expect(':') is not None
            and self.show_index(0, 3)
            and (block := self.block()) is not None
            and self.show_index(0, 4)
            and (elif_stmt := self.elif_stmt()) is not None
        ):
            self.show_index(0, 0, 5)
            return Node('if_stmt', [named_expression, block, elif_stmt])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and self.expect('if') is not None
            and self.show_index(1, 1)
            and (named_expression := self.named_expression()) is not None
            and self.show_index(1, 2)
            and self.expect(':') is not None
            and self.show_index(1, 3)
            and (block := self.block()) is not None
            and self.show_index(1, 4)
            and ((else_block := self.else_block()) is not None or True)
        ):
            self.show_index(1, 0, 5)
            return Node('if_stmt', [named_expression, block, else_block])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def elif_stmt(self):
        self.show_rule('elif_stmt', [["'elif'", 'named_expression', "':'", 'block', 'elif_stmt'], ["'elif'", 'named_expression', "':'", 'block', '[else_block]']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('elif') is not None
            and self.show_index(0, 1)
            and (named_expression := self.named_expression()) is not None
            and self.show_index(0, 2)
            and self.expect(':') is not None
            and self.show_index(0, 3)
            and (block := self.block()) is not None
            and self.show_index(0, 4)
            and (elif_stmt := self.elif_stmt()) is not None
        ):
            self.show_index(0, 0, 5)
            return Node('elif_stmt', [named_expression, block, elif_stmt])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and self.expect('elif') is not None
            and self.show_index(1, 1)
            and (named_expression := self.named_expression()) is not None
            and self.show_index(1, 2)
            and self.expect(':') is not None
            and self.show_index(1, 3)
            and (block := self.block()) is not None
            and self.show_index(1, 4)
            and ((else_block := self.else_block()) is not None or True)
        ):
            self.show_index(1, 0, 5)
            return Node('elif_stmt', [named_expression, block, else_block])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def else_block(self):
        self.show_rule('else_block', [["'else'", "':'", 'block']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('else') is not None
            and self.show_index(0, 1)
            and self.expect(':') is not None
            and self.show_index(0, 2)
            and (block := self.block()) is not None
        ):
            self.show_index(0, 0, 3)
            return Node('else_block', [block])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def while_stmt(self):
        self.show_rule('while_stmt', [["'while'", 'named_expression', "':'", 'block', '[else_block]']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('while') is not None
            and self.show_index(0, 1)
            and (named_expression := self.named_expression()) is not None
            and self.show_index(0, 2)
            and self.expect(':') is not None
            and self.show_index(0, 3)
            and (block := self.block()) is not None
            and self.show_index(0, 4)
            and ((else_block := self.else_block()) is not None or True)
        ):
            self.show_index(0, 0, 5)
            return Node('while_stmt', [named_expression, block, else_block])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def for_stmt(self):
        self.show_rule('for_stmt', [["'for'", 'star_targets', "'in'", '~', 'star_expressions', "':'", '[TYPE_COMMENT]', 'block', '[else_block]'], ['ASYNC', "'for'", 'star_targets', "'in'", '~', 'star_expressions', "':'", '[TYPE_COMMENT]', 'block', '[else_block]']])
        pos = self.mark()
        cut = False
        if (True
            and self.show_index(0, 0)
            and self.expect('for') is not None
            and self.show_index(0, 1)
            and (star_targets := self.star_targets()) is not None
            and self.show_index(0, 2)
            and self.expect('in') is not None
            and self.show_index(0, 3)
            and True
            and self.show_index(0, 4)
            and (star_expressions := self.star_expressions()) is not None
            and self.show_index(0, 5)
            and self.expect(':') is not None
            and self.show_index(0, 6)
            and ((type_comment := self.expect(TYPE_COMMENT)) is not None or True)
            and self.show_index(0, 7)
            and (block := self.block()) is not None
            and self.show_index(0, 8)
            and ((else_block := self.else_block()) is not None or True)
        ):
            self.show_index(0, 0, 9)
            return Node('for_stmt', [star_targets, star_expressions, type_comment, block, else_block])
        self.reset(pos)
        if cut:
            self.show_index(0, 0, 0)
            return None
        if (True
            and self.show_index(1, 0)
            and (async_var := self.expect(ASYNC)) is not None
            and self.show_index(1, 1)
            and self.expect('for') is not None
            and self.show_index(1, 2)
            and (star_targets := self.star_targets()) is not None
            and self.show_index(1, 3)
            and self.expect('in') is not None
            and self.show_index(1, 4)
            and True
            and self.show_index(1, 5)
            and (star_expressions := self.star_expressions()) is not None
            and self.show_index(1, 6)
            and self.expect(':') is not None
            and self.show_index(1, 7)
            and ((type_comment := self.expect(TYPE_COMMENT)) is not None or True)
            and self.show_index(1, 8)
            and (block := self.block()) is not None
            and self.show_index(1, 9)
            and ((else_block := self.else_block()) is not None or True)
        ):
            self.show_index(1, 0, 10)
            return Node('for_stmt', [async_var, star_targets, star_expressions, type_comment, block, else_block])
        self.reset(pos)
        if cut:
            self.show_index(0, 0, 0)
            return None
        self.show_index(0, 0, 0)
        return None

    @memoize
    def with_stmt(self):
        self.show_rule('with_stmt', [["'with'", "'('", '_synthetic_rule_31', "[',']", "')'", "':'", 'block'], ["'with'", '_synthetic_rule_33', "':'", '[TYPE_COMMENT]', 'block'], ['ASYNC', "'with'", "'('", '_synthetic_rule_35', "[',']", "')'", "':'", 'block'], ['ASYNC', "'with'", '_synthetic_rule_37', "':'", '[TYPE_COMMENT]', 'block']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('with') is not None
            and self.show_index(0, 1)
            and self.expect('(') is not None
            and self.show_index(0, 2)
            and (_synthetic_rule_31 := self._synthetic_rule_31()) is not None
            and self.show_index(0, 3)
            and (self.expect(',') is not None or True)
            and self.show_index(0, 4)
            and self.expect(')') is not None
            and self.show_index(0, 5)
            and self.expect(':') is not None
            and self.show_index(0, 6)
            and (block := self.block()) is not None
        ):
            self.show_index(0, 0, 7)
            return Node('with_stmt', [_synthetic_rule_31, block])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and self.expect('with') is not None
            and self.show_index(1, 1)
            and (_synthetic_rule_33 := self._synthetic_rule_33()) is not None
            and self.show_index(1, 2)
            and self.expect(':') is not None
            and self.show_index(1, 3)
            and ((type_comment := self.expect(TYPE_COMMENT)) is not None or True)
            and self.show_index(1, 4)
            and (block := self.block()) is not None
        ):
            self.show_index(1, 0, 5)
            return Node('with_stmt', [_synthetic_rule_33, type_comment, block])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and (async_var := self.expect(ASYNC)) is not None
            and self.show_index(2, 1)
            and self.expect('with') is not None
            and self.show_index(2, 2)
            and self.expect('(') is not None
            and self.show_index(2, 3)
            and (_synthetic_rule_35 := self._synthetic_rule_35()) is not None
            and self.show_index(2, 4)
            and (self.expect(',') is not None or True)
            and self.show_index(2, 5)
            and self.expect(')') is not None
            and self.show_index(2, 6)
            and self.expect(':') is not None
            and self.show_index(2, 7)
            and (block := self.block()) is not None
        ):
            self.show_index(2, 0, 8)
            return Node('with_stmt', [async_var, _synthetic_rule_35, block])
        self.reset(pos)
        if (True
            and self.show_index(3, 0)
            and (async_var := self.expect(ASYNC)) is not None
            and self.show_index(3, 1)
            and self.expect('with') is not None
            and self.show_index(3, 2)
            and (_synthetic_rule_37 := self._synthetic_rule_37()) is not None
            and self.show_index(3, 3)
            and self.expect(':') is not None
            and self.show_index(3, 4)
            and ((type_comment := self.expect(TYPE_COMMENT)) is not None or True)
            and self.show_index(3, 5)
            and (block := self.block()) is not None
        ):
            self.show_index(3, 0, 6)
            return Node('with_stmt', [async_var, _synthetic_rule_37, type_comment, block])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def with_item(self):
        self.show_rule('with_item', [['expression', "'as'", 'star_target', '&_synthetic_rule_38'], ['expression']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (expression := self.expression()) is not None
            and self.show_index(0, 1)
            and self.expect('as') is not None
            and self.show_index(0, 2)
            and (star_target := self.star_target()) is not None
            and self.show_index(0, 3)
            and self.lookahead(True, self._synthetic_rule_38)
        ):
            self.show_index(0, 0, 4)
            return Node('with_item', [expression, star_target])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (expression := self.expression()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('with_item', [expression])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def try_stmt(self):
        self.show_rule('try_stmt', [["'try'", "':'", 'block', 'finally_block'], ["'try'", "':'", 'block', 'except_block+', '[else_block]', '[finally_block]']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('try') is not None
            and self.show_index(0, 1)
            and self.expect(':') is not None
            and self.show_index(0, 2)
            and (block := self.block()) is not None
            and self.show_index(0, 3)
            and (finally_block := self.finally_block()) is not None
        ):
            self.show_index(0, 0, 4)
            return Node('try_stmt', [block, finally_block])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and self.expect('try') is not None
            and self.show_index(1, 1)
            and self.expect(':') is not None
            and self.show_index(1, 2)
            and (block := self.block()) is not None
            and self.show_index(1, 3)
            and (except_block := self.loop(True, self.except_block)) is not None
            and self.show_index(1, 4)
            and ((else_block := self.else_block()) is not None or True)
            and self.show_index(1, 5)
            and ((finally_block := self.finally_block()) is not None or True)
        ):
            self.show_index(1, 0, 6)
            return Node('try_stmt', [block, except_block, else_block, finally_block])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def except_block(self):
        self.show_rule('except_block', [["'except'", 'expression', '[_synthetic_rule_39]', "':'", 'block'], ["'except'", "':'", 'block']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('except') is not None
            and self.show_index(0, 1)
            and (expression := self.expression()) is not None
            and self.show_index(0, 2)
            and ((_synthetic_rule_39 := self._synthetic_rule_39()) is not None or True)
            and self.show_index(0, 3)
            and self.expect(':') is not None
            and self.show_index(0, 4)
            and (block := self.block()) is not None
        ):
            self.show_index(0, 0, 5)
            return Node('except_block', [expression, _synthetic_rule_39, block])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and self.expect('except') is not None
            and self.show_index(1, 1)
            and self.expect(':') is not None
            and self.show_index(1, 2)
            and (block := self.block()) is not None
        ):
            self.show_index(1, 0, 3)
            return Node('except_block', [block])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def finally_block(self):
        self.show_rule('finally_block', [["'finally'", "':'", 'block']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('finally') is not None
            and self.show_index(0, 1)
            and self.expect(':') is not None
            and self.show_index(0, 2)
            and (block := self.block()) is not None
        ):
            self.show_index(0, 0, 3)
            return Node('finally_block', [block])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def match_stmt(self):
        self.show_rule('match_stmt', [['"match"', 'subject_expr', "':'", 'NEWLINE', 'INDENT', 'case_block+', 'DEDENT']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect("match") is not None
            and self.show_index(0, 1)
            and (subject_expr := self.subject_expr()) is not None
            and self.show_index(0, 2)
            and self.expect(':') is not None
            and self.show_index(0, 3)
            and (newline := self.expect(NEWLINE)) is not None
            and self.show_index(0, 4)
            and (indent := self.expect(INDENT)) is not None
            and self.show_index(0, 5)
            and (case_block := self.loop(True, self.case_block)) is not None
            and self.show_index(0, 6)
            and (dedent := self.expect(DEDENT)) is not None
        ):
            self.show_index(0, 0, 7)
            return Node('match_stmt', [subject_expr, newline, indent, case_block, dedent])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def subject_expr(self):
        self.show_rule('subject_expr', [['star_named_expression', "','", '[star_named_expressions]'], ['named_expression']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (star_named_expression := self.star_named_expression()) is not None
            and self.show_index(0, 1)
            and self.expect(',') is not None
            and self.show_index(0, 2)
            and ((star_named_expressions := self.star_named_expressions()) is not None or True)
        ):
            self.show_index(0, 0, 3)
            return Node('subject_expr', [star_named_expression, star_named_expressions])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (named_expression := self.named_expression()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('subject_expr', [named_expression])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def case_block(self):
        self.show_rule('case_block', [['"case"', 'patterns', '[guard]', "':'", 'block']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect("case") is not None
            and self.show_index(0, 1)
            and (patterns := self.patterns()) is not None
            and self.show_index(0, 2)
            and ((guard := self.guard()) is not None or True)
            and self.show_index(0, 3)
            and self.expect(':') is not None
            and self.show_index(0, 4)
            and (block := self.block()) is not None
        ):
            self.show_index(0, 0, 5)
            return Node('case_block', [patterns, guard, block])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def guard(self):
        self.show_rule('guard', [["'if'", 'named_expression']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('if') is not None
            and self.show_index(0, 1)
            and (named_expression := self.named_expression()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('guard', [named_expression])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def patterns(self):
        self.show_rule('patterns', [['open_sequence_pattern'], ['pattern']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (open_sequence_pattern := self.open_sequence_pattern()) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('patterns', [open_sequence_pattern])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (pattern := self.pattern()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('patterns', [pattern])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def pattern(self):
        self.show_rule('pattern', [['as_pattern'], ['or_pattern']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (as_pattern := self.as_pattern()) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('pattern', [as_pattern])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (or_pattern := self.or_pattern()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('pattern', [or_pattern])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def as_pattern(self):
        self.show_rule('as_pattern', [['or_pattern', "'as'", 'pattern_capture_target']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (or_pattern := self.or_pattern()) is not None
            and self.show_index(0, 1)
            and self.expect('as') is not None
            and self.show_index(0, 2)
            and (pattern_capture_target := self.pattern_capture_target()) is not None
        ):
            self.show_index(0, 0, 3)
            return Node('as_pattern', [or_pattern, pattern_capture_target])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def or_pattern(self):
        self.show_rule('or_pattern', [['_synthetic_rule_41']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (_synthetic_rule_41 := self._synthetic_rule_41()) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('or_pattern', [_synthetic_rule_41])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def closed_pattern(self):
        self.show_rule('closed_pattern', [['literal_pattern'], ['capture_pattern'], ['wildcard_pattern'], ['value_pattern'], ['group_pattern'], ['sequence_pattern'], ['mapping_pattern'], ['class_pattern']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (literal_pattern := self.literal_pattern()) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('closed_pattern', [literal_pattern])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (capture_pattern := self.capture_pattern()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('closed_pattern', [capture_pattern])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and (wildcard_pattern := self.wildcard_pattern()) is not None
        ):
            self.show_index(2, 0, 1)
            return Node('closed_pattern', [wildcard_pattern])
        self.reset(pos)
        if (True
            and self.show_index(3, 0)
            and (value_pattern := self.value_pattern()) is not None
        ):
            self.show_index(3, 0, 1)
            return Node('closed_pattern', [value_pattern])
        self.reset(pos)
        if (True
            and self.show_index(4, 0)
            and (group_pattern := self.group_pattern()) is not None
        ):
            self.show_index(4, 0, 1)
            return Node('closed_pattern', [group_pattern])
        self.reset(pos)
        if (True
            and self.show_index(5, 0)
            and (sequence_pattern := self.sequence_pattern()) is not None
        ):
            self.show_index(5, 0, 1)
            return Node('closed_pattern', [sequence_pattern])
        self.reset(pos)
        if (True
            and self.show_index(6, 0)
            and (mapping_pattern := self.mapping_pattern()) is not None
        ):
            self.show_index(6, 0, 1)
            return Node('closed_pattern', [mapping_pattern])
        self.reset(pos)
        if (True
            and self.show_index(7, 0)
            and (class_pattern := self.class_pattern()) is not None
        ):
            self.show_index(7, 0, 1)
            return Node('closed_pattern', [class_pattern])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def literal_pattern(self):
        self.show_rule('literal_pattern', [['signed_number', '!_synthetic_rule_42'], ['complex_number'], ['strings'], ["'None'"], ["'True'"], ["'False'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (signed_number := self.signed_number()) is not None
            and self.show_index(0, 1)
            and self.lookahead(False, self._synthetic_rule_42)
        ):
            self.show_index(0, 0, 2)
            return Node('literal_pattern', [signed_number])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (complex_number := self.complex_number()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('literal_pattern', [complex_number])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and (strings := self.strings()) is not None
        ):
            self.show_index(2, 0, 1)
            return Node('literal_pattern', [strings])
        self.reset(pos)
        if (True
            and self.show_index(3, 0)
            and self.expect('None') is not None
        ):
            self.show_index(3, 0, 1)
            return Node('literal_pattern', [])
        self.reset(pos)
        if (True
            and self.show_index(4, 0)
            and self.expect('True') is not None
        ):
            self.show_index(4, 0, 1)
            return Node('literal_pattern', [])
        self.reset(pos)
        if (True
            and self.show_index(5, 0)
            and self.expect('False') is not None
        ):
            self.show_index(5, 0, 1)
            return Node('literal_pattern', [])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def literal_expr(self):
        self.show_rule('literal_expr', [['signed_number', '!_synthetic_rule_43'], ['complex_number'], ['strings'], ["'None'"], ["'True'"], ["'False'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (signed_number := self.signed_number()) is not None
            and self.show_index(0, 1)
            and self.lookahead(False, self._synthetic_rule_43)
        ):
            self.show_index(0, 0, 2)
            return Node('literal_expr', [signed_number])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (complex_number := self.complex_number()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('literal_expr', [complex_number])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and (strings := self.strings()) is not None
        ):
            self.show_index(2, 0, 1)
            return Node('literal_expr', [strings])
        self.reset(pos)
        if (True
            and self.show_index(3, 0)
            and self.expect('None') is not None
        ):
            self.show_index(3, 0, 1)
            return Node('literal_expr', [])
        self.reset(pos)
        if (True
            and self.show_index(4, 0)
            and self.expect('True') is not None
        ):
            self.show_index(4, 0, 1)
            return Node('literal_expr', [])
        self.reset(pos)
        if (True
            and self.show_index(5, 0)
            and self.expect('False') is not None
        ):
            self.show_index(5, 0, 1)
            return Node('literal_expr', [])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def complex_number(self):
        self.show_rule('complex_number', [['signed_real_number', "'+'", 'imaginary_number'], ['signed_real_number', "'-'", 'imaginary_number']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (signed_real_number := self.signed_real_number()) is not None
            and self.show_index(0, 1)
            and self.expect('+') is not None
            and self.show_index(0, 2)
            and (imaginary_number := self.imaginary_number()) is not None
        ):
            self.show_index(0, 0, 3)
            return Node('complex_number', [signed_real_number, imaginary_number])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (signed_real_number := self.signed_real_number()) is not None
            and self.show_index(1, 1)
            and self.expect('-') is not None
            and self.show_index(1, 2)
            and (imaginary_number := self.imaginary_number()) is not None
        ):
            self.show_index(1, 0, 3)
            return Node('complex_number', [signed_real_number, imaginary_number])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def signed_number(self):
        self.show_rule('signed_number', [['NUMBER'], ["'-'", 'NUMBER']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (number := self.expect(NUMBER)) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('signed_number', [number])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and self.expect('-') is not None
            and self.show_index(1, 1)
            and (number := self.expect(NUMBER)) is not None
        ):
            self.show_index(1, 0, 2)
            return Node('signed_number', [number])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def signed_real_number(self):
        self.show_rule('signed_real_number', [['real_number'], ["'-'", 'real_number']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (real_number := self.real_number()) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('signed_real_number', [real_number])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and self.expect('-') is not None
            and self.show_index(1, 1)
            and (real_number := self.real_number()) is not None
        ):
            self.show_index(1, 0, 2)
            return Node('signed_real_number', [real_number])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def real_number(self):
        self.show_rule('real_number', [['NUMBER']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (number := self.expect(NUMBER)) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('real_number', [number])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def imaginary_number(self):
        self.show_rule('imaginary_number', [['NUMBER']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (number := self.expect(NUMBER)) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('imaginary_number', [number])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def capture_pattern(self):
        self.show_rule('capture_pattern', [['pattern_capture_target']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (pattern_capture_target := self.pattern_capture_target()) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('capture_pattern', [pattern_capture_target])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def pattern_capture_target(self):
        self.show_rule('pattern_capture_target', [['!"_"', 'NAME', '!_synthetic_rule_44']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.lookahead(False, self.expect, "_")
            and self.show_index(0, 1)
            and (name := self.expect(NAME)) is not None
            and self.show_index(0, 2)
            and self.lookahead(False, self._synthetic_rule_44)
        ):
            self.show_index(0, 0, 3)
            return Node('pattern_capture_target', [name])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def wildcard_pattern(self):
        self.show_rule('wildcard_pattern', [['"_"']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect("_") is not None
        ):
            self.show_index(0, 0, 1)
            return Node('wildcard_pattern', [])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def value_pattern(self):
        self.show_rule('value_pattern', [['attr', '!_synthetic_rule_45']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (attr := self.attr()) is not None
            and self.show_index(0, 1)
            and self.lookahead(False, self._synthetic_rule_45)
        ):
            self.show_index(0, 0, 2)
            return Node('value_pattern', [attr])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def attr(self):
        self.show_rule('attr', [['name_or_attr', "'.'", 'NAME']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (name_or_attr := self.name_or_attr()) is not None
            and self.show_index(0, 1)
            and self.expect('.') is not None
            and self.show_index(0, 2)
            and (name := self.expect(NAME)) is not None
        ):
            self.show_index(0, 0, 3)
            return Node('attr', [name_or_attr, name])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def name_or_attr(self):
        self.show_rule('name_or_attr', [['attr'], ['NAME']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (attr := self.attr()) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('name_or_attr', [attr])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (name := self.expect(NAME)) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('name_or_attr', [name])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def group_pattern(self):
        self.show_rule('group_pattern', [["'('", 'pattern', "')'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('(') is not None
            and self.show_index(0, 1)
            and (pattern := self.pattern()) is not None
            and self.show_index(0, 2)
            and self.expect(')') is not None
        ):
            self.show_index(0, 0, 3)
            return Node('group_pattern', [pattern])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def sequence_pattern(self):
        self.show_rule('sequence_pattern', [["'['", '[maybe_sequence_pattern]', "']'"], ["'('", '[open_sequence_pattern]', "')'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('[') is not None
            and self.show_index(0, 1)
            and ((maybe_sequence_pattern := self.maybe_sequence_pattern()) is not None or True)
            and self.show_index(0, 2)
            and self.expect(']') is not None
        ):
            self.show_index(0, 0, 3)
            return Node('sequence_pattern', [maybe_sequence_pattern])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and self.expect('(') is not None
            and self.show_index(1, 1)
            and ((open_sequence_pattern := self.open_sequence_pattern()) is not None or True)
            and self.show_index(1, 2)
            and self.expect(')') is not None
        ):
            self.show_index(1, 0, 3)
            return Node('sequence_pattern', [open_sequence_pattern])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def open_sequence_pattern(self):
        self.show_rule('open_sequence_pattern', [['maybe_star_pattern', "','", '[maybe_sequence_pattern]']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (maybe_star_pattern := self.maybe_star_pattern()) is not None
            and self.show_index(0, 1)
            and self.expect(',') is not None
            and self.show_index(0, 2)
            and ((maybe_sequence_pattern := self.maybe_sequence_pattern()) is not None or True)
        ):
            self.show_index(0, 0, 3)
            return Node('open_sequence_pattern', [maybe_star_pattern, maybe_sequence_pattern])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def maybe_sequence_pattern(self):
        self.show_rule('maybe_sequence_pattern', [['_synthetic_rule_47', "[',']"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (_synthetic_rule_47 := self._synthetic_rule_47()) is not None
            and self.show_index(0, 1)
            and (self.expect(',') is not None or True)
        ):
            self.show_index(0, 0, 2)
            return Node('maybe_sequence_pattern', [_synthetic_rule_47])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def maybe_star_pattern(self):
        self.show_rule('maybe_star_pattern', [['star_pattern'], ['pattern']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (star_pattern := self.star_pattern()) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('maybe_star_pattern', [star_pattern])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (pattern := self.pattern()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('maybe_star_pattern', [pattern])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def star_pattern(self):
        self.show_rule('star_pattern', [["'*'", 'pattern_capture_target'], ["'*'", 'wildcard_pattern']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('*') is not None
            and self.show_index(0, 1)
            and (pattern_capture_target := self.pattern_capture_target()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('star_pattern', [pattern_capture_target])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and self.expect('*') is not None
            and self.show_index(1, 1)
            and (wildcard_pattern := self.wildcard_pattern()) is not None
        ):
            self.show_index(1, 0, 2)
            return Node('star_pattern', [wildcard_pattern])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def mapping_pattern(self):
        self.show_rule('mapping_pattern', [["'{'", "'}'"], ["'{'", 'double_star_pattern', "[',']", "'}'"], ["'{'", 'items_pattern', "','", 'double_star_pattern', "[',']", "'}'"], ["'{'", 'items_pattern', "[',']", "'}'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('{') is not None
            and self.show_index(0, 1)
            and self.expect('}') is not None
        ):
            self.show_index(0, 0, 2)
            return Node('mapping_pattern', [])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and self.expect('{') is not None
            and self.show_index(1, 1)
            and (double_star_pattern := self.double_star_pattern()) is not None
            and self.show_index(1, 2)
            and (self.expect(',') is not None or True)
            and self.show_index(1, 3)
            and self.expect('}') is not None
        ):
            self.show_index(1, 0, 4)
            return Node('mapping_pattern', [double_star_pattern])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and self.expect('{') is not None
            and self.show_index(2, 1)
            and (items_pattern := self.items_pattern()) is not None
            and self.show_index(2, 2)
            and self.expect(',') is not None
            and self.show_index(2, 3)
            and (double_star_pattern := self.double_star_pattern()) is not None
            and self.show_index(2, 4)
            and (self.expect(',') is not None or True)
            and self.show_index(2, 5)
            and self.expect('}') is not None
        ):
            self.show_index(2, 0, 6)
            return Node('mapping_pattern', [items_pattern, double_star_pattern])
        self.reset(pos)
        if (True
            and self.show_index(3, 0)
            and self.expect('{') is not None
            and self.show_index(3, 1)
            and (items_pattern := self.items_pattern()) is not None
            and self.show_index(3, 2)
            and (self.expect(',') is not None or True)
            and self.show_index(3, 3)
            and self.expect('}') is not None
        ):
            self.show_index(3, 0, 4)
            return Node('mapping_pattern', [items_pattern])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def items_pattern(self):
        self.show_rule('items_pattern', [['_synthetic_rule_49']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (_synthetic_rule_49 := self._synthetic_rule_49()) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('items_pattern', [_synthetic_rule_49])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def key_value_pattern(self):
        self.show_rule('key_value_pattern', [['_synthetic_rule_50', "':'", 'pattern']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (_synthetic_rule_50 := self._synthetic_rule_50()) is not None
            and self.show_index(0, 1)
            and self.expect(':') is not None
            and self.show_index(0, 2)
            and (pattern := self.pattern()) is not None
        ):
            self.show_index(0, 0, 3)
            return Node('key_value_pattern', [_synthetic_rule_50, pattern])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def double_star_pattern(self):
        self.show_rule('double_star_pattern', [["'**'", 'pattern_capture_target']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('**') is not None
            and self.show_index(0, 1)
            and (pattern_capture_target := self.pattern_capture_target()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('double_star_pattern', [pattern_capture_target])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def class_pattern(self):
        self.show_rule('class_pattern', [['name_or_attr', "'('", "')'"], ['name_or_attr', "'('", 'positional_patterns', "[',']", "')'"], ['name_or_attr', "'('", 'keyword_patterns', "[',']", "')'"], ['name_or_attr', "'('", 'positional_patterns', "','", 'keyword_patterns', "[',']", "')'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (name_or_attr := self.name_or_attr()) is not None
            and self.show_index(0, 1)
            and self.expect('(') is not None
            and self.show_index(0, 2)
            and self.expect(')') is not None
        ):
            self.show_index(0, 0, 3)
            return Node('class_pattern', [name_or_attr])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (name_or_attr := self.name_or_attr()) is not None
            and self.show_index(1, 1)
            and self.expect('(') is not None
            and self.show_index(1, 2)
            and (positional_patterns := self.positional_patterns()) is not None
            and self.show_index(1, 3)
            and (self.expect(',') is not None or True)
            and self.show_index(1, 4)
            and self.expect(')') is not None
        ):
            self.show_index(1, 0, 5)
            return Node('class_pattern', [name_or_attr, positional_patterns])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and (name_or_attr := self.name_or_attr()) is not None
            and self.show_index(2, 1)
            and self.expect('(') is not None
            and self.show_index(2, 2)
            and (keyword_patterns := self.keyword_patterns()) is not None
            and self.show_index(2, 3)
            and (self.expect(',') is not None or True)
            and self.show_index(2, 4)
            and self.expect(')') is not None
        ):
            self.show_index(2, 0, 5)
            return Node('class_pattern', [name_or_attr, keyword_patterns])
        self.reset(pos)
        if (True
            and self.show_index(3, 0)
            and (name_or_attr := self.name_or_attr()) is not None
            and self.show_index(3, 1)
            and self.expect('(') is not None
            and self.show_index(3, 2)
            and (positional_patterns := self.positional_patterns()) is not None
            and self.show_index(3, 3)
            and self.expect(',') is not None
            and self.show_index(3, 4)
            and (keyword_patterns := self.keyword_patterns()) is not None
            and self.show_index(3, 5)
            and (self.expect(',') is not None or True)
            and self.show_index(3, 6)
            and self.expect(')') is not None
        ):
            self.show_index(3, 0, 7)
            return Node('class_pattern', [name_or_attr, positional_patterns, keyword_patterns])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def positional_patterns(self):
        self.show_rule('positional_patterns', [['_synthetic_rule_52']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (_synthetic_rule_52 := self._synthetic_rule_52()) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('positional_patterns', [_synthetic_rule_52])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def keyword_patterns(self):
        self.show_rule('keyword_patterns', [['_synthetic_rule_54']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (_synthetic_rule_54 := self._synthetic_rule_54()) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('keyword_patterns', [_synthetic_rule_54])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def keyword_pattern(self):
        self.show_rule('keyword_pattern', [['NAME', "'='", 'pattern']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (name := self.expect(NAME)) is not None
            and self.show_index(0, 1)
            and self.expect('=') is not None
            and self.show_index(0, 2)
            and (pattern := self.pattern()) is not None
        ):
            self.show_index(0, 0, 3)
            return Node('keyword_pattern', [name, pattern])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def return_stmt(self):
        self.show_rule('return_stmt', [["'return'", '[star_expressions]']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('return') is not None
            and self.show_index(0, 1)
            and ((star_expressions := self.star_expressions()) is not None or True)
        ):
            self.show_index(0, 0, 2)
            return Node('return_stmt', [star_expressions])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def raise_stmt(self):
        self.show_rule('raise_stmt', [["'raise'", 'expression', '[_synthetic_rule_55]'], ["'raise'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('raise') is not None
            and self.show_index(0, 1)
            and (expression := self.expression()) is not None
            and self.show_index(0, 2)
            and ((_synthetic_rule_55 := self._synthetic_rule_55()) is not None or True)
        ):
            self.show_index(0, 0, 3)
            return Node('raise_stmt', [expression, _synthetic_rule_55])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and self.expect('raise') is not None
        ):
            self.show_index(1, 0, 1)
            return Node('raise_stmt', [])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def function_def(self):
        self.show_rule('function_def', [['decorators', 'function_def_raw'], ['function_def_raw']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (decorators := self.decorators()) is not None
            and self.show_index(0, 1)
            and (function_def_raw := self.function_def_raw()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('function_def', [decorators, function_def_raw])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (function_def_raw := self.function_def_raw()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('function_def', [function_def_raw])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def function_def_raw(self):
        self.show_rule('function_def_raw', [["'def'", 'NAME', "'('", '[params]', "')'", '[_synthetic_rule_56]', "':'", '[func_type_comment]', 'block'], ['ASYNC', "'def'", 'NAME', "'('", '[params]', "')'", '[_synthetic_rule_57]', "':'", '[func_type_comment]', 'block']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('def') is not None
            and self.show_index(0, 1)
            and (name := self.expect(NAME)) is not None
            and self.show_index(0, 2)
            and self.expect('(') is not None
            and self.show_index(0, 3)
            and ((params := self.params()) is not None or True)
            and self.show_index(0, 4)
            and self.expect(')') is not None
            and self.show_index(0, 5)
            and ((_synthetic_rule_56 := self._synthetic_rule_56()) is not None or True)
            and self.show_index(0, 6)
            and self.expect(':') is not None
            and self.show_index(0, 7)
            and ((func_type_comment := self.func_type_comment()) is not None or True)
            and self.show_index(0, 8)
            and (block := self.block()) is not None
        ):
            self.show_index(0, 0, 9)
            return Node('function_def_raw', [name, params, _synthetic_rule_56, func_type_comment, block])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (async_var := self.expect(ASYNC)) is not None
            and self.show_index(1, 1)
            and self.expect('def') is not None
            and self.show_index(1, 2)
            and (name := self.expect(NAME)) is not None
            and self.show_index(1, 3)
            and self.expect('(') is not None
            and self.show_index(1, 4)
            and ((params := self.params()) is not None or True)
            and self.show_index(1, 5)
            and self.expect(')') is not None
            and self.show_index(1, 6)
            and ((_synthetic_rule_57 := self._synthetic_rule_57()) is not None or True)
            and self.show_index(1, 7)
            and self.expect(':') is not None
            and self.show_index(1, 8)
            and ((func_type_comment := self.func_type_comment()) is not None or True)
            and self.show_index(1, 9)
            and (block := self.block()) is not None
        ):
            self.show_index(1, 0, 10)
            return Node('function_def_raw', [async_var, name, params, _synthetic_rule_57, func_type_comment, block])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def func_type_comment(self):
        self.show_rule('func_type_comment', [['NEWLINE', 'TYPE_COMMENT', '&_synthetic_rule_58'], ['TYPE_COMMENT']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (newline := self.expect(NEWLINE)) is not None
            and self.show_index(0, 1)
            and (type_comment := self.expect(TYPE_COMMENT)) is not None
            and self.show_index(0, 2)
            and self.lookahead(True, self._synthetic_rule_58)
        ):
            self.show_index(0, 0, 3)
            return Node('func_type_comment', [newline, type_comment])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (type_comment := self.expect(TYPE_COMMENT)) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('func_type_comment', [type_comment])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def params(self):
        self.show_rule('params', [['parameters']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (parameters := self.parameters()) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('params', [parameters])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def parameters(self):
        self.show_rule('parameters', [['slash_no_default', 'param_no_default*', 'param_with_default*', '[star_etc]'], ['slash_with_default', 'param_with_default*', '[star_etc]'], ['param_no_default+', 'param_with_default*', '[star_etc]'], ['param_with_default+', '[star_etc]'], ['star_etc']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (slash_no_default := self.slash_no_default()) is not None
            and self.show_index(0, 1)
            and (param_no_default := self.loop(False, self.param_no_default)) is not None
            and self.show_index(0, 2)
            and (param_with_default := self.loop(False, self.param_with_default)) is not None
            and self.show_index(0, 3)
            and ((star_etc := self.star_etc()) is not None or True)
        ):
            self.show_index(0, 0, 4)
            return Node('parameters', [slash_no_default, param_no_default, param_with_default, star_etc])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (slash_with_default := self.slash_with_default()) is not None
            and self.show_index(1, 1)
            and (param_with_default := self.loop(False, self.param_with_default)) is not None
            and self.show_index(1, 2)
            and ((star_etc := self.star_etc()) is not None or True)
        ):
            self.show_index(1, 0, 3)
            return Node('parameters', [slash_with_default, param_with_default, star_etc])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and (param_no_default := self.loop(True, self.param_no_default)) is not None
            and self.show_index(2, 1)
            and (param_with_default := self.loop(False, self.param_with_default)) is not None
            and self.show_index(2, 2)
            and ((star_etc := self.star_etc()) is not None or True)
        ):
            self.show_index(2, 0, 3)
            return Node('parameters', [param_no_default, param_with_default, star_etc])
        self.reset(pos)
        if (True
            and self.show_index(3, 0)
            and (param_with_default := self.loop(True, self.param_with_default)) is not None
            and self.show_index(3, 1)
            and ((star_etc := self.star_etc()) is not None or True)
        ):
            self.show_index(3, 0, 2)
            return Node('parameters', [param_with_default, star_etc])
        self.reset(pos)
        if (True
            and self.show_index(4, 0)
            and (star_etc := self.star_etc()) is not None
        ):
            self.show_index(4, 0, 1)
            return Node('parameters', [star_etc])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def slash_no_default(self):
        self.show_rule('slash_no_default', [['param_no_default+', "'/'", "','"], ['param_no_default+', "'/'", "&')'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (param_no_default := self.loop(True, self.param_no_default)) is not None
            and self.show_index(0, 1)
            and self.expect('/') is not None
            and self.show_index(0, 2)
            and self.expect(',') is not None
        ):
            self.show_index(0, 0, 3)
            return Node('slash_no_default', [param_no_default])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (param_no_default := self.loop(True, self.param_no_default)) is not None
            and self.show_index(1, 1)
            and self.expect('/') is not None
            and self.show_index(1, 2)
            and self.lookahead(True, self.expect, ')')
        ):
            self.show_index(1, 0, 3)
            return Node('slash_no_default', [param_no_default])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def slash_with_default(self):
        self.show_rule('slash_with_default', [['param_no_default*', 'param_with_default+', "'/'", "','"], ['param_no_default*', 'param_with_default+', "'/'", "&')'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (param_no_default := self.loop(False, self.param_no_default)) is not None
            and self.show_index(0, 1)
            and (param_with_default := self.loop(True, self.param_with_default)) is not None
            and self.show_index(0, 2)
            and self.expect('/') is not None
            and self.show_index(0, 3)
            and self.expect(',') is not None
        ):
            self.show_index(0, 0, 4)
            return Node('slash_with_default', [param_no_default, param_with_default])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (param_no_default := self.loop(False, self.param_no_default)) is not None
            and self.show_index(1, 1)
            and (param_with_default := self.loop(True, self.param_with_default)) is not None
            and self.show_index(1, 2)
            and self.expect('/') is not None
            and self.show_index(1, 3)
            and self.lookahead(True, self.expect, ')')
        ):
            self.show_index(1, 0, 4)
            return Node('slash_with_default', [param_no_default, param_with_default])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def star_etc(self):
        self.show_rule('star_etc', [["'*'", 'param_no_default', 'param_maybe_default*', '[kwds]'], ["'*'", "','", 'param_maybe_default+', '[kwds]'], ['kwds']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('*') is not None
            and self.show_index(0, 1)
            and (param_no_default := self.param_no_default()) is not None
            and self.show_index(0, 2)
            and (param_maybe_default := self.loop(False, self.param_maybe_default)) is not None
            and self.show_index(0, 3)
            and ((kwds := self.kwds()) is not None or True)
        ):
            self.show_index(0, 0, 4)
            return Node('star_etc', [param_no_default, param_maybe_default, kwds])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and self.expect('*') is not None
            and self.show_index(1, 1)
            and self.expect(',') is not None
            and self.show_index(1, 2)
            and (param_maybe_default := self.loop(True, self.param_maybe_default)) is not None
            and self.show_index(1, 3)
            and ((kwds := self.kwds()) is not None or True)
        ):
            self.show_index(1, 0, 4)
            return Node('star_etc', [param_maybe_default, kwds])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and (kwds := self.kwds()) is not None
        ):
            self.show_index(2, 0, 1)
            return Node('star_etc', [kwds])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def kwds(self):
        self.show_rule('kwds', [["'**'", 'param_no_default']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('**') is not None
            and self.show_index(0, 1)
            and (param_no_default := self.param_no_default()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('kwds', [param_no_default])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def param_no_default(self):
        self.show_rule('param_no_default', [['param', "','", '[TYPE_COMMENT]'], ['param', '[TYPE_COMMENT]', "&')'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (param := self.param()) is not None
            and self.show_index(0, 1)
            and self.expect(',') is not None
            and self.show_index(0, 2)
            and ((type_comment := self.expect(TYPE_COMMENT)) is not None or True)
        ):
            self.show_index(0, 0, 3)
            return Node('param_no_default', [param, type_comment])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (param := self.param()) is not None
            and self.show_index(1, 1)
            and ((type_comment := self.expect(TYPE_COMMENT)) is not None or True)
            and self.show_index(1, 2)
            and self.lookahead(True, self.expect, ')')
        ):
            self.show_index(1, 0, 3)
            return Node('param_no_default', [param, type_comment])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def param_with_default(self):
        self.show_rule('param_with_default', [['param', 'default', "','", '[TYPE_COMMENT]'], ['param', 'default', '[TYPE_COMMENT]', "&')'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (param := self.param()) is not None
            and self.show_index(0, 1)
            and (default := self.default()) is not None
            and self.show_index(0, 2)
            and self.expect(',') is not None
            and self.show_index(0, 3)
            and ((type_comment := self.expect(TYPE_COMMENT)) is not None or True)
        ):
            self.show_index(0, 0, 4)
            return Node('param_with_default', [param, default, type_comment])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (param := self.param()) is not None
            and self.show_index(1, 1)
            and (default := self.default()) is not None
            and self.show_index(1, 2)
            and ((type_comment := self.expect(TYPE_COMMENT)) is not None or True)
            and self.show_index(1, 3)
            and self.lookahead(True, self.expect, ')')
        ):
            self.show_index(1, 0, 4)
            return Node('param_with_default', [param, default, type_comment])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def param_maybe_default(self):
        self.show_rule('param_maybe_default', [['param', '[default]', "','", '[TYPE_COMMENT]'], ['param', '[default]', '[TYPE_COMMENT]', "&')'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (param := self.param()) is not None
            and self.show_index(0, 1)
            and ((default := self.default()) is not None or True)
            and self.show_index(0, 2)
            and self.expect(',') is not None
            and self.show_index(0, 3)
            and ((type_comment := self.expect(TYPE_COMMENT)) is not None or True)
        ):
            self.show_index(0, 0, 4)
            return Node('param_maybe_default', [param, default, type_comment])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (param := self.param()) is not None
            and self.show_index(1, 1)
            and ((default := self.default()) is not None or True)
            and self.show_index(1, 2)
            and ((type_comment := self.expect(TYPE_COMMENT)) is not None or True)
            and self.show_index(1, 3)
            and self.lookahead(True, self.expect, ')')
        ):
            self.show_index(1, 0, 4)
            return Node('param_maybe_default', [param, default, type_comment])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def param(self):
        self.show_rule('param', [['NAME', '[annotation]']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (name := self.expect(NAME)) is not None
            and self.show_index(0, 1)
            and ((annotation := self.annotation()) is not None or True)
        ):
            self.show_index(0, 0, 2)
            return Node('param', [name, annotation])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def annotation(self):
        self.show_rule('annotation', [["':'", 'expression']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect(':') is not None
            and self.show_index(0, 1)
            and (expression := self.expression()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('annotation', [expression])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def default(self):
        self.show_rule('default', [["'='", 'expression']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('=') is not None
            and self.show_index(0, 1)
            and (expression := self.expression()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('default', [expression])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def decorators(self):
        self.show_rule('decorators', [['_synthetic_rule_59+']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (_synthetic_rule_59 := self.loop(True, self._synthetic_rule_59)) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('decorators', [_synthetic_rule_59])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def class_def(self):
        self.show_rule('class_def', [['decorators', 'class_def_raw'], ['class_def_raw']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (decorators := self.decorators()) is not None
            and self.show_index(0, 1)
            and (class_def_raw := self.class_def_raw()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('class_def', [decorators, class_def_raw])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (class_def_raw := self.class_def_raw()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('class_def', [class_def_raw])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def class_def_raw(self):
        self.show_rule('class_def_raw', [["'class'", 'NAME', '[_synthetic_rule_60]', "':'", 'block']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('class') is not None
            and self.show_index(0, 1)
            and (name := self.expect(NAME)) is not None
            and self.show_index(0, 2)
            and ((_synthetic_rule_60 := self._synthetic_rule_60()) is not None or True)
            and self.show_index(0, 3)
            and self.expect(':') is not None
            and self.show_index(0, 4)
            and (block := self.block()) is not None
        ):
            self.show_index(0, 0, 5)
            return Node('class_def_raw', [name, _synthetic_rule_60, block])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def block(self):
        self.show_rule('block', [['NEWLINE', 'INDENT', 'statements', 'DEDENT'], ['simple_stmts']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (newline := self.expect(NEWLINE)) is not None
            and self.show_index(0, 1)
            and (indent := self.expect(INDENT)) is not None
            and self.show_index(0, 2)
            and (statements := self.statements()) is not None
            and self.show_index(0, 3)
            and (dedent := self.expect(DEDENT)) is not None
        ):
            self.show_index(0, 0, 4)
            return Node('block', [newline, indent, statements, dedent])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (simple_stmts := self.simple_stmts()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('block', [simple_stmts])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def star_expressions(self):
        self.show_rule('star_expressions', [['star_expression', '_synthetic_rule_61+', "[',']"], ['star_expression', "','"], ['star_expression']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (star_expression := self.star_expression()) is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_61 := self.loop(True, self._synthetic_rule_61)) is not None
            and self.show_index(0, 2)
            and (self.expect(',') is not None or True)
        ):
            self.show_index(0, 0, 3)
            return Node('star_expressions', [star_expression, _synthetic_rule_61])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (star_expression := self.star_expression()) is not None
            and self.show_index(1, 1)
            and self.expect(',') is not None
        ):
            self.show_index(1, 0, 2)
            return Node('star_expressions', [star_expression])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and (star_expression := self.star_expression()) is not None
        ):
            self.show_index(2, 0, 1)
            return Node('star_expressions', [star_expression])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def star_expression(self):
        self.show_rule('star_expression', [["'*'", 'bitwise_or'], ['expression']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('*') is not None
            and self.show_index(0, 1)
            and (bitwise_or := self.bitwise_or()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('star_expression', [bitwise_or])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (expression := self.expression()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('star_expression', [expression])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def star_named_expressions(self):
        self.show_rule('star_named_expressions', [['_synthetic_rule_63', "[',']"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (_synthetic_rule_63 := self._synthetic_rule_63()) is not None
            and self.show_index(0, 1)
            and (self.expect(',') is not None or True)
        ):
            self.show_index(0, 0, 2)
            return Node('star_named_expressions', [_synthetic_rule_63])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def star_named_expression(self):
        self.show_rule('star_named_expression', [["'*'", 'bitwise_or'], ['named_expression']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('*') is not None
            and self.show_index(0, 1)
            and (bitwise_or := self.bitwise_or()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('star_named_expression', [bitwise_or])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (named_expression := self.named_expression()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('star_named_expression', [named_expression])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def assignment_expression(self):
        self.show_rule('assignment_expression', [['NAME', "':='", '~', 'expression']])
        pos = self.mark()
        cut = False
        if (True
            and self.show_index(0, 0)
            and (name := self.expect(NAME)) is not None
            and self.show_index(0, 1)
            and self.expect(':=') is not None
            and self.show_index(0, 2)
            and True
            and self.show_index(0, 3)
            and (expression := self.expression()) is not None
        ):
            self.show_index(0, 0, 4)
            return Node('assignment_expression', [name, expression])
        self.reset(pos)
        if cut:
            self.show_index(0, 0, 0)
            return None
        self.show_index(0, 0, 0)
        return None

    @memoize
    def named_expression(self):
        self.show_rule('named_expression', [['assignment_expression'], ['expression', "!':='"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (assignment_expression := self.assignment_expression()) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('named_expression', [assignment_expression])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (expression := self.expression()) is not None
            and self.show_index(1, 1)
            and self.lookahead(False, self.expect, ':=')
        ):
            self.show_index(1, 0, 2)
            return Node('named_expression', [expression])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def annotated_rhs(self):
        self.show_rule('annotated_rhs', [['yield_expr'], ['star_expressions']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (yield_expr := self.yield_expr()) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('annotated_rhs', [yield_expr])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (star_expressions := self.star_expressions()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('annotated_rhs', [star_expressions])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def expressions(self):
        self.show_rule('expressions', [['expression', '_synthetic_rule_64+', "[',']"], ['expression', "','"], ['expression']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (expression := self.expression()) is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_64 := self.loop(True, self._synthetic_rule_64)) is not None
            and self.show_index(0, 2)
            and (self.expect(',') is not None or True)
        ):
            self.show_index(0, 0, 3)
            return Node('expressions', [expression, _synthetic_rule_64])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (expression := self.expression()) is not None
            and self.show_index(1, 1)
            and self.expect(',') is not None
        ):
            self.show_index(1, 0, 2)
            return Node('expressions', [expression])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and (expression := self.expression()) is not None
        ):
            self.show_index(2, 0, 1)
            return Node('expressions', [expression])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def expression(self):
        self.show_rule('expression', [['disjunction', "'if'", 'disjunction', "'else'", 'expression'], ['disjunction'], ['lambdef']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (disjunction := self.disjunction()) is not None
            and self.show_index(0, 1)
            and self.expect('if') is not None
            and self.show_index(0, 2)
            and (disjunction1 := self.disjunction()) is not None
            and self.show_index(0, 3)
            and self.expect('else') is not None
            and self.show_index(0, 4)
            and (expression := self.expression()) is not None
        ):
            self.show_index(0, 0, 5)
            return Node('expression', [disjunction, disjunction1, expression])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (disjunction := self.disjunction()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('expression', [disjunction])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and (lambdef := self.lambdef()) is not None
        ):
            self.show_index(2, 0, 1)
            return Node('expression', [lambdef])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def lambdef(self):
        self.show_rule('lambdef', [["'lambda'", '[lambda_params]', "':'", 'expression']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('lambda') is not None
            and self.show_index(0, 1)
            and ((lambda_params := self.lambda_params()) is not None or True)
            and self.show_index(0, 2)
            and self.expect(':') is not None
            and self.show_index(0, 3)
            and (expression := self.expression()) is not None
        ):
            self.show_index(0, 0, 4)
            return Node('lambdef', [lambda_params, expression])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def lambda_params(self):
        self.show_rule('lambda_params', [['lambda_parameters']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (lambda_parameters := self.lambda_parameters()) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('lambda_params', [lambda_parameters])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def lambda_parameters(self):
        self.show_rule('lambda_parameters', [['lambda_slash_no_default', 'lambda_param_no_default*', 'lambda_param_with_default*', '[lambda_star_etc]'], ['lambda_slash_with_default', 'lambda_param_with_default*', '[lambda_star_etc]'], ['lambda_param_no_default+', 'lambda_param_with_default*', '[lambda_star_etc]'], ['lambda_param_with_default+', '[lambda_star_etc]'], ['lambda_star_etc']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (lambda_slash_no_default := self.lambda_slash_no_default()) is not None
            and self.show_index(0, 1)
            and (lambda_param_no_default := self.loop(False, self.lambda_param_no_default)) is not None
            and self.show_index(0, 2)
            and (lambda_param_with_default := self.loop(False, self.lambda_param_with_default)) is not None
            and self.show_index(0, 3)
            and ((lambda_star_etc := self.lambda_star_etc()) is not None or True)
        ):
            self.show_index(0, 0, 4)
            return Node('lambda_parameters', [lambda_slash_no_default, lambda_param_no_default, lambda_param_with_default, lambda_star_etc])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (lambda_slash_with_default := self.lambda_slash_with_default()) is not None
            and self.show_index(1, 1)
            and (lambda_param_with_default := self.loop(False, self.lambda_param_with_default)) is not None
            and self.show_index(1, 2)
            and ((lambda_star_etc := self.lambda_star_etc()) is not None or True)
        ):
            self.show_index(1, 0, 3)
            return Node('lambda_parameters', [lambda_slash_with_default, lambda_param_with_default, lambda_star_etc])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and (lambda_param_no_default := self.loop(True, self.lambda_param_no_default)) is not None
            and self.show_index(2, 1)
            and (lambda_param_with_default := self.loop(False, self.lambda_param_with_default)) is not None
            and self.show_index(2, 2)
            and ((lambda_star_etc := self.lambda_star_etc()) is not None or True)
        ):
            self.show_index(2, 0, 3)
            return Node('lambda_parameters', [lambda_param_no_default, lambda_param_with_default, lambda_star_etc])
        self.reset(pos)
        if (True
            and self.show_index(3, 0)
            and (lambda_param_with_default := self.loop(True, self.lambda_param_with_default)) is not None
            and self.show_index(3, 1)
            and ((lambda_star_etc := self.lambda_star_etc()) is not None or True)
        ):
            self.show_index(3, 0, 2)
            return Node('lambda_parameters', [lambda_param_with_default, lambda_star_etc])
        self.reset(pos)
        if (True
            and self.show_index(4, 0)
            and (lambda_star_etc := self.lambda_star_etc()) is not None
        ):
            self.show_index(4, 0, 1)
            return Node('lambda_parameters', [lambda_star_etc])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def lambda_slash_no_default(self):
        self.show_rule('lambda_slash_no_default', [['lambda_param_no_default+', "'/'", "','"], ['lambda_param_no_default+', "'/'", "&':'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (lambda_param_no_default := self.loop(True, self.lambda_param_no_default)) is not None
            and self.show_index(0, 1)
            and self.expect('/') is not None
            and self.show_index(0, 2)
            and self.expect(',') is not None
        ):
            self.show_index(0, 0, 3)
            return Node('lambda_slash_no_default', [lambda_param_no_default])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (lambda_param_no_default := self.loop(True, self.lambda_param_no_default)) is not None
            and self.show_index(1, 1)
            and self.expect('/') is not None
            and self.show_index(1, 2)
            and self.lookahead(True, self.expect, ':')
        ):
            self.show_index(1, 0, 3)
            return Node('lambda_slash_no_default', [lambda_param_no_default])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def lambda_slash_with_default(self):
        self.show_rule('lambda_slash_with_default', [['lambda_param_no_default*', 'lambda_param_with_default+', "'/'", "','"], ['lambda_param_no_default*', 'lambda_param_with_default+', "'/'", "&':'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (lambda_param_no_default := self.loop(False, self.lambda_param_no_default)) is not None
            and self.show_index(0, 1)
            and (lambda_param_with_default := self.loop(True, self.lambda_param_with_default)) is not None
            and self.show_index(0, 2)
            and self.expect('/') is not None
            and self.show_index(0, 3)
            and self.expect(',') is not None
        ):
            self.show_index(0, 0, 4)
            return Node('lambda_slash_with_default', [lambda_param_no_default, lambda_param_with_default])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (lambda_param_no_default := self.loop(False, self.lambda_param_no_default)) is not None
            and self.show_index(1, 1)
            and (lambda_param_with_default := self.loop(True, self.lambda_param_with_default)) is not None
            and self.show_index(1, 2)
            and self.expect('/') is not None
            and self.show_index(1, 3)
            and self.lookahead(True, self.expect, ':')
        ):
            self.show_index(1, 0, 4)
            return Node('lambda_slash_with_default', [lambda_param_no_default, lambda_param_with_default])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def lambda_star_etc(self):
        self.show_rule('lambda_star_etc', [["'*'", 'lambda_param_no_default', 'lambda_param_maybe_default*', '[lambda_kwds]'], ["'*'", "','", 'lambda_param_maybe_default+', '[lambda_kwds]'], ['lambda_kwds']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('*') is not None
            and self.show_index(0, 1)
            and (lambda_param_no_default := self.lambda_param_no_default()) is not None
            and self.show_index(0, 2)
            and (lambda_param_maybe_default := self.loop(False, self.lambda_param_maybe_default)) is not None
            and self.show_index(0, 3)
            and ((lambda_kwds := self.lambda_kwds()) is not None or True)
        ):
            self.show_index(0, 0, 4)
            return Node('lambda_star_etc', [lambda_param_no_default, lambda_param_maybe_default, lambda_kwds])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and self.expect('*') is not None
            and self.show_index(1, 1)
            and self.expect(',') is not None
            and self.show_index(1, 2)
            and (lambda_param_maybe_default := self.loop(True, self.lambda_param_maybe_default)) is not None
            and self.show_index(1, 3)
            and ((lambda_kwds := self.lambda_kwds()) is not None or True)
        ):
            self.show_index(1, 0, 4)
            return Node('lambda_star_etc', [lambda_param_maybe_default, lambda_kwds])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and (lambda_kwds := self.lambda_kwds()) is not None
        ):
            self.show_index(2, 0, 1)
            return Node('lambda_star_etc', [lambda_kwds])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def lambda_kwds(self):
        self.show_rule('lambda_kwds', [["'**'", 'lambda_param_no_default']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('**') is not None
            and self.show_index(0, 1)
            and (lambda_param_no_default := self.lambda_param_no_default()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('lambda_kwds', [lambda_param_no_default])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def lambda_param_no_default(self):
        self.show_rule('lambda_param_no_default', [['lambda_param', "','"], ['lambda_param', "&':'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (lambda_param := self.lambda_param()) is not None
            and self.show_index(0, 1)
            and self.expect(',') is not None
        ):
            self.show_index(0, 0, 2)
            return Node('lambda_param_no_default', [lambda_param])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (lambda_param := self.lambda_param()) is not None
            and self.show_index(1, 1)
            and self.lookahead(True, self.expect, ':')
        ):
            self.show_index(1, 0, 2)
            return Node('lambda_param_no_default', [lambda_param])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def lambda_param_with_default(self):
        self.show_rule('lambda_param_with_default', [['lambda_param', 'default', "','"], ['lambda_param', 'default', "&':'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (lambda_param := self.lambda_param()) is not None
            and self.show_index(0, 1)
            and (default := self.default()) is not None
            and self.show_index(0, 2)
            and self.expect(',') is not None
        ):
            self.show_index(0, 0, 3)
            return Node('lambda_param_with_default', [lambda_param, default])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (lambda_param := self.lambda_param()) is not None
            and self.show_index(1, 1)
            and (default := self.default()) is not None
            and self.show_index(1, 2)
            and self.lookahead(True, self.expect, ':')
        ):
            self.show_index(1, 0, 3)
            return Node('lambda_param_with_default', [lambda_param, default])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def lambda_param_maybe_default(self):
        self.show_rule('lambda_param_maybe_default', [['lambda_param', '[default]', "','"], ['lambda_param', '[default]', "&':'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (lambda_param := self.lambda_param()) is not None
            and self.show_index(0, 1)
            and ((default := self.default()) is not None or True)
            and self.show_index(0, 2)
            and self.expect(',') is not None
        ):
            self.show_index(0, 0, 3)
            return Node('lambda_param_maybe_default', [lambda_param, default])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (lambda_param := self.lambda_param()) is not None
            and self.show_index(1, 1)
            and ((default := self.default()) is not None or True)
            and self.show_index(1, 2)
            and self.lookahead(True, self.expect, ':')
        ):
            self.show_index(1, 0, 3)
            return Node('lambda_param_maybe_default', [lambda_param, default])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def lambda_param(self):
        self.show_rule('lambda_param', [['NAME']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (name := self.expect(NAME)) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('lambda_param', [name])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def disjunction(self):
        self.show_rule('disjunction', [['conjunction', '_synthetic_rule_65+'], ['conjunction']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (conjunction := self.conjunction()) is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_65 := self.loop(True, self._synthetic_rule_65)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('disjunction', [conjunction, _synthetic_rule_65])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (conjunction := self.conjunction()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('disjunction', [conjunction])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def conjunction(self):
        self.show_rule('conjunction', [['inversion', '_synthetic_rule_66+'], ['inversion']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (inversion := self.inversion()) is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_66 := self.loop(True, self._synthetic_rule_66)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('conjunction', [inversion, _synthetic_rule_66])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (inversion := self.inversion()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('conjunction', [inversion])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def inversion(self):
        self.show_rule('inversion', [["'not'", 'inversion'], ['comparison']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('not') is not None
            and self.show_index(0, 1)
            and (inversion := self.inversion()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('inversion', [inversion])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (comparison := self.comparison()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('inversion', [comparison])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def comparison(self):
        self.show_rule('comparison', [['bitwise_or', 'compare_op_bitwise_or_pair+'], ['bitwise_or']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (bitwise_or := self.bitwise_or()) is not None
            and self.show_index(0, 1)
            and (compare_op_bitwise_or_pair := self.loop(True, self.compare_op_bitwise_or_pair)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('comparison', [bitwise_or, compare_op_bitwise_or_pair])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (bitwise_or := self.bitwise_or()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('comparison', [bitwise_or])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def compare_op_bitwise_or_pair(self):
        self.show_rule('compare_op_bitwise_or_pair', [['eq_bitwise_or'], ['noteq_bitwise_or'], ['lte_bitwise_or'], ['lt_bitwise_or'], ['gte_bitwise_or'], ['gt_bitwise_or'], ['notin_bitwise_or'], ['in_bitwise_or'], ['isnot_bitwise_or'], ['is_bitwise_or']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (eq_bitwise_or := self.eq_bitwise_or()) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('compare_op_bitwise_or_pair', [eq_bitwise_or])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (noteq_bitwise_or := self.noteq_bitwise_or()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('compare_op_bitwise_or_pair', [noteq_bitwise_or])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and (lte_bitwise_or := self.lte_bitwise_or()) is not None
        ):
            self.show_index(2, 0, 1)
            return Node('compare_op_bitwise_or_pair', [lte_bitwise_or])
        self.reset(pos)
        if (True
            and self.show_index(3, 0)
            and (lt_bitwise_or := self.lt_bitwise_or()) is not None
        ):
            self.show_index(3, 0, 1)
            return Node('compare_op_bitwise_or_pair', [lt_bitwise_or])
        self.reset(pos)
        if (True
            and self.show_index(4, 0)
            and (gte_bitwise_or := self.gte_bitwise_or()) is not None
        ):
            self.show_index(4, 0, 1)
            return Node('compare_op_bitwise_or_pair', [gte_bitwise_or])
        self.reset(pos)
        if (True
            and self.show_index(5, 0)
            and (gt_bitwise_or := self.gt_bitwise_or()) is not None
        ):
            self.show_index(5, 0, 1)
            return Node('compare_op_bitwise_or_pair', [gt_bitwise_or])
        self.reset(pos)
        if (True
            and self.show_index(6, 0)
            and (notin_bitwise_or := self.notin_bitwise_or()) is not None
        ):
            self.show_index(6, 0, 1)
            return Node('compare_op_bitwise_or_pair', [notin_bitwise_or])
        self.reset(pos)
        if (True
            and self.show_index(7, 0)
            and (in_bitwise_or := self.in_bitwise_or()) is not None
        ):
            self.show_index(7, 0, 1)
            return Node('compare_op_bitwise_or_pair', [in_bitwise_or])
        self.reset(pos)
        if (True
            and self.show_index(8, 0)
            and (isnot_bitwise_or := self.isnot_bitwise_or()) is not None
        ):
            self.show_index(8, 0, 1)
            return Node('compare_op_bitwise_or_pair', [isnot_bitwise_or])
        self.reset(pos)
        if (True
            and self.show_index(9, 0)
            and (is_bitwise_or := self.is_bitwise_or()) is not None
        ):
            self.show_index(9, 0, 1)
            return Node('compare_op_bitwise_or_pair', [is_bitwise_or])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def eq_bitwise_or(self):
        self.show_rule('eq_bitwise_or', [["'=='", 'bitwise_or']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('==') is not None
            and self.show_index(0, 1)
            and (bitwise_or := self.bitwise_or()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('eq_bitwise_or', [bitwise_or])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def noteq_bitwise_or(self):
        self.show_rule('noteq_bitwise_or', [["'!='", 'bitwise_or']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('!=') is not None
            and self.show_index(0, 1)
            and (bitwise_or := self.bitwise_or()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('noteq_bitwise_or', [bitwise_or])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def lte_bitwise_or(self):
        self.show_rule('lte_bitwise_or', [["'<='", 'bitwise_or']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('<=') is not None
            and self.show_index(0, 1)
            and (bitwise_or := self.bitwise_or()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('lte_bitwise_or', [bitwise_or])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def lt_bitwise_or(self):
        self.show_rule('lt_bitwise_or', [["'<'", 'bitwise_or']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('<') is not None
            and self.show_index(0, 1)
            and (bitwise_or := self.bitwise_or()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('lt_bitwise_or', [bitwise_or])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def gte_bitwise_or(self):
        self.show_rule('gte_bitwise_or', [["'>='", 'bitwise_or']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('>=') is not None
            and self.show_index(0, 1)
            and (bitwise_or := self.bitwise_or()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('gte_bitwise_or', [bitwise_or])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def gt_bitwise_or(self):
        self.show_rule('gt_bitwise_or', [["'>'", 'bitwise_or']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('>') is not None
            and self.show_index(0, 1)
            and (bitwise_or := self.bitwise_or()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('gt_bitwise_or', [bitwise_or])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def notin_bitwise_or(self):
        self.show_rule('notin_bitwise_or', [["'not'", "'in'", 'bitwise_or']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('not') is not None
            and self.show_index(0, 1)
            and self.expect('in') is not None
            and self.show_index(0, 2)
            and (bitwise_or := self.bitwise_or()) is not None
        ):
            self.show_index(0, 0, 3)
            return Node('notin_bitwise_or', [bitwise_or])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def in_bitwise_or(self):
        self.show_rule('in_bitwise_or', [["'in'", 'bitwise_or']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('in') is not None
            and self.show_index(0, 1)
            and (bitwise_or := self.bitwise_or()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('in_bitwise_or', [bitwise_or])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def isnot_bitwise_or(self):
        self.show_rule('isnot_bitwise_or', [["'is'", "'not'", 'bitwise_or']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('is') is not None
            and self.show_index(0, 1)
            and self.expect('not') is not None
            and self.show_index(0, 2)
            and (bitwise_or := self.bitwise_or()) is not None
        ):
            self.show_index(0, 0, 3)
            return Node('isnot_bitwise_or', [bitwise_or])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def is_bitwise_or(self):
        self.show_rule('is_bitwise_or', [["'is'", 'bitwise_or']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('is') is not None
            and self.show_index(0, 1)
            and (bitwise_or := self.bitwise_or()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('is_bitwise_or', [bitwise_or])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize_left_rec
    def bitwise_or(self):
        self.show_rule('*' + 'bitwise_or', [['bitwise_or', "'|'", 'bitwise_xor'], ['bitwise_xor']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (bitwise_or := self.bitwise_or()) is not None
            and self.show_index(0, 1)
            and self.expect('|') is not None
            and self.show_index(0, 2)
            and (bitwise_xor := self.bitwise_xor()) is not None
        ):
            self.show_index(0, 0, 3)
            return Node('bitwise_or', [bitwise_or, bitwise_xor])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (bitwise_xor := self.bitwise_xor()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('bitwise_or', [bitwise_xor])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize_left_rec
    def bitwise_xor(self):
        self.show_rule('*' + 'bitwise_xor', [['bitwise_xor', "'^'", 'bitwise_and'], ['bitwise_and']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (bitwise_xor := self.bitwise_xor()) is not None
            and self.show_index(0, 1)
            and self.expect('^') is not None
            and self.show_index(0, 2)
            and (bitwise_and := self.bitwise_and()) is not None
        ):
            self.show_index(0, 0, 3)
            return Node('bitwise_xor', [bitwise_xor, bitwise_and])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (bitwise_and := self.bitwise_and()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('bitwise_xor', [bitwise_and])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize_left_rec
    def bitwise_and(self):
        self.show_rule('*' + 'bitwise_and', [['bitwise_and', "'&'", 'shift_expr'], ['shift_expr']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (bitwise_and := self.bitwise_and()) is not None
            and self.show_index(0, 1)
            and self.expect('&') is not None
            and self.show_index(0, 2)
            and (shift_expr := self.shift_expr()) is not None
        ):
            self.show_index(0, 0, 3)
            return Node('bitwise_and', [bitwise_and, shift_expr])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (shift_expr := self.shift_expr()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('bitwise_and', [shift_expr])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize_left_rec
    def shift_expr(self):
        self.show_rule('*' + 'shift_expr', [['shift_expr', "'<<'", 'sum'], ['shift_expr', "'>>'", 'sum'], ['sum']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (shift_expr := self.shift_expr()) is not None
            and self.show_index(0, 1)
            and self.expect('<<') is not None
            and self.show_index(0, 2)
            and (sum := self.sum()) is not None
        ):
            self.show_index(0, 0, 3)
            return Node('shift_expr', [shift_expr, sum])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (shift_expr := self.shift_expr()) is not None
            and self.show_index(1, 1)
            and self.expect('>>') is not None
            and self.show_index(1, 2)
            and (sum := self.sum()) is not None
        ):
            self.show_index(1, 0, 3)
            return Node('shift_expr', [shift_expr, sum])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and (sum := self.sum()) is not None
        ):
            self.show_index(2, 0, 1)
            return Node('shift_expr', [sum])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize_left_rec
    def sum(self):
        self.show_rule('*' + 'sum', [['sum', "'+'", 'term'], ['sum', "'-'", 'term'], ['term']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (sum := self.sum()) is not None
            and self.show_index(0, 1)
            and self.expect('+') is not None
            and self.show_index(0, 2)
            and (term := self.term()) is not None
        ):
            self.show_index(0, 0, 3)
            return Node('sum', [sum, term])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (sum := self.sum()) is not None
            and self.show_index(1, 1)
            and self.expect('-') is not None
            and self.show_index(1, 2)
            and (term := self.term()) is not None
        ):
            self.show_index(1, 0, 3)
            return Node('sum', [sum, term])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and (term := self.term()) is not None
        ):
            self.show_index(2, 0, 1)
            return Node('sum', [term])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize_left_rec
    def term(self):
        self.show_rule('*' + 'term', [['term', "'*'", 'factor'], ['term', "'/'", 'factor'], ['term', "'//'", 'factor'], ['term', "'%'", 'factor'], ['term', "'@'", 'factor'], ['factor']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (term := self.term()) is not None
            and self.show_index(0, 1)
            and self.expect('*') is not None
            and self.show_index(0, 2)
            and (factor := self.factor()) is not None
        ):
            self.show_index(0, 0, 3)
            return Node('term', [term, factor])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (term := self.term()) is not None
            and self.show_index(1, 1)
            and self.expect('/') is not None
            and self.show_index(1, 2)
            and (factor := self.factor()) is not None
        ):
            self.show_index(1, 0, 3)
            return Node('term', [term, factor])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and (term := self.term()) is not None
            and self.show_index(2, 1)
            and self.expect('//') is not None
            and self.show_index(2, 2)
            and (factor := self.factor()) is not None
        ):
            self.show_index(2, 0, 3)
            return Node('term', [term, factor])
        self.reset(pos)
        if (True
            and self.show_index(3, 0)
            and (term := self.term()) is not None
            and self.show_index(3, 1)
            and self.expect('%') is not None
            and self.show_index(3, 2)
            and (factor := self.factor()) is not None
        ):
            self.show_index(3, 0, 3)
            return Node('term', [term, factor])
        self.reset(pos)
        if (True
            and self.show_index(4, 0)
            and (term := self.term()) is not None
            and self.show_index(4, 1)
            and self.expect('@') is not None
            and self.show_index(4, 2)
            and (factor := self.factor()) is not None
        ):
            self.show_index(4, 0, 3)
            return Node('term', [term, factor])
        self.reset(pos)
        if (True
            and self.show_index(5, 0)
            and (factor := self.factor()) is not None
        ):
            self.show_index(5, 0, 1)
            return Node('term', [factor])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def factor(self):
        self.show_rule('factor', [["'+'", 'factor'], ["'-'", 'factor'], ["'~'", 'factor'], ['power']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('+') is not None
            and self.show_index(0, 1)
            and (factor := self.factor()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('factor', [factor])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and self.expect('-') is not None
            and self.show_index(1, 1)
            and (factor := self.factor()) is not None
        ):
            self.show_index(1, 0, 2)
            return Node('factor', [factor])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and self.expect('~') is not None
            and self.show_index(2, 1)
            and (factor := self.factor()) is not None
        ):
            self.show_index(2, 0, 2)
            return Node('factor', [factor])
        self.reset(pos)
        if (True
            and self.show_index(3, 0)
            and (power := self.power()) is not None
        ):
            self.show_index(3, 0, 1)
            return Node('factor', [power])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def power(self):
        self.show_rule('power', [['await_var_primary', "'**'", 'factor'], ['await_var_primary']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (await_var_primary := self.await_var_primary()) is not None
            and self.show_index(0, 1)
            and self.expect('**') is not None
            and self.show_index(0, 2)
            and (factor := self.factor()) is not None
        ):
            self.show_index(0, 0, 3)
            return Node('power', [await_var_primary, factor])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (await_var_primary := self.await_var_primary()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('power', [await_var_primary])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def await_var_primary(self):
        self.show_rule('await_var_primary', [['AWAIT', 'primary'], ['primary']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (await_var := self.expect(AWAIT)) is not None
            and self.show_index(0, 1)
            and (primary := self.primary()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('await_var_primary', [await_var, primary])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (primary := self.primary()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('await_var_primary', [primary])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize_left_rec
    def primary(self):
        self.show_rule('*' + 'primary', [['primary', "'.'", 'NAME'], ['primary', 'genexp'], ['primary', "'('", '[arguments]', "')'"], ['primary', "'['", 'slices', "']'"], ['atom']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (primary := self.primary()) is not None
            and self.show_index(0, 1)
            and self.expect('.') is not None
            and self.show_index(0, 2)
            and (name := self.expect(NAME)) is not None
        ):
            self.show_index(0, 0, 3)
            return Node('primary', [primary, name])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (primary := self.primary()) is not None
            and self.show_index(1, 1)
            and (genexp := self.genexp()) is not None
        ):
            self.show_index(1, 0, 2)
            return Node('primary', [primary, genexp])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and (primary := self.primary()) is not None
            and self.show_index(2, 1)
            and self.expect('(') is not None
            and self.show_index(2, 2)
            and ((arguments := self.arguments()) is not None or True)
            and self.show_index(2, 3)
            and self.expect(')') is not None
        ):
            self.show_index(2, 0, 4)
            return Node('primary', [primary, arguments])
        self.reset(pos)
        if (True
            and self.show_index(3, 0)
            and (primary := self.primary()) is not None
            and self.show_index(3, 1)
            and self.expect('[') is not None
            and self.show_index(3, 2)
            and (slices := self.slices()) is not None
            and self.show_index(3, 3)
            and self.expect(']') is not None
        ):
            self.show_index(3, 0, 4)
            return Node('primary', [primary, slices])
        self.reset(pos)
        if (True
            and self.show_index(4, 0)
            and (atom := self.atom()) is not None
        ):
            self.show_index(4, 0, 1)
            return Node('primary', [atom])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def slices(self):
        self.show_rule('slices', [['slice', "!','"], ['_synthetic_rule_68', "[',']"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (slice := self.slice()) is not None
            and self.show_index(0, 1)
            and self.lookahead(False, self.expect, ',')
        ):
            self.show_index(0, 0, 2)
            return Node('slices', [slice])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (_synthetic_rule_68 := self._synthetic_rule_68()) is not None
            and self.show_index(1, 1)
            and (self.expect(',') is not None or True)
        ):
            self.show_index(1, 0, 2)
            return Node('slices', [_synthetic_rule_68])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def slice(self):
        self.show_rule('slice', [['[expression]', "':'", '[expression]', '[_synthetic_rule_69]'], ['named_expression']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and ((expression := self.expression()) is not None or True)
            and self.show_index(0, 1)
            and self.expect(':') is not None
            and self.show_index(0, 2)
            and ((expression1 := self.expression()) is not None or True)
            and self.show_index(0, 3)
            and ((_synthetic_rule_69 := self._synthetic_rule_69()) is not None or True)
        ):
            self.show_index(0, 0, 4)
            return Node('slice', [expression, expression1, _synthetic_rule_69])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (named_expression := self.named_expression()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('slice', [named_expression])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def atom(self):
        self.show_rule('atom', [['NAME'], ["'True'"], ["'False'"], ["'None'"], ['strings'], ['NUMBER'], ['_synthetic_rule_70'], ['_synthetic_rule_71'], ['_synthetic_rule_72'], ["'...'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (name := self.expect(NAME)) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('atom', [name])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and self.expect('True') is not None
        ):
            self.show_index(1, 0, 1)
            return Node('atom', [])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and self.expect('False') is not None
        ):
            self.show_index(2, 0, 1)
            return Node('atom', [])
        self.reset(pos)
        if (True
            and self.show_index(3, 0)
            and self.expect('None') is not None
        ):
            self.show_index(3, 0, 1)
            return Node('atom', [])
        self.reset(pos)
        if (True
            and self.show_index(4, 0)
            and (strings := self.strings()) is not None
        ):
            self.show_index(4, 0, 1)
            return Node('atom', [strings])
        self.reset(pos)
        if (True
            and self.show_index(5, 0)
            and (number := self.expect(NUMBER)) is not None
        ):
            self.show_index(5, 0, 1)
            return Node('atom', [number])
        self.reset(pos)
        if (True
            and self.show_index(6, 0)
            and (_synthetic_rule_70 := self._synthetic_rule_70()) is not None
        ):
            self.show_index(6, 0, 1)
            return Node('atom', [_synthetic_rule_70])
        self.reset(pos)
        if (True
            and self.show_index(7, 0)
            and (_synthetic_rule_71 := self._synthetic_rule_71()) is not None
        ):
            self.show_index(7, 0, 1)
            return Node('atom', [_synthetic_rule_71])
        self.reset(pos)
        if (True
            and self.show_index(8, 0)
            and (_synthetic_rule_72 := self._synthetic_rule_72()) is not None
        ):
            self.show_index(8, 0, 1)
            return Node('atom', [_synthetic_rule_72])
        self.reset(pos)
        if (True
            and self.show_index(9, 0)
            and self.expect('...') is not None
        ):
            self.show_index(9, 0, 1)
            return Node('atom', [])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def strings(self):
        self.show_rule('strings', [['STRING+']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (string := self.loop(True, self.expect, STRING)) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('strings', [string])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def list(self):
        self.show_rule('list', [["'['", '[star_named_expressions]', "']'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('[') is not None
            and self.show_index(0, 1)
            and ((star_named_expressions := self.star_named_expressions()) is not None or True)
            and self.show_index(0, 2)
            and self.expect(']') is not None
        ):
            self.show_index(0, 0, 3)
            return Node('list', [star_named_expressions])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def listcomp(self):
        self.show_rule('listcomp', [["'['", 'named_expression', 'for_if_clauses', "']'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('[') is not None
            and self.show_index(0, 1)
            and (named_expression := self.named_expression()) is not None
            and self.show_index(0, 2)
            and (for_if_clauses := self.for_if_clauses()) is not None
            and self.show_index(0, 3)
            and self.expect(']') is not None
        ):
            self.show_index(0, 0, 4)
            return Node('listcomp', [named_expression, for_if_clauses])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def tuple(self):
        self.show_rule('tuple', [["'('", '[_synthetic_rule_73]', "')'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('(') is not None
            and self.show_index(0, 1)
            and ((_synthetic_rule_73 := self._synthetic_rule_73()) is not None or True)
            and self.show_index(0, 2)
            and self.expect(')') is not None
        ):
            self.show_index(0, 0, 3)
            return Node('tuple', [_synthetic_rule_73])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def group(self):
        self.show_rule('group', [["'('", '_synthetic_rule_74', "')'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('(') is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_74 := self._synthetic_rule_74()) is not None
            and self.show_index(0, 2)
            and self.expect(')') is not None
        ):
            self.show_index(0, 0, 3)
            return Node('group', [_synthetic_rule_74])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def genexp(self):
        self.show_rule('genexp', [["'('", '_synthetic_rule_75', 'for_if_clauses', "')'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('(') is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_75 := self._synthetic_rule_75()) is not None
            and self.show_index(0, 2)
            and (for_if_clauses := self.for_if_clauses()) is not None
            and self.show_index(0, 3)
            and self.expect(')') is not None
        ):
            self.show_index(0, 0, 4)
            return Node('genexp', [_synthetic_rule_75, for_if_clauses])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def set(self):
        self.show_rule('set', [["'{'", 'star_named_expressions', "'}'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('{') is not None
            and self.show_index(0, 1)
            and (star_named_expressions := self.star_named_expressions()) is not None
            and self.show_index(0, 2)
            and self.expect('}') is not None
        ):
            self.show_index(0, 0, 3)
            return Node('set', [star_named_expressions])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def setcomp(self):
        self.show_rule('setcomp', [["'{'", 'named_expression', 'for_if_clauses', "'}'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('{') is not None
            and self.show_index(0, 1)
            and (named_expression := self.named_expression()) is not None
            and self.show_index(0, 2)
            and (for_if_clauses := self.for_if_clauses()) is not None
            and self.show_index(0, 3)
            and self.expect('}') is not None
        ):
            self.show_index(0, 0, 4)
            return Node('setcomp', [named_expression, for_if_clauses])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def dict(self):
        self.show_rule('dict', [["'{'", '[double_starred_kvpairs]', "'}'"], ["'{'", 'invalid_double_starred_kvpairs', "'}'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('{') is not None
            and self.show_index(0, 1)
            and ((double_starred_kvpairs := self.double_starred_kvpairs()) is not None or True)
            and self.show_index(0, 2)
            and self.expect('}') is not None
        ):
            self.show_index(0, 0, 3)
            return Node('dict', [double_starred_kvpairs])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and self.expect('{') is not None
            and self.show_index(1, 1)
            and (invalid_double_starred_kvpairs := self.invalid_double_starred_kvpairs()) is not None
            and self.show_index(1, 2)
            and self.expect('}') is not None
        ):
            self.show_index(1, 0, 3)
            return Node('dict', [invalid_double_starred_kvpairs])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def dictcomp(self):
        self.show_rule('dictcomp', [["'{'", 'kvpair', 'for_if_clauses', "'}'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('{') is not None
            and self.show_index(0, 1)
            and (kvpair := self.kvpair()) is not None
            and self.show_index(0, 2)
            and (for_if_clauses := self.for_if_clauses()) is not None
            and self.show_index(0, 3)
            and self.expect('}') is not None
        ):
            self.show_index(0, 0, 4)
            return Node('dictcomp', [kvpair, for_if_clauses])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def double_starred_kvpairs(self):
        self.show_rule('double_starred_kvpairs', [['_synthetic_rule_77', "[',']"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (_synthetic_rule_77 := self._synthetic_rule_77()) is not None
            and self.show_index(0, 1)
            and (self.expect(',') is not None or True)
        ):
            self.show_index(0, 0, 2)
            return Node('double_starred_kvpairs', [_synthetic_rule_77])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def double_starred_kvpair(self):
        self.show_rule('double_starred_kvpair', [["'**'", 'bitwise_or'], ['kvpair']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('**') is not None
            and self.show_index(0, 1)
            and (bitwise_or := self.bitwise_or()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('double_starred_kvpair', [bitwise_or])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (kvpair := self.kvpair()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('double_starred_kvpair', [kvpair])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def kvpair(self):
        self.show_rule('kvpair', [['expression', "':'", 'expression']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (expression := self.expression()) is not None
            and self.show_index(0, 1)
            and self.expect(':') is not None
            and self.show_index(0, 2)
            and (expression1 := self.expression()) is not None
        ):
            self.show_index(0, 0, 3)
            return Node('kvpair', [expression, expression1])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def for_if_clauses(self):
        self.show_rule('for_if_clauses', [['for_if_clause+']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (for_if_clause := self.loop(True, self.for_if_clause)) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('for_if_clauses', [for_if_clause])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def for_if_clause(self):
        self.show_rule('for_if_clause', [['ASYNC', "'for'", 'star_targets', "'in'", '~', 'disjunction', '_synthetic_rule_78*'], ["'for'", 'star_targets', "'in'", '~', 'disjunction', '_synthetic_rule_79*']])
        pos = self.mark()
        cut = False
        if (True
            and self.show_index(0, 0)
            and (async_var := self.expect(ASYNC)) is not None
            and self.show_index(0, 1)
            and self.expect('for') is not None
            and self.show_index(0, 2)
            and (star_targets := self.star_targets()) is not None
            and self.show_index(0, 3)
            and self.expect('in') is not None
            and self.show_index(0, 4)
            and True
            and self.show_index(0, 5)
            and (disjunction := self.disjunction()) is not None
            and self.show_index(0, 6)
            and (_synthetic_rule_78 := self.loop(False, self._synthetic_rule_78)) is not None
        ):
            self.show_index(0, 0, 7)
            return Node('for_if_clause', [async_var, star_targets, disjunction, _synthetic_rule_78])
        self.reset(pos)
        if cut:
            self.show_index(0, 0, 0)
            return None
        if (True
            and self.show_index(1, 0)
            and self.expect('for') is not None
            and self.show_index(1, 1)
            and (star_targets := self.star_targets()) is not None
            and self.show_index(1, 2)
            and self.expect('in') is not None
            and self.show_index(1, 3)
            and True
            and self.show_index(1, 4)
            and (disjunction := self.disjunction()) is not None
            and self.show_index(1, 5)
            and (_synthetic_rule_79 := self.loop(False, self._synthetic_rule_79)) is not None
        ):
            self.show_index(1, 0, 6)
            return Node('for_if_clause', [star_targets, disjunction, _synthetic_rule_79])
        self.reset(pos)
        if cut:
            self.show_index(0, 0, 0)
            return None
        self.show_index(0, 0, 0)
        return None

    @memoize
    def yield_expr(self):
        self.show_rule('yield_expr', [["'yield'", "'from'", 'expression'], ["'yield'", '[star_expressions]']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('yield') is not None
            and self.show_index(0, 1)
            and self.expect('from') is not None
            and self.show_index(0, 2)
            and (expression := self.expression()) is not None
        ):
            self.show_index(0, 0, 3)
            return Node('yield_expr', [expression])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and self.expect('yield') is not None
            and self.show_index(1, 1)
            and ((star_expressions := self.star_expressions()) is not None or True)
        ):
            self.show_index(1, 0, 2)
            return Node('yield_expr', [star_expressions])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def arguments(self):
        self.show_rule('arguments', [['args', "[',']", "&')'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (args := self.args()) is not None
            and self.show_index(0, 1)
            and (self.expect(',') is not None or True)
            and self.show_index(0, 2)
            and self.lookahead(True, self.expect, ')')
        ):
            self.show_index(0, 0, 3)
            return Node('arguments', [args])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def args(self):
        self.show_rule('args', [['_synthetic_rule_83', '[_synthetic_rule_84]'], ['kwargs']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (_synthetic_rule_83 := self._synthetic_rule_83()) is not None
            and self.show_index(0, 1)
            and ((_synthetic_rule_84 := self._synthetic_rule_84()) is not None or True)
        ):
            self.show_index(0, 0, 2)
            return Node('args', [_synthetic_rule_83, _synthetic_rule_84])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (kwargs := self.kwargs()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('args', [kwargs])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def kwargs(self):
        self.show_rule('kwargs', [['_synthetic_rule_86', "','", '_synthetic_rule_88'], ['_synthetic_rule_90'], ['_synthetic_rule_92']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (_synthetic_rule_86 := self._synthetic_rule_86()) is not None
            and self.show_index(0, 1)
            and self.expect(',') is not None
            and self.show_index(0, 2)
            and (_synthetic_rule_88 := self._synthetic_rule_88()) is not None
        ):
            self.show_index(0, 0, 3)
            return Node('kwargs', [_synthetic_rule_86, _synthetic_rule_88])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (_synthetic_rule_90 := self._synthetic_rule_90()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('kwargs', [_synthetic_rule_90])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and (_synthetic_rule_92 := self._synthetic_rule_92()) is not None
        ):
            self.show_index(2, 0, 1)
            return Node('kwargs', [_synthetic_rule_92])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def starred_expression(self):
        self.show_rule('starred_expression', [["'*'", 'expression']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('*') is not None
            and self.show_index(0, 1)
            and (expression := self.expression()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('starred_expression', [expression])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def kwarg_or_starred(self):
        self.show_rule('kwarg_or_starred', [['NAME', "'='", 'expression'], ['starred_expression']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (name := self.expect(NAME)) is not None
            and self.show_index(0, 1)
            and self.expect('=') is not None
            and self.show_index(0, 2)
            and (expression := self.expression()) is not None
        ):
            self.show_index(0, 0, 3)
            return Node('kwarg_or_starred', [name, expression])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (starred_expression := self.starred_expression()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('kwarg_or_starred', [starred_expression])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def kwarg_or_double_starred(self):
        self.show_rule('kwarg_or_double_starred', [['NAME', "'='", 'expression'], ["'**'", 'expression']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (name := self.expect(NAME)) is not None
            and self.show_index(0, 1)
            and self.expect('=') is not None
            and self.show_index(0, 2)
            and (expression := self.expression()) is not None
        ):
            self.show_index(0, 0, 3)
            return Node('kwarg_or_double_starred', [name, expression])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and self.expect('**') is not None
            and self.show_index(1, 1)
            and (expression := self.expression()) is not None
        ):
            self.show_index(1, 0, 2)
            return Node('kwarg_or_double_starred', [expression])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def star_targets(self):
        self.show_rule('star_targets', [['star_target', "!','"], ['star_target', '_synthetic_rule_93*', "[',']"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (star_target := self.star_target()) is not None
            and self.show_index(0, 1)
            and self.lookahead(False, self.expect, ',')
        ):
            self.show_index(0, 0, 2)
            return Node('star_targets', [star_target])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (star_target := self.star_target()) is not None
            and self.show_index(1, 1)
            and (_synthetic_rule_93 := self.loop(False, self._synthetic_rule_93)) is not None
            and self.show_index(1, 2)
            and (self.expect(',') is not None or True)
        ):
            self.show_index(1, 0, 3)
            return Node('star_targets', [star_target, _synthetic_rule_93])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def star_targets_list_seq(self):
        self.show_rule('star_targets_list_seq', [['_synthetic_rule_95', "[',']"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (_synthetic_rule_95 := self._synthetic_rule_95()) is not None
            and self.show_index(0, 1)
            and (self.expect(',') is not None or True)
        ):
            self.show_index(0, 0, 2)
            return Node('star_targets_list_seq', [_synthetic_rule_95])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def star_targets_tuple_seq(self):
        self.show_rule('star_targets_tuple_seq', [['star_target', '_synthetic_rule_96+', "[',']"], ['star_target', "','"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (star_target := self.star_target()) is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_96 := self.loop(True, self._synthetic_rule_96)) is not None
            and self.show_index(0, 2)
            and (self.expect(',') is not None or True)
        ):
            self.show_index(0, 0, 3)
            return Node('star_targets_tuple_seq', [star_target, _synthetic_rule_96])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (star_target := self.star_target()) is not None
            and self.show_index(1, 1)
            and self.expect(',') is not None
        ):
            self.show_index(1, 0, 2)
            return Node('star_targets_tuple_seq', [star_target])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def star_target(self):
        self.show_rule('star_target', [["'*'", '_synthetic_rule_97'], ['target_with_star_atom']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('*') is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_97 := self._synthetic_rule_97()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('star_target', [_synthetic_rule_97])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (target_with_star_atom := self.target_with_star_atom()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('star_target', [target_with_star_atom])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def target_with_star_atom(self):
        self.show_rule('target_with_star_atom', [['t_primary', "'.'", 'NAME', '!t_lookahead'], ['t_primary', "'['", 'slices', "']'", '!t_lookahead'], ['star_atom']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (t_primary := self.t_primary()) is not None
            and self.show_index(0, 1)
            and self.expect('.') is not None
            and self.show_index(0, 2)
            and (name := self.expect(NAME)) is not None
            and self.show_index(0, 3)
            and self.lookahead(False, self.t_lookahead)
        ):
            self.show_index(0, 0, 4)
            return Node('target_with_star_atom', [t_primary, name])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (t_primary := self.t_primary()) is not None
            and self.show_index(1, 1)
            and self.expect('[') is not None
            and self.show_index(1, 2)
            and (slices := self.slices()) is not None
            and self.show_index(1, 3)
            and self.expect(']') is not None
            and self.show_index(1, 4)
            and self.lookahead(False, self.t_lookahead)
        ):
            self.show_index(1, 0, 5)
            return Node('target_with_star_atom', [t_primary, slices])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and (star_atom := self.star_atom()) is not None
        ):
            self.show_index(2, 0, 1)
            return Node('target_with_star_atom', [star_atom])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def star_atom(self):
        self.show_rule('star_atom', [['NAME'], ["'('", 'target_with_star_atom', "')'"], ["'('", '[star_targets_tuple_seq]', "')'"], ["'['", '[star_targets_list_seq]', "']'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (name := self.expect(NAME)) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('star_atom', [name])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and self.expect('(') is not None
            and self.show_index(1, 1)
            and (target_with_star_atom := self.target_with_star_atom()) is not None
            and self.show_index(1, 2)
            and self.expect(')') is not None
        ):
            self.show_index(1, 0, 3)
            return Node('star_atom', [target_with_star_atom])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and self.expect('(') is not None
            and self.show_index(2, 1)
            and ((star_targets_tuple_seq := self.star_targets_tuple_seq()) is not None or True)
            and self.show_index(2, 2)
            and self.expect(')') is not None
        ):
            self.show_index(2, 0, 3)
            return Node('star_atom', [star_targets_tuple_seq])
        self.reset(pos)
        if (True
            and self.show_index(3, 0)
            and self.expect('[') is not None
            and self.show_index(3, 1)
            and ((star_targets_list_seq := self.star_targets_list_seq()) is not None or True)
            and self.show_index(3, 2)
            and self.expect(']') is not None
        ):
            self.show_index(3, 0, 3)
            return Node('star_atom', [star_targets_list_seq])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def single_target(self):
        self.show_rule('single_target', [['single_subscript_attribute_target'], ['NAME'], ["'('", 'single_target', "')'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (single_subscript_attribute_target := self.single_subscript_attribute_target()) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('single_target', [single_subscript_attribute_target])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (name := self.expect(NAME)) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('single_target', [name])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and self.expect('(') is not None
            and self.show_index(2, 1)
            and (single_target := self.single_target()) is not None
            and self.show_index(2, 2)
            and self.expect(')') is not None
        ):
            self.show_index(2, 0, 3)
            return Node('single_target', [single_target])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def single_subscript_attribute_target(self):
        self.show_rule('single_subscript_attribute_target', [['t_primary', "'.'", 'NAME', '!t_lookahead'], ['t_primary', "'['", 'slices', "']'", '!t_lookahead']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (t_primary := self.t_primary()) is not None
            and self.show_index(0, 1)
            and self.expect('.') is not None
            and self.show_index(0, 2)
            and (name := self.expect(NAME)) is not None
            and self.show_index(0, 3)
            and self.lookahead(False, self.t_lookahead)
        ):
            self.show_index(0, 0, 4)
            return Node('single_subscript_attribute_target', [t_primary, name])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (t_primary := self.t_primary()) is not None
            and self.show_index(1, 1)
            and self.expect('[') is not None
            and self.show_index(1, 2)
            and (slices := self.slices()) is not None
            and self.show_index(1, 3)
            and self.expect(']') is not None
            and self.show_index(1, 4)
            and self.lookahead(False, self.t_lookahead)
        ):
            self.show_index(1, 0, 5)
            return Node('single_subscript_attribute_target', [t_primary, slices])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def del_targets(self):
        self.show_rule('del_targets', [['_synthetic_rule_99', "[',']"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (_synthetic_rule_99 := self._synthetic_rule_99()) is not None
            and self.show_index(0, 1)
            and (self.expect(',') is not None or True)
        ):
            self.show_index(0, 0, 2)
            return Node('del_targets', [_synthetic_rule_99])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def del_target(self):
        self.show_rule('del_target', [['t_primary', "'.'", 'NAME', '!t_lookahead'], ['t_primary', "'['", 'slices', "']'", '!t_lookahead'], ['del_t_atom']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (t_primary := self.t_primary()) is not None
            and self.show_index(0, 1)
            and self.expect('.') is not None
            and self.show_index(0, 2)
            and (name := self.expect(NAME)) is not None
            and self.show_index(0, 3)
            and self.lookahead(False, self.t_lookahead)
        ):
            self.show_index(0, 0, 4)
            return Node('del_target', [t_primary, name])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (t_primary := self.t_primary()) is not None
            and self.show_index(1, 1)
            and self.expect('[') is not None
            and self.show_index(1, 2)
            and (slices := self.slices()) is not None
            and self.show_index(1, 3)
            and self.expect(']') is not None
            and self.show_index(1, 4)
            and self.lookahead(False, self.t_lookahead)
        ):
            self.show_index(1, 0, 5)
            return Node('del_target', [t_primary, slices])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and (del_t_atom := self.del_t_atom()) is not None
        ):
            self.show_index(2, 0, 1)
            return Node('del_target', [del_t_atom])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def del_t_atom(self):
        self.show_rule('del_t_atom', [['NAME'], ["'('", 'del_target', "')'"], ["'('", '[del_targets]', "')'"], ["'['", '[del_targets]', "']'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (name := self.expect(NAME)) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('del_t_atom', [name])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and self.expect('(') is not None
            and self.show_index(1, 1)
            and (del_target := self.del_target()) is not None
            and self.show_index(1, 2)
            and self.expect(')') is not None
        ):
            self.show_index(1, 0, 3)
            return Node('del_t_atom', [del_target])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and self.expect('(') is not None
            and self.show_index(2, 1)
            and ((del_targets := self.del_targets()) is not None or True)
            and self.show_index(2, 2)
            and self.expect(')') is not None
        ):
            self.show_index(2, 0, 3)
            return Node('del_t_atom', [del_targets])
        self.reset(pos)
        if (True
            and self.show_index(3, 0)
            and self.expect('[') is not None
            and self.show_index(3, 1)
            and ((del_targets := self.del_targets()) is not None or True)
            and self.show_index(3, 2)
            and self.expect(']') is not None
        ):
            self.show_index(3, 0, 3)
            return Node('del_t_atom', [del_targets])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize_left_rec
    def t_primary(self):
        self.show_rule('*' + 't_primary', [['t_primary', "'.'", 'NAME', '&t_lookahead'], ['t_primary', "'['", 'slices', "']'", '&t_lookahead'], ['t_primary', 'genexp', '&t_lookahead'], ['t_primary', "'('", '[arguments]', "')'", '&t_lookahead'], ['atom', '&t_lookahead']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (t_primary := self.t_primary()) is not None
            and self.show_index(0, 1)
            and self.expect('.') is not None
            and self.show_index(0, 2)
            and (name := self.expect(NAME)) is not None
            and self.show_index(0, 3)
            and self.lookahead(True, self.t_lookahead)
        ):
            self.show_index(0, 0, 4)
            return Node('t_primary', [t_primary, name])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (t_primary := self.t_primary()) is not None
            and self.show_index(1, 1)
            and self.expect('[') is not None
            and self.show_index(1, 2)
            and (slices := self.slices()) is not None
            and self.show_index(1, 3)
            and self.expect(']') is not None
            and self.show_index(1, 4)
            and self.lookahead(True, self.t_lookahead)
        ):
            self.show_index(1, 0, 5)
            return Node('t_primary', [t_primary, slices])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and (t_primary := self.t_primary()) is not None
            and self.show_index(2, 1)
            and (genexp := self.genexp()) is not None
            and self.show_index(2, 2)
            and self.lookahead(True, self.t_lookahead)
        ):
            self.show_index(2, 0, 3)
            return Node('t_primary', [t_primary, genexp])
        self.reset(pos)
        if (True
            and self.show_index(3, 0)
            and (t_primary := self.t_primary()) is not None
            and self.show_index(3, 1)
            and self.expect('(') is not None
            and self.show_index(3, 2)
            and ((arguments := self.arguments()) is not None or True)
            and self.show_index(3, 3)
            and self.expect(')') is not None
            and self.show_index(3, 4)
            and self.lookahead(True, self.t_lookahead)
        ):
            self.show_index(3, 0, 5)
            return Node('t_primary', [t_primary, arguments])
        self.reset(pos)
        if (True
            and self.show_index(4, 0)
            and (atom := self.atom()) is not None
            and self.show_index(4, 1)
            and self.lookahead(True, self.t_lookahead)
        ):
            self.show_index(4, 0, 2)
            return Node('t_primary', [atom])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def t_lookahead(self):
        self.show_rule('t_lookahead', [["'('"], ["'['"], ["'.'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('(') is not None
        ):
            self.show_index(0, 0, 1)
            return Node('t_lookahead', [])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and self.expect('[') is not None
        ):
            self.show_index(1, 0, 1)
            return Node('t_lookahead', [])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and self.expect('.') is not None
        ):
            self.show_index(2, 0, 1)
            return Node('t_lookahead', [])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def invalid_double_starred_kvpairs(self):
        self.show_rule('invalid_double_starred_kvpairs', [['_synthetic_rule_101', "','", 'invalid_kvpair'], ['expression', "':'", "'*'", 'bitwise_or'], ['expression', "':'", '&_synthetic_rule_102']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (_synthetic_rule_101 := self._synthetic_rule_101()) is not None
            and self.show_index(0, 1)
            and self.expect(',') is not None
            and self.show_index(0, 2)
            and (invalid_kvpair := self.invalid_kvpair()) is not None
        ):
            self.show_index(0, 0, 3)
            return Node('invalid_double_starred_kvpairs', [_synthetic_rule_101, invalid_kvpair])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (expression := self.expression()) is not None
            and self.show_index(1, 1)
            and self.expect(':') is not None
            and self.show_index(1, 2)
            and (a := self.expect('*')) is not None
            and self.show_index(1, 3)
            and (bitwise_or := self.bitwise_or()) is not None
        ):
            self.show_index(1, 0, 4)
            return Node('invalid_double_starred_kvpairs', [expression, a, bitwise_or])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and (expression := self.expression()) is not None
            and self.show_index(2, 1)
            and (a := self.expect(':')) is not None
            and self.show_index(2, 2)
            and self.lookahead(True, self._synthetic_rule_102)
        ):
            self.show_index(2, 0, 3)
            return Node('invalid_double_starred_kvpairs', [expression, a])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def invalid_kvpair(self):
        self.show_rule('invalid_kvpair', [['expression', "!':'"], ['expression', "':'", "'*'", 'bitwise_or'], ['expression', "':'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (a := self.expression()) is not None
            and self.show_index(0, 1)
            and self.lookahead(False, self.expect, ':')
        ):
            self.show_index(0, 0, 2)
            return Node('invalid_kvpair', [a])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (expression := self.expression()) is not None
            and self.show_index(1, 1)
            and self.expect(':') is not None
            and self.show_index(1, 2)
            and (a := self.expect('*')) is not None
            and self.show_index(1, 3)
            and (bitwise_or := self.bitwise_or()) is not None
        ):
            self.show_index(1, 0, 4)
            return Node('invalid_kvpair', [expression, a, bitwise_or])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and (expression := self.expression()) is not None
            and self.show_index(2, 1)
            and (a := self.expect(':')) is not None
        ):
            self.show_index(2, 0, 2)
            return Node('invalid_kvpair', [expression, a])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_0(self):
        self.show_rule('_synthetic_rule_0', [["','", 'expression']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect(',') is not None
            and self.show_index(0, 1)
            and (expression := self.expression()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_0', [expression])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_1(self):
        self.show_rule('_synthetic_rule_1', [['expression', '_synthetic_rule_0*']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (expression := self.expression()) is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_0 := self.loop(False, self._synthetic_rule_0)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_1', [expression, _synthetic_rule_0])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_2(self):
        self.show_rule('_synthetic_rule_2', [["','", 'expression']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect(',') is not None
            and self.show_index(0, 1)
            and (expression := self.expression()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_2', [expression])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_3(self):
        self.show_rule('_synthetic_rule_3', [['expression', '_synthetic_rule_2*']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (expression := self.expression()) is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_2 := self.loop(False, self._synthetic_rule_2)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_3', [expression, _synthetic_rule_2])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_4(self):
        self.show_rule('_synthetic_rule_4', [["','", 'expression']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect(',') is not None
            and self.show_index(0, 1)
            and (expression := self.expression()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_4', [expression])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_5(self):
        self.show_rule('_synthetic_rule_5', [['expression', '_synthetic_rule_4*']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (expression := self.expression()) is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_4 := self.loop(False, self._synthetic_rule_4)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_5', [expression, _synthetic_rule_4])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_6(self):
        self.show_rule('_synthetic_rule_6', [["','", 'expression']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect(',') is not None
            and self.show_index(0, 1)
            and (expression := self.expression()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_6', [expression])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_7(self):
        self.show_rule('_synthetic_rule_7', [['expression', '_synthetic_rule_6*']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (expression := self.expression()) is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_6 := self.loop(False, self._synthetic_rule_6)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_7', [expression, _synthetic_rule_6])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_8(self):
        self.show_rule('_synthetic_rule_8', [["';'", 'simple_stmt']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect(';') is not None
            and self.show_index(0, 1)
            and (simple_stmt := self.simple_stmt()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_8', [simple_stmt])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_9(self):
        self.show_rule('_synthetic_rule_9', [['simple_stmt', '_synthetic_rule_8*']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (simple_stmt := self.simple_stmt()) is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_8 := self.loop(False, self._synthetic_rule_8)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_9', [simple_stmt, _synthetic_rule_8])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_10(self):
        self.show_rule('_synthetic_rule_10', [["'='", 'annotated_rhs']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('=') is not None
            and self.show_index(0, 1)
            and (annotated_rhs := self.annotated_rhs()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_10', [annotated_rhs])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_11(self):
        self.show_rule('_synthetic_rule_11', [["'('", 'single_target', "')'"], ['single_subscript_attribute_target']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('(') is not None
            and self.show_index(0, 1)
            and (single_target := self.single_target()) is not None
            and self.show_index(0, 2)
            and self.expect(')') is not None
        ):
            self.show_index(0, 0, 3)
            return Node('_synthetic_rule_11', [single_target])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (single_subscript_attribute_target := self.single_subscript_attribute_target()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('_synthetic_rule_11', [single_subscript_attribute_target])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_12(self):
        self.show_rule('_synthetic_rule_12', [["'='", 'annotated_rhs']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('=') is not None
            and self.show_index(0, 1)
            and (annotated_rhs := self.annotated_rhs()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_12', [annotated_rhs])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_13(self):
        self.show_rule('_synthetic_rule_13', [['star_targets', "'='"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (star_targets := self.star_targets()) is not None
            and self.show_index(0, 1)
            and self.expect('=') is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_13', [star_targets])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_14(self):
        self.show_rule('_synthetic_rule_14', [['yield_expr'], ['star_expressions']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (yield_expr := self.yield_expr()) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('_synthetic_rule_14', [yield_expr])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (star_expressions := self.star_expressions()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('_synthetic_rule_14', [star_expressions])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_15(self):
        self.show_rule('_synthetic_rule_15', [['yield_expr'], ['star_expressions']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (yield_expr := self.yield_expr()) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('_synthetic_rule_15', [yield_expr])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (star_expressions := self.star_expressions()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('_synthetic_rule_15', [star_expressions])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_16(self):
        self.show_rule('_synthetic_rule_16', [["','", 'NAME']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect(',') is not None
            and self.show_index(0, 1)
            and (name := self.expect(NAME)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_16', [name])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_17(self):
        self.show_rule('_synthetic_rule_17', [['NAME', '_synthetic_rule_16*']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (name := self.expect(NAME)) is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_16 := self.loop(False, self._synthetic_rule_16)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_17', [name, _synthetic_rule_16])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_18(self):
        self.show_rule('_synthetic_rule_18', [["','", 'NAME']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect(',') is not None
            and self.show_index(0, 1)
            and (name := self.expect(NAME)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_18', [name])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_19(self):
        self.show_rule('_synthetic_rule_19', [['NAME', '_synthetic_rule_18*']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (name := self.expect(NAME)) is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_18 := self.loop(False, self._synthetic_rule_18)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_19', [name, _synthetic_rule_18])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_20(self):
        self.show_rule('_synthetic_rule_20', [["','", 'expression']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect(',') is not None
            and self.show_index(0, 1)
            and (expression := self.expression()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_20', [expression])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_21(self):
        self.show_rule('_synthetic_rule_21', [["';'"], ['NEWLINE']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect(';') is not None
        ):
            self.show_index(0, 0, 1)
            return Node('_synthetic_rule_21', [])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (newline := self.expect(NEWLINE)) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('_synthetic_rule_21', [newline])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_22(self):
        self.show_rule('_synthetic_rule_22', [["'.'"], ["'...'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('.') is not None
        ):
            self.show_index(0, 0, 1)
            return Node('_synthetic_rule_22', [])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and self.expect('...') is not None
        ):
            self.show_index(1, 0, 1)
            return Node('_synthetic_rule_22', [])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_23(self):
        self.show_rule('_synthetic_rule_23', [["'.'"], ["'...'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('.') is not None
        ):
            self.show_index(0, 0, 1)
            return Node('_synthetic_rule_23', [])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and self.expect('...') is not None
        ):
            self.show_index(1, 0, 1)
            return Node('_synthetic_rule_23', [])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_24(self):
        self.show_rule('_synthetic_rule_24', [["','", 'import_from_as_name']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect(',') is not None
            and self.show_index(0, 1)
            and (import_from_as_name := self.import_from_as_name()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_24', [import_from_as_name])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_25(self):
        self.show_rule('_synthetic_rule_25', [['import_from_as_name', '_synthetic_rule_24*']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (import_from_as_name := self.import_from_as_name()) is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_24 := self.loop(False, self._synthetic_rule_24)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_25', [import_from_as_name, _synthetic_rule_24])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_26(self):
        self.show_rule('_synthetic_rule_26', [["'as'", 'NAME']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('as') is not None
            and self.show_index(0, 1)
            and (name := self.expect(NAME)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_26', [name])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_27(self):
        self.show_rule('_synthetic_rule_27', [["','", 'dotted_as_name']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect(',') is not None
            and self.show_index(0, 1)
            and (dotted_as_name := self.dotted_as_name()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_27', [dotted_as_name])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_28(self):
        self.show_rule('_synthetic_rule_28', [['dotted_as_name', '_synthetic_rule_27*']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (dotted_as_name := self.dotted_as_name()) is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_27 := self.loop(False, self._synthetic_rule_27)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_28', [dotted_as_name, _synthetic_rule_27])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_29(self):
        self.show_rule('_synthetic_rule_29', [["'as'", 'NAME']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('as') is not None
            and self.show_index(0, 1)
            and (name := self.expect(NAME)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_29', [name])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_30(self):
        self.show_rule('_synthetic_rule_30', [["','", 'with_item']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect(',') is not None
            and self.show_index(0, 1)
            and (with_item := self.with_item()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_30', [with_item])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_31(self):
        self.show_rule('_synthetic_rule_31', [['with_item', '_synthetic_rule_30*']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (with_item := self.with_item()) is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_30 := self.loop(False, self._synthetic_rule_30)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_31', [with_item, _synthetic_rule_30])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_32(self):
        self.show_rule('_synthetic_rule_32', [["','", 'with_item']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect(',') is not None
            and self.show_index(0, 1)
            and (with_item := self.with_item()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_32', [with_item])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_33(self):
        self.show_rule('_synthetic_rule_33', [['with_item', '_synthetic_rule_32*']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (with_item := self.with_item()) is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_32 := self.loop(False, self._synthetic_rule_32)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_33', [with_item, _synthetic_rule_32])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_34(self):
        self.show_rule('_synthetic_rule_34', [["','", 'with_item']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect(',') is not None
            and self.show_index(0, 1)
            and (with_item := self.with_item()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_34', [with_item])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_35(self):
        self.show_rule('_synthetic_rule_35', [['with_item', '_synthetic_rule_34*']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (with_item := self.with_item()) is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_34 := self.loop(False, self._synthetic_rule_34)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_35', [with_item, _synthetic_rule_34])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_36(self):
        self.show_rule('_synthetic_rule_36', [["','", 'with_item']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect(',') is not None
            and self.show_index(0, 1)
            and (with_item := self.with_item()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_36', [with_item])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_37(self):
        self.show_rule('_synthetic_rule_37', [['with_item', '_synthetic_rule_36*']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (with_item := self.with_item()) is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_36 := self.loop(False, self._synthetic_rule_36)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_37', [with_item, _synthetic_rule_36])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_38(self):
        self.show_rule('_synthetic_rule_38', [["','"], ["')'"], ["':'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect(',') is not None
        ):
            self.show_index(0, 0, 1)
            return Node('_synthetic_rule_38', [])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and self.expect(')') is not None
        ):
            self.show_index(1, 0, 1)
            return Node('_synthetic_rule_38', [])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and self.expect(':') is not None
        ):
            self.show_index(2, 0, 1)
            return Node('_synthetic_rule_38', [])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_39(self):
        self.show_rule('_synthetic_rule_39', [["'as'", 'NAME']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('as') is not None
            and self.show_index(0, 1)
            and (name := self.expect(NAME)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_39', [name])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_40(self):
        self.show_rule('_synthetic_rule_40', [["'|'", 'closed_pattern']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('|') is not None
            and self.show_index(0, 1)
            and (closed_pattern := self.closed_pattern()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_40', [closed_pattern])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_41(self):
        self.show_rule('_synthetic_rule_41', [['closed_pattern', '_synthetic_rule_40*']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (closed_pattern := self.closed_pattern()) is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_40 := self.loop(False, self._synthetic_rule_40)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_41', [closed_pattern, _synthetic_rule_40])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_42(self):
        self.show_rule('_synthetic_rule_42', [["'+'"], ["'-'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('+') is not None
        ):
            self.show_index(0, 0, 1)
            return Node('_synthetic_rule_42', [])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and self.expect('-') is not None
        ):
            self.show_index(1, 0, 1)
            return Node('_synthetic_rule_42', [])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_43(self):
        self.show_rule('_synthetic_rule_43', [["'+'"], ["'-'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('+') is not None
        ):
            self.show_index(0, 0, 1)
            return Node('_synthetic_rule_43', [])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and self.expect('-') is not None
        ):
            self.show_index(1, 0, 1)
            return Node('_synthetic_rule_43', [])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_44(self):
        self.show_rule('_synthetic_rule_44', [["'.'"], ["'('"], ["'='"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('.') is not None
        ):
            self.show_index(0, 0, 1)
            return Node('_synthetic_rule_44', [])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and self.expect('(') is not None
        ):
            self.show_index(1, 0, 1)
            return Node('_synthetic_rule_44', [])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and self.expect('=') is not None
        ):
            self.show_index(2, 0, 1)
            return Node('_synthetic_rule_44', [])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_45(self):
        self.show_rule('_synthetic_rule_45', [["'.'"], ["'('"], ["'='"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('.') is not None
        ):
            self.show_index(0, 0, 1)
            return Node('_synthetic_rule_45', [])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and self.expect('(') is not None
        ):
            self.show_index(1, 0, 1)
            return Node('_synthetic_rule_45', [])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and self.expect('=') is not None
        ):
            self.show_index(2, 0, 1)
            return Node('_synthetic_rule_45', [])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_46(self):
        self.show_rule('_synthetic_rule_46', [["','", 'maybe_star_pattern']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect(',') is not None
            and self.show_index(0, 1)
            and (maybe_star_pattern := self.maybe_star_pattern()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_46', [maybe_star_pattern])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_47(self):
        self.show_rule('_synthetic_rule_47', [['maybe_star_pattern', '_synthetic_rule_46*']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (maybe_star_pattern := self.maybe_star_pattern()) is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_46 := self.loop(False, self._synthetic_rule_46)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_47', [maybe_star_pattern, _synthetic_rule_46])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_48(self):
        self.show_rule('_synthetic_rule_48', [["','", 'key_value_pattern']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect(',') is not None
            and self.show_index(0, 1)
            and (key_value_pattern := self.key_value_pattern()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_48', [key_value_pattern])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_49(self):
        self.show_rule('_synthetic_rule_49', [['key_value_pattern', '_synthetic_rule_48*']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (key_value_pattern := self.key_value_pattern()) is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_48 := self.loop(False, self._synthetic_rule_48)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_49', [key_value_pattern, _synthetic_rule_48])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_50(self):
        self.show_rule('_synthetic_rule_50', [['literal_expr'], ['attr']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (literal_expr := self.literal_expr()) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('_synthetic_rule_50', [literal_expr])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (attr := self.attr()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('_synthetic_rule_50', [attr])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_51(self):
        self.show_rule('_synthetic_rule_51', [["','", 'pattern']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect(',') is not None
            and self.show_index(0, 1)
            and (pattern := self.pattern()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_51', [pattern])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_52(self):
        self.show_rule('_synthetic_rule_52', [['pattern', '_synthetic_rule_51*']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (pattern := self.pattern()) is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_51 := self.loop(False, self._synthetic_rule_51)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_52', [pattern, _synthetic_rule_51])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_53(self):
        self.show_rule('_synthetic_rule_53', [["','", 'keyword_pattern']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect(',') is not None
            and self.show_index(0, 1)
            and (keyword_pattern := self.keyword_pattern()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_53', [keyword_pattern])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_54(self):
        self.show_rule('_synthetic_rule_54', [['keyword_pattern', '_synthetic_rule_53*']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (keyword_pattern := self.keyword_pattern()) is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_53 := self.loop(False, self._synthetic_rule_53)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_54', [keyword_pattern, _synthetic_rule_53])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_55(self):
        self.show_rule('_synthetic_rule_55', [["'from'", 'expression']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('from') is not None
            and self.show_index(0, 1)
            and (expression := self.expression()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_55', [expression])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_56(self):
        self.show_rule('_synthetic_rule_56', [["'->'", 'expression']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('->') is not None
            and self.show_index(0, 1)
            and (expression := self.expression()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_56', [expression])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_57(self):
        self.show_rule('_synthetic_rule_57', [["'->'", 'expression']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('->') is not None
            and self.show_index(0, 1)
            and (expression := self.expression()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_57', [expression])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_58(self):
        self.show_rule('_synthetic_rule_58', [['NEWLINE', 'INDENT']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (newline := self.expect(NEWLINE)) is not None
            and self.show_index(0, 1)
            and (indent := self.expect(INDENT)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_58', [newline, indent])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_59(self):
        self.show_rule('_synthetic_rule_59', [["'@'", 'named_expression', 'NEWLINE']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('@') is not None
            and self.show_index(0, 1)
            and (named_expression := self.named_expression()) is not None
            and self.show_index(0, 2)
            and (newline := self.expect(NEWLINE)) is not None
        ):
            self.show_index(0, 0, 3)
            return Node('_synthetic_rule_59', [named_expression, newline])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_60(self):
        self.show_rule('_synthetic_rule_60', [["'('", '[arguments]', "')'"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('(') is not None
            and self.show_index(0, 1)
            and ((arguments := self.arguments()) is not None or True)
            and self.show_index(0, 2)
            and self.expect(')') is not None
        ):
            self.show_index(0, 0, 3)
            return Node('_synthetic_rule_60', [arguments])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_61(self):
        self.show_rule('_synthetic_rule_61', [["','", 'star_expression']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect(',') is not None
            and self.show_index(0, 1)
            and (star_expression := self.star_expression()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_61', [star_expression])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_62(self):
        self.show_rule('_synthetic_rule_62', [["','", 'star_named_expression']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect(',') is not None
            and self.show_index(0, 1)
            and (star_named_expression := self.star_named_expression()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_62', [star_named_expression])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_63(self):
        self.show_rule('_synthetic_rule_63', [['star_named_expression', '_synthetic_rule_62*']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (star_named_expression := self.star_named_expression()) is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_62 := self.loop(False, self._synthetic_rule_62)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_63', [star_named_expression, _synthetic_rule_62])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_64(self):
        self.show_rule('_synthetic_rule_64', [["','", 'expression']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect(',') is not None
            and self.show_index(0, 1)
            and (expression := self.expression()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_64', [expression])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_65(self):
        self.show_rule('_synthetic_rule_65', [["'or'", 'conjunction']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('or') is not None
            and self.show_index(0, 1)
            and (conjunction := self.conjunction()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_65', [conjunction])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_66(self):
        self.show_rule('_synthetic_rule_66', [["'and'", 'inversion']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('and') is not None
            and self.show_index(0, 1)
            and (inversion := self.inversion()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_66', [inversion])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_67(self):
        self.show_rule('_synthetic_rule_67', [["','", 'slice']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect(',') is not None
            and self.show_index(0, 1)
            and (slice := self.slice()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_67', [slice])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_68(self):
        self.show_rule('_synthetic_rule_68', [['slice', '_synthetic_rule_67*']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (slice := self.slice()) is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_67 := self.loop(False, self._synthetic_rule_67)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_68', [slice, _synthetic_rule_67])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_69(self):
        self.show_rule('_synthetic_rule_69', [["':'", '[expression]']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect(':') is not None
            and self.show_index(0, 1)
            and ((expression := self.expression()) is not None or True)
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_69', [expression])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_70(self):
        self.show_rule('_synthetic_rule_70', [['tuple'], ['group'], ['genexp']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (tuple := self.tuple()) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('_synthetic_rule_70', [tuple])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (group := self.group()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('_synthetic_rule_70', [group])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and (genexp := self.genexp()) is not None
        ):
            self.show_index(2, 0, 1)
            return Node('_synthetic_rule_70', [genexp])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_71(self):
        self.show_rule('_synthetic_rule_71', [['list'], ['listcomp']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (list := self.list()) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('_synthetic_rule_71', [list])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (listcomp := self.listcomp()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('_synthetic_rule_71', [listcomp])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_72(self):
        self.show_rule('_synthetic_rule_72', [['dict'], ['set'], ['dictcomp'], ['setcomp']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (dict := self.dict()) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('_synthetic_rule_72', [dict])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (set := self.set()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('_synthetic_rule_72', [set])
        self.reset(pos)
        if (True
            and self.show_index(2, 0)
            and (dictcomp := self.dictcomp()) is not None
        ):
            self.show_index(2, 0, 1)
            return Node('_synthetic_rule_72', [dictcomp])
        self.reset(pos)
        if (True
            and self.show_index(3, 0)
            and (setcomp := self.setcomp()) is not None
        ):
            self.show_index(3, 0, 1)
            return Node('_synthetic_rule_72', [setcomp])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_73(self):
        self.show_rule('_synthetic_rule_73', [['star_named_expression', "','", '[star_named_expressions]']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (star_named_expression := self.star_named_expression()) is not None
            and self.show_index(0, 1)
            and self.expect(',') is not None
            and self.show_index(0, 2)
            and ((star_named_expressions := self.star_named_expressions()) is not None or True)
        ):
            self.show_index(0, 0, 3)
            return Node('_synthetic_rule_73', [star_named_expression, star_named_expressions])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_74(self):
        self.show_rule('_synthetic_rule_74', [['yield_expr'], ['named_expression']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (yield_expr := self.yield_expr()) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('_synthetic_rule_74', [yield_expr])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (named_expression := self.named_expression()) is not None
        ):
            self.show_index(1, 0, 1)
            return Node('_synthetic_rule_74', [named_expression])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_75(self):
        self.show_rule('_synthetic_rule_75', [['assignment_expression'], ['expression', "!':='"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (assignment_expression := self.assignment_expression()) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('_synthetic_rule_75', [assignment_expression])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (expression := self.expression()) is not None
            and self.show_index(1, 1)
            and self.lookahead(False, self.expect, ':=')
        ):
            self.show_index(1, 0, 2)
            return Node('_synthetic_rule_75', [expression])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_76(self):
        self.show_rule('_synthetic_rule_76', [["','", 'double_starred_kvpair']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect(',') is not None
            and self.show_index(0, 1)
            and (double_starred_kvpair := self.double_starred_kvpair()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_76', [double_starred_kvpair])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_77(self):
        self.show_rule('_synthetic_rule_77', [['double_starred_kvpair', '_synthetic_rule_76*']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (double_starred_kvpair := self.double_starred_kvpair()) is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_76 := self.loop(False, self._synthetic_rule_76)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_77', [double_starred_kvpair, _synthetic_rule_76])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_78(self):
        self.show_rule('_synthetic_rule_78', [["'if'", 'disjunction']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('if') is not None
            and self.show_index(0, 1)
            and (disjunction := self.disjunction()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_78', [disjunction])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_79(self):
        self.show_rule('_synthetic_rule_79', [["'if'", 'disjunction']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('if') is not None
            and self.show_index(0, 1)
            and (disjunction := self.disjunction()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_79', [disjunction])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_80(self):
        self.show_rule('_synthetic_rule_80', [['assignment_expression'], ['expression', "!':='"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (assignment_expression := self.assignment_expression()) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('_synthetic_rule_80', [assignment_expression])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (expression := self.expression()) is not None
            and self.show_index(1, 1)
            and self.lookahead(False, self.expect, ':=')
        ):
            self.show_index(1, 0, 2)
            return Node('_synthetic_rule_80', [expression])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_81(self):
        self.show_rule('_synthetic_rule_81', [['assignment_expression'], ['expression', "!':='"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (assignment_expression := self.assignment_expression()) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('_synthetic_rule_81', [assignment_expression])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (expression := self.expression()) is not None
            and self.show_index(1, 1)
            and self.lookahead(False, self.expect, ':=')
        ):
            self.show_index(1, 0, 2)
            return Node('_synthetic_rule_81', [expression])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_82(self):
        self.show_rule('_synthetic_rule_82', [["','", 'starred_expression'], ['_synthetic_rule_81', "!'='"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect(',') is not None
            and self.show_index(0, 1)
            and (starred_expression := self.starred_expression()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_82', [starred_expression])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (_synthetic_rule_81 := self._synthetic_rule_81()) is not None
            and self.show_index(1, 1)
            and self.lookahead(False, self.expect, '=')
        ):
            self.show_index(1, 0, 2)
            return Node('_synthetic_rule_82', [_synthetic_rule_81])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_83(self):
        self.show_rule('_synthetic_rule_83', [['starred_expression'], ['_synthetic_rule_80', "!'='", '_synthetic_rule_82*']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (starred_expression := self.starred_expression()) is not None
        ):
            self.show_index(0, 0, 1)
            return Node('_synthetic_rule_83', [starred_expression])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and (_synthetic_rule_80 := self._synthetic_rule_80()) is not None
            and self.show_index(1, 1)
            and self.lookahead(False, self.expect, '=')
            and self.show_index(1, 2)
            and (_synthetic_rule_82 := self.loop(False, self._synthetic_rule_82)) is not None
        ):
            self.show_index(1, 0, 3)
            return Node('_synthetic_rule_83', [_synthetic_rule_80, _synthetic_rule_82])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_84(self):
        self.show_rule('_synthetic_rule_84', [["','", 'kwargs']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect(',') is not None
            and self.show_index(0, 1)
            and (kwargs := self.kwargs()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_84', [kwargs])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_85(self):
        self.show_rule('_synthetic_rule_85', [["','", 'kwarg_or_starred']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect(',') is not None
            and self.show_index(0, 1)
            and (kwarg_or_starred := self.kwarg_or_starred()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_85', [kwarg_or_starred])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_86(self):
        self.show_rule('_synthetic_rule_86', [['kwarg_or_starred', '_synthetic_rule_85*']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (kwarg_or_starred := self.kwarg_or_starred()) is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_85 := self.loop(False, self._synthetic_rule_85)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_86', [kwarg_or_starred, _synthetic_rule_85])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_87(self):
        self.show_rule('_synthetic_rule_87', [["','", 'kwarg_or_double_starred']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect(',') is not None
            and self.show_index(0, 1)
            and (kwarg_or_double_starred := self.kwarg_or_double_starred()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_87', [kwarg_or_double_starred])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_88(self):
        self.show_rule('_synthetic_rule_88', [['kwarg_or_double_starred', '_synthetic_rule_87*']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (kwarg_or_double_starred := self.kwarg_or_double_starred()) is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_87 := self.loop(False, self._synthetic_rule_87)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_88', [kwarg_or_double_starred, _synthetic_rule_87])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_89(self):
        self.show_rule('_synthetic_rule_89', [["','", 'kwarg_or_starred']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect(',') is not None
            and self.show_index(0, 1)
            and (kwarg_or_starred := self.kwarg_or_starred()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_89', [kwarg_or_starred])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_90(self):
        self.show_rule('_synthetic_rule_90', [['kwarg_or_starred', '_synthetic_rule_89*']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (kwarg_or_starred := self.kwarg_or_starred()) is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_89 := self.loop(False, self._synthetic_rule_89)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_90', [kwarg_or_starred, _synthetic_rule_89])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_91(self):
        self.show_rule('_synthetic_rule_91', [["','", 'kwarg_or_double_starred']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect(',') is not None
            and self.show_index(0, 1)
            and (kwarg_or_double_starred := self.kwarg_or_double_starred()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_91', [kwarg_or_double_starred])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_92(self):
        self.show_rule('_synthetic_rule_92', [['kwarg_or_double_starred', '_synthetic_rule_91*']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (kwarg_or_double_starred := self.kwarg_or_double_starred()) is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_91 := self.loop(False, self._synthetic_rule_91)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_92', [kwarg_or_double_starred, _synthetic_rule_91])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_93(self):
        self.show_rule('_synthetic_rule_93', [["','", 'star_target']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect(',') is not None
            and self.show_index(0, 1)
            and (star_target := self.star_target()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_93', [star_target])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_94(self):
        self.show_rule('_synthetic_rule_94', [["','", 'star_target']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect(',') is not None
            and self.show_index(0, 1)
            and (star_target := self.star_target()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_94', [star_target])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_95(self):
        self.show_rule('_synthetic_rule_95', [['star_target', '_synthetic_rule_94*']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (star_target := self.star_target()) is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_94 := self.loop(False, self._synthetic_rule_94)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_95', [star_target, _synthetic_rule_94])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_96(self):
        self.show_rule('_synthetic_rule_96', [["','", 'star_target']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect(',') is not None
            and self.show_index(0, 1)
            and (star_target := self.star_target()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_96', [star_target])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_97(self):
        self.show_rule('_synthetic_rule_97', [["!'*'", 'star_target']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.lookahead(False, self.expect, '*')
            and self.show_index(0, 1)
            and (star_target := self.star_target()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_97', [star_target])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_98(self):
        self.show_rule('_synthetic_rule_98', [["','", 'del_target']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect(',') is not None
            and self.show_index(0, 1)
            and (del_target := self.del_target()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_98', [del_target])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_99(self):
        self.show_rule('_synthetic_rule_99', [['del_target', '_synthetic_rule_98*']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (del_target := self.del_target()) is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_98 := self.loop(False, self._synthetic_rule_98)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_99', [del_target, _synthetic_rule_98])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_100(self):
        self.show_rule('_synthetic_rule_100', [["','", 'double_starred_kvpair']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect(',') is not None
            and self.show_index(0, 1)
            and (double_starred_kvpair := self.double_starred_kvpair()) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_100', [double_starred_kvpair])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_101(self):
        self.show_rule('_synthetic_rule_101', [['double_starred_kvpair', '_synthetic_rule_100*']])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and (double_starred_kvpair := self.double_starred_kvpair()) is not None
            and self.show_index(0, 1)
            and (_synthetic_rule_100 := self.loop(False, self._synthetic_rule_100)) is not None
        ):
            self.show_index(0, 0, 2)
            return Node('_synthetic_rule_101', [double_starred_kvpair, _synthetic_rule_100])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None

    @memoize
    def _synthetic_rule_102(self):
        self.show_rule('_synthetic_rule_102', [["'}'"], ["','"]])
        pos = self.mark()
        if (True
            and self.show_index(0, 0)
            and self.expect('}') is not None
        ):
            self.show_index(0, 0, 1)
            return Node('_synthetic_rule_102', [])
        self.reset(pos)
        if (True
            and self.show_index(1, 0)
            and self.expect(',') is not None
        ):
            self.show_index(1, 0, 1)
            return Node('_synthetic_rule_102', [])
        self.reset(pos)
        self.show_index(0, 0, 0)
        return None
