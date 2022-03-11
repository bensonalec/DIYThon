from tokenize import TokenInfo, generate_tokens
from tokenizer import Tokenizer
from out import ToyParser

with open("test_input.py") as fi:
    tokenGen = generate_tokens(fi.readline)
    p = ToyParser(Tokenizer(tokenGen))
    gram = p.file()


def dive(i):
    if type(i) == list:
        print(i)
        for i in i:
            for x in i.rest:
                dive(x)
    elif type(i) == TokenInfo:
        print(i)
    else:
        print(i.rest)

        for x in i.rest:
            dive(x)

with open("results.py", "w") as fi:
    fi.write(gram.translate())