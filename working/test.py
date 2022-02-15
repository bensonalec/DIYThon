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

#code to generate parser
#TODO: Finish implementing to_rules for all appropriate nodes
# Repeat 0
# Repeat 1
# Lookaheads
#TODO: Build translation generation infra
# NOTE: For now, get this as simple as OG version
varnum = 0
for _, rule in rules:
    variables = []
    tokenInfos = []
    currentMethod = ""
    currentMethod += f"\t{'@memoize_left_rec' if rule.left_recursive else '@memoize'}\n"
    currentMethod += f'\tdef {rule.name}(self):\n'
    currentMethod += rule.rhs.to_rule(varnum, False)
    currentMethod += '\t\treturn None\n'

    print(currentMethod)
