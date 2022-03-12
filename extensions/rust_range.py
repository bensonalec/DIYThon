extension = """
list:
    | '[' NUMBER '...' NUMBER ']' { "range(" _a "," _b ")" }
"""

keywords = [
    "'...'",
]