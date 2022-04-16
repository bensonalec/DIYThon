top_content = """
"""

extension = """
atom:
    | 'True' { "True" }
    | 'False' { "False" }
    | 'false' { "False" }
    | 'true' { "True" }
"""

keywords = [
    "'false'",
    "'true'",
]