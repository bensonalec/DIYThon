extension = """
atom:
    | NAME { _a } 
    | 'True' { "True" } 
    | 'False' { "False" }
    | 'true' { "True" }
    | 'false' { "False" }
    | 'None' { "None" }
    | strings { _a } 
    | NUMBER { _a } 
    | (tuple | group | genexp) { _a } 
    | (list | listcomp) { _a[0] } 
    | (dict | set | dictcomp | setcomp) { _a } 
    | '...' { "..." }
"""

keywords = [
    "'true'",
    "'false'",
]