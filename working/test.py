from tokenize import generate_tokens
from tokenizer import Tokenizer
from grammar_parser import GeneratedParser
from typing import AbstractSet, Dict, IO, Iterator, List, Optional, Set, Text, Tuple
from grammar import Rule
import sccutils 

def make_first_graph(rules: Dict[str, Rule]) -> Dict[str, AbstractSet[str]]:
    """Compute the graph of left-invocations.

    There's an edge from A to B if A may invoke B at its initial
    position.

    Note that this requires the nullable flags to have been computed.
    """
    graph = {}
    vertices: Set[str] = set()
    for rulename, rhs in rules.items():
        graph[rulename] = names = rhs.initial_names()
        vertices |= names
    for vertex in vertices:
        graph.setdefault(vertex, set())
    return graph

def compute_left_recursives(
    rules: Dict[str, Rule]
) -> Tuple[Dict[str, AbstractSet[str]], List[AbstractSet[str]]]:
    graph = make_first_graph(rules)
    sccs = list(sccutils.strongly_connected_components(graph.keys(), graph))
    for scc in sccs:
        if len(scc) > 1:
            for name in scc:
                rules[name].left_recursive = True
            # Try to find a leader such that all cycles go through it.
            leaders = set(scc)
            for start in scc:
                for cycle in sccutils.find_cycles_in_scc(graph, scc, start):
                    # print("Cycle:", " -> ".join(cycle))
                    leaders -= scc - set(cycle)
                    if not leaders:
                        raise ValueError(
                            f"SCC {scc} has no leadership candidate (no element is included in all cycles)"
                        )
            # print("Leaders:", leaders)
            leader = min(leaders)  # Pick an arbitrary leader from the candidates.
            rules[leader].leader = True
        else:
            name = min(scc)  # The only element.
            if name in graph[name]:
                rules[name].left_recursive = True
                rules[name].leader = True
    return graph, sccs

with open("./grammars/translation/python.grm") as fi:
    tokenGen = generate_tokens(fi.readline)
    p = GeneratedParser(Tokenizer(tokenGen))
    gram = p.start()

p.synthetic_rules = {rule.name: rule for rule in p.synthetic_rules}
gram.rules = gram.rules |  p.synthetic_rules
compute_left_recursives(gram.rules)
rules = gram.rules.items()

#Todo, in order of high priority to low
#TODO: Test that it can actually parse various files
#NOTE: For now will probably continue onwards, but it has trouble with various features:
#   NOTE: Item destructuring (i.e in an enumerated loop)
#   NOTE: Function input (2 or more input to a function)
# Handle synthetic rules that should be passed input 
#TODO: Improve translation infrastructure
#   Probably want something that can say "anything inside gets tabbed this much"
#   Implement some kind of "optional" part of the translation, this might be hard and more worth just rewriting the rule
#   Figure out how repitions can be caught and translated
#TODO: Write appropriate translations for Python
#TODO: Get 2 sample extensions working
#TODO: Get everything together for the IRB
#   Finish course
#   Actual paperwork
#   Describe the actual experiment, the extensions being implemented, and the questions asked
#TODO: Write the design and implementation part of the actual thesis
#TODO: Implement Visualization Tool
varnum = 0
parserClass = ""
nodeClasses = ""
for _, rule in rules:
    variables = []
    tokenInfos = []
    currentNode = ""
    for ind,translation in enumerate([x.action for x in rule.rhs.alts if x.action != None]):
        translation = translation.split(" ")
        variables = [x for x in translation if x.startswith('_')]
        currentNode += f'class {rule.name}{ind if not rule.name.startswith("synthetic_rule_") else ""}:\n'
        currentNode += f'\tdef __init__(self, {", ".join([f"{x}" for x in variables])}{"," if len(variables) > 0 else ""} *rest):\n'
        for var in variables:
            currentNode += f'\t\tself.{var} = {var}\n'
        currentNode += "\t\tpass\n"
        currentNode += f'\tdef translate(self):\n'
        currentNode += f'\t\treturn f"{"".join([f"{{self.{x}.translate() if type(self.{x}) != str else self.{x}}}" if x in variables else f"{{{x}}}" for x in translation])}"\n'
    nodeClasses += currentNode
    currentNode = ""
    for translation in [x.action for x in rule.rhs.alts if x.rule_name.startswith("synthetic_rule")]:
        translation = ["_a"]
        variables = ["_a"]
        currentNode += f'class {rule.name}{"0" if not rule.name.startswith("synthetic_rule_") else ""}:\n'
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
output += f"import tokenize\n"
output += nodeClasses
output += "class ToyParser(Parser):\n"
output += parserClass

print(output)