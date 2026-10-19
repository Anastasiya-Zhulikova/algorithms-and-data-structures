class Queue:
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
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            return "error"
        return self.items[0]

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

q = Queue()

for action in actions:
    if action[:4] == "push":
        n = action[5:]
        print(q.push(n))
    elif action == "pop":
        print(q.pop())
    elif action == "front":
        print(q.front())
    elif action == "size":
        print(q.size())
    elif action == "clear":
        print(q.clear())
    elif action == "exit":
        print(q.__exit__())
        break