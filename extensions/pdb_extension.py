top_content = """
import pdb
"""
extension = """
import_stmt:
    | '$' { "pdb.set_trace()" }

"""

keywords = [
  "'$'",
]
