#Read in extension file names, and target file name
extension_names = ["./extensions/rust_range.py", "./extensions/true_false.py"]
target_file = "test_input.py"
output_file = "test_output.py"
core_grammar = "./grammars/translation/python.grm"
#Generate new keywords for use
#Generate parser for core grammar, store as string
from parser_gen_main import build_parser, generate_parser
import sccutils 
primary_rules = build_parser(core_grammar)
#Generate parser for each extension

#Import all relevant parsers
#Combine parsers together
#Generate final parser
sccutils.compute_left_recursives(primary_rules)
rules = primary_rules.items()
parser = generate_parser(rules)
with open("out.py", "w") as fi:
    fi.write(parser)
#Run input file through final parser
from tokenize import generate_tokens
from tokenizer import Tokenizer
from out import ToyParser
with open(target_file) as fi:
    tokenGen = generate_tokens(fi.readline)
    p = ToyParser(Tokenizer(tokenGen))
    gram = p.file()
final_output = gram.translate()
#Output final translated input
with open(output_file, "w") as fi:
    fi.write(final_output)