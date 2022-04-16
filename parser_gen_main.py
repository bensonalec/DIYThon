from tokenize import generate_tokens
from tokenizer import Tokenizer
from grammar_parser import GeneratedParser
import io

def build_parser_from_string(inp, synth_num=0):
    buf = io.StringIO(inp)
    tokenGen = generate_tokens(buf.readline)
    p = GeneratedParser(Tokenizer(tokenGen))
    p.synthetic_rules = []
    p.synth_num = synth_num

    gram = p.start()
    p.synthetic_rules = {rule.name: rule for rule in p.synthetic_rules}
    gram.rules = gram.rules |  p.synthetic_rules
    return gram.rules, p.synth_num

def build_parser(grammar_file_location):
    with open(grammar_file_location) as fi:
        tokenGen = generate_tokens(fi.readline)
        p = GeneratedParser(Tokenizer(tokenGen))
        gram = p.start()

    p.synthetic_rules = {rule.name: rule for rule in p.synthetic_rules}
    gram.rules = gram.rules |  p.synthetic_rules
    return gram.rules

def generate_parser(rules):
    varnum = 0
    parserClass = ""
    nodeClasses = ""
    for _, rule in rules:
        variables = []
        currentNode = ""
        if rule.name.startswith('synthetic_rule_'):
            currentNode += f'class {rule.name}:\n'
            currentNode += f'\tdef __init__(self, *rest):\n'
            currentNode += f'\t\tself.rest = rest\n'
            currentNode += f'\tdef translate(self):\n'
            currentNode += f'\t\ttoReturn = []\n'
            currentNode += f'\t\tfor i in self.rest:\n'
            currentNode += f'\t\t\ttry:\n'
            currentNode += f'\t\t\t\ttoReturn.append(i.translate())\n'
            currentNode += f'\t\t\texcept AttributeError:\n'
            currentNode += f'\t\t\t\ttoReturn.append(i)\n'
            currentNode += f'\t\treturn toReturn\n'
            # currentNode += f'\t\treturn self.rest\n'
        else:
            for ind,translation in enumerate([x.action for x in rule.rhs.alts if x.action != None]):
                # print(translation)
                currentNode += f'class {rule.name}{ind}:\n'
                currentNode += f'\tdef __init__(self, *rest):\n'
                currentNode += '\t\tself.rest = rest\n'
                currentNode += f'\tdef translate(self):\n'
                currentNode += f"\t\treturn tr.translation_parser('{translation}', *self.rest).parse()\n"
        nodeClasses += currentNode

        currentMethod = ""
        currentMethod += f"\t{'@memoize_left_rec' if rule.left_recursive else '@memoize'}\n"
        currentMethod += f'\tdef {rule.name}(self):\n'
        currentMethod += rule.rhs.to_rule(varnum, False)
        currentMethod += '\t\treturn None\n'

        parserClass += currentMethod

    output = ""
    output += f"from parser import memoize, memoize_left_rec, Parser\n"
    output += "import translate as tr\n"
    output += nodeClasses
    output += "class ToyParser(Parser):\n"
    output += parserClass
    
    return output
    # with open(output_file_name, "w") as fi:
    #     fi.write(output)

# generate_parser("./grammars/translation/python.grm")