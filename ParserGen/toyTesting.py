from Tokenizer import Tokenizer
from toy import ToyParser
from treelib import Node as no, Tree as tr
from tokenize import TokenInfo, generate_tokens
grammar = None
with open("sampleToy.py") as f:
    tokengen = generate_tokens(f.read)
    # for tok in tokengen:
    #     print(tok)
    tok = Tokenizer(tokengen, None)
    p = ToyParser(tok)
    grammar = p.start()

if not grammar:
    if tok.tokens:
        last = tok.tokens[-1]
        print(f"Line {last.start[0]}:")
        print(last.line)
        print(" "*last.start[1] + "^")

import random
import string
print(grammar)
tree = tr()
def traverseNode(node, parent=None):
    global tree
    if(type(node) == list):
        for node in node[::]:
            nodeName = ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))
            tree.create_node(str(node), nodeName, parent=parent)
            for child in node.children:
                traverseNode(child, nodeName)
    else:
        try:
            node.children
            nodeName = ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))
            tree.create_node(str(node), nodeName, parent=parent)
            for child in node.children:
                traverseNode(child, nodeName)
        except AttributeError:
            nodeName = ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))
            tree.create_node(str(node), nodeName, parent=parent)

traverseNode(grammar)
tree.show()