from std import Tokenizer
from tokenize import generate_tokens
from grammarParser import GrammarParser
with open("../grammars/translation/toy.grm") as fi:
    tokenGen = generate_tokens(fi.read)
    p = GrammarParser(Tokenizer(tokenGen))
    gram = p.start()
print(p.code)