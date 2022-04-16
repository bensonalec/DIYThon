top_content = """
"""

extension = """
list:
    | '[' NUMBER '...' NUMBER ']' { "range(" _a "," _b ")" }
"""

keywords = [
    "'...'",
]