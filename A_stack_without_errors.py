class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, n):
        self.items.append(n)
        return "ok"

    def pop(self):
        if self.is_empty():
            return "error"
        return self.items.pop()

    def back(self):
        if self.is_empty():
            return "error"
        return self.items[-1]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []
        return "ok"

    def __exit__(self):
        return "bye"

actions = []
while True:
    try:
        actions.append(input())
    except EOFError:
        break

s = Stack()
for action in actions:
    if action[:4] == "push":
        n = action[5:]
        print(s.push(n))
    elif action == "pop":
        print(s.pop())
    elif action == "back":
        print(s.back())
    elif action == "size":
        print(s.size())
    elif action == "clear":
        print(s.clear())
    elif action == "exit":
        print(s.__exit__())
        break