from collections import namedtuple
from tokenize import NAME, ENDMARKER, STRING, NEWLINE, COMMENT
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
        output = ""
        output += f"from memo import memoize_left_rec\n"
        output += f"import tokenize\n"
        output += f"from std import Parser\n"
        nodes = []
        methods = []
        varNumber = 0
        if self.rules:
            for rule in self.rules:
                currentNode = ""
                currentMethod = ""
                #build node code
                for ind,translation in enumerate(rule.Translations):
                    variables = [x for x in translation if x.startswith('_')]
                    currentNode += f'class {rule.Name}{ind}:\n'
                    currentNode += f'\tdef __init__(self, {", ".join([f"{x}" for x in variables])}{"," if len(variables) > 0 else ""} *rest):\n'
                    for var in variables:
                        currentNode += f'\t\tself.{var} = {var}\n'
                    currentNode += "\t\tpass\n"
                    currentNode += f'\tdef translate(self):\n'
                    currentNode += f'\t\treturn f"{"".join([f"{{self.{x}.translate() if type(self.{x}) != str else self.{x}}}" if x in variables else f"{{{x}}}" for x in translation])}"\n'
                nodes.append(currentNode)
                #build parsing method code
                currentMethod += "\t@memoize_left_rec\n"
                currentMethod += f'\tdef {rule.Name}(self):\n'
                for ind, alternative in enumerate(rule.Alts):
                    variables = []
                    tokenInfos = []
                    currentMethod += '\t\tpos = self.mark()\n'
                    currentMethod += f'\t\tif (True and\n'
                    for item in alternative:
                        if item.startswith("'"):
                            currentMethod += f'\t\t   self.expect({item}) and\n'
                        elif item.isupper():
                            currentMethod += f'\t\t   (n{varNumber} := self.expect(tokenize.{item})) and\n'
                            variables.append(f"n{varNumber}")
                            tokenInfos.append(f"n{varNumber}")
                            varNumber += 1
                        else:
                            currentMethod += f'\t\t   (n{varNumber} := self.{item}()) and\n'
                            variables.append(f"n{varNumber}")
                            varNumber += 1
                    currentMethod += '\t\t   True):\n'
                    currentMethod += f'\t\t\treturn {rule.Name}{ind}({", ".join([x if x not in tokenInfos else f"{x}.string" for x in variables])})\n'
                    currentMethod += '\t\tself.reset(pos)\n'
                currentMethod += '\t\treturn None\n'
                methods.append(currentMethod)
        output += "\n".join([x for x in nodes])
        output += "class ToyParser(Parser):\n"
        output += "\n".join([x for x in methods])
        print(output)