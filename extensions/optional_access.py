top_content = """
def optional_access(primary, att):
    try:
        return primary.__dict__[att]
    except:
        return None
"""
extension = """
primary:
    | primary '?' '.' NAME { "optional_access("_a ", " QUOTE _b QUOTE ")" } 
"""

keywords = [
    "'?'"
]
