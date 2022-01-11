from grammarParser import Tokenizer, GrammarParser
from tokenize import generate_tokens
from treelib import Node as no, Tree as tr
import random, string
with open("sampleGrammar.txt") as fi:
    tokenGen = generate_tokens(fi.read)
    p = GrammarParser(Tokenizer(tokenGen))
    gram = p.start()
print(gram)