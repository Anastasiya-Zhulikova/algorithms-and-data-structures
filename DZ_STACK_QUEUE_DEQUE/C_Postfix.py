# s = input().split()
# stack = []
#
# for c in s:
#     if c not in "+-*":
#         stack.append(c)
#         continue
#     else:
#         b = int(stack.pop())
#         a = int(stack.pop())
#         if c == "+":
#             stack.append(a + b)
#         if c == "-":
#             stack.append(a - b)
#         if c == "*":
#             stack.append(a * b)
#
# print(stack[0])

s = input().split()
stack = []

oper = {"+": lambda x, y: x+y,
        "-": lambda x, y: x-y,
        "*": lambda x, y: x*y}

for c in s:
    if c not in oper.keys():
        stack.append(int(c))
    else:
        b, a = stack.pop(), stack.pop()
        stack.append(oper[c](a, b))

print(stack[0])