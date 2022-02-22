with open("test_input.py") as fi:
    tokenGen = generate_tokens(fi.readline)
    for i in tokenGen:
        print(i)
    p = ToyParser(Tokenizer(tokenGen))
    gram = p.file()

# print(gram)

# i = gram
# def dive(i):
#         if type(i) == TokenInfo:
#             print("Base case")
#             print(i)
#             return
#         else:
#             if type(i) == list:
#                 for x in i:
#                     print(i)
#                     dive(x)
#                 return
#             i = i._a
#             print(i)
#             dive(i)
#             return
# # print(gram)
# # dive(i)