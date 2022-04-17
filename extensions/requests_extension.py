top_content = """
import requests
"""
extension = """
expression:
    | 'get' '(' atom ')' { "requests.get("_a ")"}
"""

keywords = [
  "'get'",
]
