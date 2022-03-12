from asyncore import loop
from tokenize import TokenInfo, generate_tokens, STRING, NEWLINE, NAME, ENDMARKER
from more_itertools import peekable
import io
from copy import deepcopy
class translation_tokenizer:
    def __init__(self, translation_definition):
        buf = io.StringIO(translation_definition)
        self.tokens = list(generate_tokens(buf.read))
        self.index = 0

    def peek(self):
        return self.tokens[self.index]
    
    def next(self):
        to_return = self.tokens[self.index]
        self.index += 1
        return to_return

    def mark(self):
        return self.index

    def reset(self, index):
        self.index = index


def translateVar(ar):
    #ar can be a tuple, list, Tokeninfo, or rule
    if(type(ar) != str):
        try:
            ar = ar.translate()
        except AttributeError:
            pass
        if type(ar) == tuple:
            toReturn = ()
            for a in ar:
                toReturn.append(translateVar(a))
            return toReturn
            #     return translateVar(a)
            # return [translateVar(a) for a in ar]
        if type(ar) == list:
            toReturn = []
            for a in ar:
                toReturn.append(translateVar(a))
            return toReturn

            # for a in ar:
            #     return translateVar(a)
            # return [translateVar(a) for a in ar]
        if type(ar) == TokenInfo:
            return ar.string
        return ar
    else:
        return ar

class translation_parser:
    def __init__(self, translation_definition, *args):
        self.translation_definition = translation_definition
        self.tokenizer = translation_tokenizer(translation_definition)
        self.translatedArgs = []
        self.args = args
        # print(self.args)
        for ar in args:
            self.translatedArgs.append(translateVar(ar))
        self.initialArgs = deepcopy(self.translatedArgs)
    def parse(self, end_marker=ENDMARKER):
        try:
            self.current_tab_level = 0
            result = ""
            while(tok := self.tokenizer.next()):
                if tok.type == end_marker or tok.string == end_marker:
                    return result
                if tok.type == STRING:
                    result += "\t"*self.current_tab_level + tok.string.replace("\"","")
                if tok.type == NEWLINE and tok.string=="\n":
                    result += "\n"
                if tok.type == NAME and tok.string.startswith("_"):
                    if self.tokenizer.peek().string == "[":
                        #contains some indexing
                        letter = tok.string[1:]
                        index = ord(letter) - 97

                        self.tokenizer.next()
                        indice = self.find_index()
                        indice = [int(x) for x in indice.split(",")]
                        currentVar = self.translatedArgs[index]
                        for ind in indice:
                            currentVar = currentVar[ind]
                        # if type(self.translatedArgs[index][ind] == list and len(self.translatedArgs[index][ind]) == 1):
                        #     self.translatedArgs[index][ind] = self.translatedArgs[index][ind][0]                            
                        result += "\t"*self.current_tab_level + currentVar
                    else:
                        letter = tok.string[1:]
                        index = ord(letter) - 97
                        # if type(self.translatedArgs[index] == list and len(self.translatedArgs[index]) == 1):
                        #     print(self.translatedArgs[index])
                        #     self.translatedArgs[index] = self.translatedArgs[index][0]
                        
                        result += "\t"*self.current_tab_level + self.translatedArgs[index]
                if tok.type == NAME and tok.string == "TABBED":
                    #want to consume tokens until ENDTABBED is reached
                    self.current_tab_level += 1
                if tok.type == NAME and tok.string == "ENDTABBED":
                    self.current_tab_level -= 1
                if tok.type == NAME and tok.string == "STARTLOOP":
                    #want to consume tokens until ENDLOOP is reached
                    loop_contents = self.loop()
                    result += loop_contents
                if tok.type == NAME and tok.string == "OPTIONAL":
                    opt_content = self.optional()
                    result += opt_content
        except:
            print(self.args)
            print(self.initialArgs)
            print(self.translatedArgs)
            exit()
    def find_index(self):
        result = ""
        while(tok := self.tokenizer.next()):
            if tok.string == "]":
                return result
            else:
                result += tok.string

    def get_index_from_variable(self, variable_string):
        letter = variable_string[1:]
        index = ord(letter) - 97
        return index

    def optional(self):
        result = ""
        loop_variables = []
        while(tok := self.tokenizer.next()):
            if tok.string == "ENDOPTIONAL":
                return result
            if tok.type == STRING:
                result += "\t"*self.current_tab_level + tok.string.replace("\"","") + " "
            if tok.type == NEWLINE:
                result += "\n"
            if tok.type == NAME and tok.string.startswith("_"):
                if self.tokenizer.peek().string == "[":
                    #contains some indexing
                    letter = tok.string[1:]
                    index = ord(letter) - 97

                    self.tokenizer.next()
                    indice = self.find_index()
                    indice = [int(x) for x in indice.split(",")]
                    currentVar = self.translatedArgs[index]
                    for ind in indice:
                        currentVar = currentVar[ind]

                    # ind = int(self.find_index())
                    result += "\t"*self.current_tab_level + currentVar
                else:
                    index = self.get_index_from_variable(tok.string)
                    if self.translatedArgs[index]:
                        if type(self.translatedArgs[index]) == list:
                            if tok.string not in loop_variables:
                                loop_variables.append(tok.string)
                            if len(self.translatedArgs[index]) == 0:
                                continue
                            result += "\t"*self.current_tab_level + self.translatedArgs[index][0]
                            self.translatedArgs[index].pop(0)
                        else:
                            if self.tokenizer.peek().string == "[":
                                #contains some indexing
                                pass
                            else:
                                letter = tok.string[1:]
                                index = ord(letter) - 97
                                result += "\t"*self.current_tab_level + self.translatedArgs[index]
                    else:
                        continue
            if tok.type == NAME and tok.string == "TABBED":
                #want to consume tokens until ENDTABBED is reached
                self.current_tab_level += 1
            if tok.type == NAME and tok.string == "ENDTABBED":
                self.current_tab_level -= 1
            if tok.type == NAME and tok.string == "STARTLOOP":
                #want to consume tokens until ENDLOOP is reached
                loop_contents = self.parse("ENDLOOP")
                result += loop_contents
            if tok.type == NAME and tok.string == "OPTIONAL":
                opt_content = self.optional()
                result += opt_content


    def loop(self):
        result = ""
        loop_start = self.tokenizer.mark()
        loop_variables = []
        while(tok := self.tokenizer.next()):
            if tok.string == "ENDLOOP":
                finished = True
                for v in loop_variables:
                    name = v[0]
                    ind = v[1]
                    if ind is not None:
                        index = self.get_index_from_variable(name)
                        indice = indice
                        currentVar = self.translatedArgs[index]
                        for ind in indice:
                            currentVar = currentVar[ind]
                        if len(currentVar) > 0:
                            finished = False
                    else:
                        if len(self.translatedArgs[self.get_index_from_variable(name)]) > 0:
                            finished = False
                if finished:
                    return result
                else:
                    self.tokenizer.reset(loop_start)
            if tok.type == STRING:
                result += "\t"*self.current_tab_level + tok.string.replace("\"","") + " "
            if tok.type == NEWLINE:
                result += "\n"
            if tok.type == NAME and tok.string.startswith("_"):
                # print("Variable", self.translatedArgs)
                if self.tokenizer.peek().string == "[":
                    #contains some indexing
                    letter = tok.string[1:]
                    index = ord(letter) - 97

                    self.tokenizer.next()
                    # ind = int(self.find_index())
                    indice = self.find_index()
                    indice = [int(x) for x in indice.split(",")]
                    if len(indice) == 1:
                        currentVar = self.translatedArgs[index][indice[0]]
                    elif len(indice) == 2:
                        currentVar = self.translatedArgs[index][indice[0]][indice[1]]
                    # currentVar = self.translatedArgs[index]
                    # for ind in indice:
                    #     currentVar = currentVar[ind]

                    if type(currentVar) == list:
                        if (tok.string, indice) not in loop_variables:
                            loop_variables.append((tok.string,indice))
                        if len(currentVar) == 0:
                            continue
                        result += "\t"*self.current_tab_level + currentVar[0]
                        if len(indice) == 1:
                            self.translatedArgs[index][indice[0]].pop(0)
                        elif len(indice) == 2:
                            self.translatedArgs[index][indice[0]][indice[1]].pop(0)

                        # currentVar.pop(0)
                    else:
                        if self.tokenizer.peek().string == "[":
                            #contains some indexing
                            pass
                        else:
                            letter = tok.string[1:]
                            index = ord(letter) - 97
                            result += "\t"*self.current_tab_level + currentVar

                    # result += "\t"*self.current_tab_level + self.translatedArgs[index][ind]
                else:
                    index = self.get_index_from_variable(tok.string)
                    if type(self.translatedArgs[index]) == list:
                        if (tok.string, None) not in loop_variables:
                            loop_variables.append((tok.string, None))
                        if len(self.translatedArgs[index]) == 0:
                            continue
                        result += "\t"*self.current_tab_level + self.translatedArgs[index][0]
                        self.translatedArgs[index].pop(0)
                    else:
                        if self.tokenizer.peek().string == "[":
                            #contains some indexing
                            pass
                        else:
                            letter = tok.string[1:]
                            index = ord(letter) - 97
                            result += "\t"*self.current_tab_level + self.translatedArgs[index]
            if tok.type == NAME and tok.string == "TABBED":
                #want to consume tokens until ENDTABBED is reached
                self.current_tab_level += 1
            if tok.type == NAME and tok.string == "ENDTABBED":
                self.current_tab_level -= 1
            if tok.type == NAME and tok.string == "STARTLOOP":
                #want to consume tokens until ENDLOOP is reached
                loop_contents = self.parse("ENDLOOP")
                result += loop_contents
            if tok.type == NAME and tok.string == "OPTIONAL":
                opt_content = self.optional()
                result += opt_content



inp = """"def" _a "(" ")" ":"
TABBED "x = [" STARTLOOP _c "," _d "," ENDLOOP "]"
_e[1] 
OPTIONAL 
TABBED
_b 
ENDTABBED
ENDOPTIONAL
"return x"
ENDTABBED
"""

# print(translation_parser(inp, "SAMPLE_VAR", "OPTIONAL_VAR", ["SECOND_VAR", "THIRD_VAR", "FOURHT_VAR"], "FIFTH_VAR", ["SYNTEHTIC", "SECOND_SYNTH"]).parse())