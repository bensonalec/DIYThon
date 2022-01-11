from tokenize import NAME, ENDMARKER, STRING, NEWLINE
from std import Parser, Node

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
