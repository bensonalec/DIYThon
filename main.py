extension_files = ["./extensions/rust_range.py", "./extensions/true_false.py"]
target_file = "test_input.py"
output_file = "test_output.py"
core_grammar = "./grammars/translation/python.grm"
extension_plain = []
extension_keywords = []
for i in extension_files:
    with open(i) as fi:
        exec(fi.read())
        extension_keywords.extend(keywords)
        extension_plain.append(extension)
#Generate new keywords for use
from keywords import keywords
total_keywords = keywords+ extension_keywords
keyword_string = 'keywords = ["' + '","'.join(total_keywords) + '"]'
with open("gen_keywords.py", "w") as fi:
    fi.write(keyword_string)
#Generate parser for core grammar, store as string
from parser_gen_main import build_parser, generate_parser, build_parser_from_string
import sccutils 
final_grammar_string = ""
with open(core_grammar) as fi:
    final_grammar_string = fi.read()
primary_rules, current_synth_num = build_parser_from_string(final_grammar_string)
extensions_rules = []
for i in extension_plain:
    tmp_rules, current_synth_num = build_parser_from_string(i, current_synth_num)
    extensions_rules.append(tmp_rules)

for i in extensions_rules:
    for key, value in i.items():
        if key in primary_rules:
            #merge
            primary_rules[key].rhs.alts.extend(value.rhs.alts)
        else:
            print(key)
            primary_rules[key] = value
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
exec(final_output)
# with open(output_file, "w") as fi:
#     fi.write(final_output)