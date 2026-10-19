class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()

    def top(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

n = int(input())
ls = list(map(int, input().split()))

num_ls = []
for i in range(1, n+1):
    num_ls.append(i)

result_nums = num_ls.copy()

s_tupik = Stack()
s_put2 = Stack()

for el in ls:
    s_tupik.push(el)
    while not s_tupik.is_empty() and s_tupik.top() == num_ls[0]:
        s_put2.push(s_tupik.pop())
        num_ls.pop(0)

if s_put2.items == result_nums:
    print("YES")
else:
    print("NO")