extension = """
list:
    | '[' [star_named_expressions] ']' { "[" OPTIONAL _a ENDOPTIONAL "]" }
    | '[' NUMBER '...' NUMBER ']' { "range(" _a "," _b ")" }
"""

keywords = [
    "'...'",
]