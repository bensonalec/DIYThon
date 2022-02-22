from std import Tokenizer
from tokenize import generate_tokens
from grammarParser import GrammarParser

with open("../grammars/translation/python.grm") as fi:
    tokenGen = generate_tokens(fi.readline)
    # for tok in tokenGen:
    #     print(tok)
    p = GrammarParser(Tokenizer(tokenGen))
    gram = p.grammar()

# for rule in p.rules:
#     print(rule)
p.generateCode()