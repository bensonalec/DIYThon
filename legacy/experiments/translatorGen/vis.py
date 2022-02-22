from rich.console import Console
import time
from rich.panel import Panel
from std import Tokenizer
from tokenize import generate_tokens
from out import ToyParser
import io
from rich.tree import Tree


console = Console()



console.print("Welcome to the Translation Explorer!")
x = console.input("[red]Enter a valid statement here:[/red] ")
x = io.StringIO(x)
tokenGen = generate_tokens(x.read)
p = ToyParser(Tokenizer(tokenGen))
gram = p.file()
print(gram)
tree = Tree("File")
tree.add("Sample")
console.print(tree)
# console.print(Panel("Here's some text!"))

# console.print(x)
