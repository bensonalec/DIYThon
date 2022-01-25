from std import Tokenizer
from tokenize import generate_tokens
from out import ToyParser
with open("sample.txt") as fi:
    tokenGen = generate_tokens(fi.read)
    # for i in tokenGen:
    #     print(i)
    p = ToyParser(Tokenizer(tokenGen))
    gram = p.start()
print(gram.translate())