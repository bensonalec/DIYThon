from tokenize import TokenInfo, generate_tokens
from tokenizer import Tokenizer
from out import ToyParser

with open("test_input.py") as fi:
    tokenGen = generate_tokens(fi.readline)
    # for i in tokenGen:
    #     print(i)
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
        if(i is not None):
            print(i.rest)

            for x in i.rest:
                dive(x)

# dive(gram)

with open("results.py", "w") as fi:
    fi.write(gram.translate())