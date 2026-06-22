token = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# class Solution:
#     def evalRPN(self, tokens: list[str]) -> int:
#         l = len(tokens)
#         stack = []
#         for i in tokens:
#             if i.isdigit():
#                 stack.append(int(i))
#                 continue
#             operation = i
#             a = stack[-1]
#             b = stack[-2]
#             stack.pop()
#             stack.pop()
#
#             if operation == "+": stack.append(a+b)
#             elif operation == "-": stack.append(a-b)
#             elif operation == "*": stack.append(a*b)
#             elif operation == "/": stack.append(a//b)
#
#         return stack[0]
print("-11".isdigit())
