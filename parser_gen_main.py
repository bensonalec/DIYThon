from tokenize import generate_tokens
from tokenizer import Tokenizer
from grammar_parser import GeneratedParser
import sccutils 

#Todo, in order of high priority to low
#TODO: Get everything together for the IRB
#   Finish course
#   Actual paperwork
#   Describe the actual experiment, the extensions being implemented, and the questions asked
#TODO: Write the design and implementation part of the actual thesis
#TODO:Handle synthetic rules that should be passed input 

#TODO: Test that it can actually parse various files
#NOTE: For now will probably continue onwards, but it has trouble with various features:
#   NOTE: Item destructuring (i.e in an enumerated loop)
#   NOTE: Function input (2 or more input to a function)
#TODO: Improve translation infrastructure
#   Probably want something that can say "anything inside gets tabbed this much"
#   Implement some kind of "optional" part of the translation, this might be hard and more worth just rewriting the rule
#   Figure out how repitions can be caught and translated
#TODO: Get 2 sample extensions working
#TODO: Write appropriate translations for Python
#TODO: Implement Visualization Tool
def generate_parser(output_file_name, grammar):
    with open(grammar) as fi:
        tokenGen = generate_tokens(fi.readline)
        p = GeneratedParser(Tokenizer(tokenGen))
        gram = p.start()

    p.synthetic_rules = {rule.name: rule for rule in p.synthetic_rules}
    gram.rules = gram.rules |  p.synthetic_rules
    sccutils.compute_left_recursives(gram.rules)
    rules = gram.rules.items()

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
            currentNode += f'\t\treturn self.rest\n'
        else:
            for ind,translation in enumerate([x.action for x in rule.rhs.alts if x.action != None]):
                # print(translation)
                translation = translation.split(" ")
                variables = [x for x in translation if x.startswith('_')]
                currentNode += f'class {rule.name}{ind}:\n'
                currentNode += f'\tdef __init__(self, {", ".join([f"{x}" for x in variables])}{"," if len(variables) > 0 else ""} *rest):\n'
                for var in variables:
                    currentNode += f'\t\tself.{var} = {var}\n'
                currentNode += "\t\tpass\n"
                currentNode += f'\tdef translate(self):\n'
                currentNode += f'\t\treturn f"{"".join([f"{{self.{x}.translate() if type(self.{x}) != str else self.{x}}}" if x in variables else f"{{{x}}}" for x in translation])}"\n'
        nodeClasses += currentNode

        currentMethod = ""
        currentMethod += f"\t{'@memoize_left_rec' if rule.left_recursive else '@memoize'}\n"
        currentMethod += f'\tdef {rule.name}(self):\n'
        currentMethod += rule.rhs.to_rule(varnum, False)
        currentMethod += '\t\treturn None\n'

        parserClass += currentMethod

    output = ""
    output += f"from parser import memoize, memoize_left_rec, Parser\n"
    output += nodeClasses
    output += "class ToyParser(Parser):\n"
    output += parserClass

    with open(output_file_name, "w") as fi:
        fi.write(output)

generate_parser("out.py", "./grammars/translation/python.grm")