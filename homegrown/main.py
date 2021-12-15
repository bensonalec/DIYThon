from Tokenizer import Tokenizer
from toyParser import ToyParser
from tokenize import generate_tokens

with open("sampleInput.txt") as fi:
    tokenGen = generate_tokens(fi.read)
    p = ToyParser(Tokenizer(tokenGen))
    print(p.start())