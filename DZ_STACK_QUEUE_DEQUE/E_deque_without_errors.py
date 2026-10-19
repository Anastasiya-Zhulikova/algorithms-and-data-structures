class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push_front(self, item):
        self.items = [item] + self.items
        return "ok"

    def push_back(self, item):
        self.items.append(item)
        return "ok"

    def pop_front(self):
        if self.is_empty():
            return "error"
        return self.items.pop(0)

    def pop_back(self):
        if self.is_empty():
            return "error"
        return self.items.pop(-1)

    def front(self):
        if self.is_empty():
            return "error"
        return self.items[0]

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

d = Deque()
for action in actions:
    if action[:10] == "push_front":
        n = action[11:]
        print(d.push_front(n))
    elif action[:9] == "push_back":
        n = action[10:]
        print(d.push_back(n))
    elif action == "pop_front":
        print(d.pop_front())
    elif action == "pop_back":
        print(d.pop_back())
    elif action == "front":
        print(d.front())
    elif action == "back":
        print(d.back())
    elif action == "size":
        print(d.size())
    elif action == "clear":
        print(d.clear())
    elif action == "exit":
        print(d.__exit__())
        break