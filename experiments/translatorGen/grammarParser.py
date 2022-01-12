from tokenize import NAME, ENDMARKER, STRING, NEWLINE
from std import Parser, Node
class GrammarParser(Parser):
    code = ""
    nameCount = 0
    body = ""
    currentRule = ""
    andPart = []
    andReturns = []
    tokenList = set()
    currentTranslationName = None
    currentTranslation = []
    nodes = ""

    def start(self):
        if r := self.rules():
            pos = self.mark()
            if marker := self.expect(ENDMARKER):
                self.code += "from std import Parser\n"
                self.code += f"from tokenize import TokenInfo, {','.join(self.tokenList)}\n\n"
                self.code += f"from memo import memoize_left_rec\n"
                self.code += self.nodes + "\n"
                self.code += "class NewParser(Parser):\n"
                self.code += self.body

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
        n = self.expect(NAME)
        self.currentTranslationName = n.string if n != None else n
        if (n 
            and self.expect(":") 
            and (a := self.alts()) 
            and self.expect("{")
            and (t := self.translation())
            and self.expect("}")
            and self.expect(NEWLINE)
        ):
            self.body += f"""
    @memoize_left_rec
    def {n.string}(self):
        {self.currentRule}
        return None
            """
            self.currentRule = ""
            nodeVariables = [x for x in self.currentTranslation if x.startswith('_')]
            self.nodes += f"""
class {n.string}:
    def __init__(self, {", ".join([f"{x} = None" for x in nodeVariables])}, *rest):
        {",".join([f"self.{x}" for x in nodeVariables])} = {",".join([x for x in nodeVariables])}
        
    def translate(self):
        return f"{{{"}{".join([ f"self.{x}.translate() if type(self.{x}) != TokenInfo and self.{x} else self.{x}.string if self.{x} else self.{x}" if x.startswith("_") else x for x in self.currentTranslation])}}}"
"""
            self.currentTranslation = []
            return Node("rule", [n, a, t])
        self.reset(pos)
        return None

    def translation(self):
        if t := self.transLine():
            return Node("translation", [t])
        return None

    def transLine(self):
        if i := self.transItems():
            return Node('transLine', [i])
        return None

    def transItems(self):
        if i := self.transItem():
            pos = self.mark()
            if iSin := self.transItems():
                return Node("transItems", [i, iSin])
            self.reset(pos)
            return Node("transItems", [i])
        return None

    def transItem(self):
        pos = self.mark()
        if n := self.expect(NAME):
            self.currentTranslation.append(n.string)
            return n
        self.reset(pos)
        if s := self.expect(STRING):
            self.currentTranslation.append(s.string)
            return s
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
            self.currentRule += f"""
        pos = self.mark()
        if({" and ".join(self.andPart)}):
            # return {self.currentTranslationName}({", ".join(self.andReturns)})
            return ("{self.currentTranslationName}", [{", ".join(self.andReturns)}])
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
            self.andReturns.append(f"n{self.nameCount}")
            if(n.string.isupper()):
                self.tokenList.add(n.string)
            self.nameCount += 1
            return n
        self.reset(pos)
        if s := self.expect(STRING):
            self.andPart.append(f"self.expect({s.string})")
            self.nameCount += 1
            return s
        return None
