from std import Tokenizer
from tokenize import generate_tokens
from out import NewParser
with open("sample.txt") as fi:
    tokenGen = generate_tokens(fi.read)
    p = NewParser(Tokenizer(tokenGen))
    gram = p.start()
print(gram)