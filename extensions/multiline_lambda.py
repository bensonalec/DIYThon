top_content = """
"""
extension = """
lambdef: 'lambda' [lambda_params] ':' ( expression )*  { "lambda " OPTIONAL _a ENDOPTIONAL " : " STARTLOOP _b ENDLOOP }
"""

keywords = [
]
