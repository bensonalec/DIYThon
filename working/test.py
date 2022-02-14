from tokenize import generate_tokens
from tokenizer import Tokenizer
from grammar_parser import GeneratedParser
with open("./grammars/translation/python.grm") as fi:
    tokenGen = generate_tokens(fi.readline)
    p = GeneratedParser(Tokenizer(tokenGen))
    gram = p.start()

print(gram)