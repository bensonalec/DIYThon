from tokenize import NAME, ENDMARKER, STRING, NEWLINE
from std import Parser, Node
class GrammarParser(Parser):
    nameCount = 0
    body = ""
    currentRule = ""
    andPart = []
    andReturns = []
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
        #each rule should produce a function for the Parser, 
        #and a node class
        pos = self.mark()
        if ((n := self.expect(NAME)) 
            and self.expect(":") 
            and (a := self.alts()) 
            and self.expect(NEWLINE)
        ):
            self.body += f"""
            def {n.string}(self):
                {self.currentRule}
                return None
            """
            self.currentRule = ""
            return Node("rule", [n, a])
        self.reset(pos)
        return None

    def translation(self):
        return True

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
            self.currentRule += f"""
                pos = self.mark()
                if({" and ".join(self.andPart)}):
                    return [{", ".join(self.andReturns)}]
                self.reset(pos)
            """
            self.andPart = []
            self.andReturns = []
            return Node('alt', [i])
        return None

    def items(self):
        if i := self.item():
            pos = self.mark()
            if iSin := self.items():
                return Node("items", [i, iSin])
            self.reset(pos)
            return Node("items", [i])
        return None
    
    def item(self):
        pos = self.mark()
        if n := self.expect(NAME):
            self.andPart.append(f"(n{self.nameCount} := self.expect({n.string}))" if n.string.isupper() else f"(n{self.nameCount} := self.{n.string}())")
            self.andReturns.append(f"({n.string}, n{self.nameCount})")
            self.nameCount += 1
            return n
        self.reset(pos)
        if s := self.expect(STRING):
            self.andPart.append(f"self.expect({s.string})")
            self.nameCount += 1
            return s
        return None
