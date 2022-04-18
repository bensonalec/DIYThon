top_content = """
from joblib import Parallel, delayed
"""

extension = """
for_stmt:
    | 'parralel' 'for' star_targets 'in' ~ star_expressions ':'  block { "def par_func(" _a "):" _c NEWLINE "Parallel(n_jobs=5)(delayed(par_func)(i) for i in " _b ")" } 
"""

keywords = [
    "'parralel'"
]