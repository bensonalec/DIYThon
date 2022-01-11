from toyClasses import Tokenizer, ToyParser
from tokenize import generate_tokens

with open("sampleInput.txt") as fi:
    tokenGen = generate_tokens(fi.read)
    p = ToyParser(Tokenizer(tokenGen))
    print(p.statement().translate())