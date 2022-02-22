from tokenize import generate_tokens
from tokenizer import Tokenizer
from out import ToyParser

with open("test_input.py") as fi:
    tokenGen = generate_tokens(fi.readline)
    # for i in tokenGen:
    #     print(i)
    p = ToyParser(Tokenizer(tokenGen))
    gram = p.file()

print(gram)

i = gram
def dive(i):
        while(i):
            if type(i) == list:
                for x in i:
                    dive(x)
            else:
                print(i)
                print("U")
            try:
                i = i._a
            except:
                print(i)
                break
# print(gram)
dive(i)