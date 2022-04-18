# [[inner_consumer(row_val, col_val) for row_val in inner_producer()] for col_val in outer_producer()]
# A = ((inner_producer),(outer_producer):(inner_consumer))
top_content = """
"""

extension = """
listcomp:
    | '(' '(' NAME ')' ',' '(' NAME ')' ':' '(' NAME ')' ')' { "[[" _c "((row_val, col_val)) for row_val in " _b"] for col_val in " _a "]" }
"""

keywords = [
]