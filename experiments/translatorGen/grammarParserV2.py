from collections import namedtuple
from tokenize import NAME, ENDMARKER, STRING, NEWLINE
from typing import NamedTuple
from std import Parser, Node

Rule = namedtuple("Rule", "Name Alts Translations")

class GrammarParser(Parser):
    rules = None
    def grammar(self):
        pos = self.mark()
        if r := self.rule():
            rules = [r]
            while r := self.rule():
                rules.append(r)
            if self.expect(ENDMARKER):
                self.rules = rules
                return rules
        self.reset(pos)
        return None

    def rule(self):
        pos = self.mark()
        if ((name := self.expect(NAME)) and self.expect(":") and (alt := self.alternative())):
            currentRule = Rule(name.string, [alt], [])
            tPos = self.mark()
            while(self.expect("|") and (alt := self.alternative())):
                currentRule.Alts.append(alt)
                tPos = self.mark()
            self.reset(tPos)
            if t := self.translation():
                currentRule.Translations.extend(t)
                if self.expect(NEWLINE):
                    return currentRule
        self.reset(pos)
        return None

    def translation(self):
        pos = self.mark()
        if (self.expect("{") and (a := self.alternative())):
            alts = [a]
            tPos = self.mark()
            while(self.expect("|") and (a := self.alternative())):
                alts.append(a)
                tPos = self.mark()
            self.reset(tPos)
            if self.expect("}"):
                return alts
        self.reset(pos)

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
        if p := self.expect(NAME):
            return p.string
        self.reset(pos)
        pos = self.mark()
        if p := self.expect(STRING):
            return p.string
        self.reset(pos)
        return None

    def generateCode(self):
        
        pass