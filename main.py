extension_files = ["./extensions/optional_access.py", "./extensions/rust_range.py", "./extensions/true_false.py", "./extensions/pdb_extension.py", "./extensions/multiline_lambda.py"]
target_file = "test_input.py"
output_file = "test_output.py"
core_grammar = "./grammars/translation/python.grm"
extension_plain = []
extension_keywords = []
top_contents = ""
for i in extension_files:
    with open(i) as fi:
        exec(fi.read())
        extension_keywords.extend(keywords)
        extension_plain.append(extension)
        top_contents += top_content
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
    # print(i)
    tmp_rules, current_synth_num = build_parser_from_string(i, current_synth_num)
    extensions_rules.append(tmp_rules)

for i in extensions_rules:
    for key, value in i.items():
        if key in primary_rules:
            #merge
            for j in value.rhs.alts:
                primary_rules[key].rhs.alts.insert(0,j)
        else:
            # print(key)
            primary_rules[key] = value
#Generate final parser
for key, value in primary_rules.items():
    value.recalc_indexes()
    primary_rules[key] = value
# print(primary_rules["primary"])
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
    # for i in tokenGen:
    #     print(i)
    # exit()
    p = ToyParser(Tokenizer(tokenGen))
    gram = p.file()
final_output = gram.translate()
final_output = top_contents + final_output
#Output final translated input
print(final_output)
exec(final_output)
# with open(output_file, "w") as fi:
#     fi.write(final_output)