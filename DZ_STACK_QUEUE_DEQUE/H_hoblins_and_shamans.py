from collections import deque


goblins = []
n = int(input())
while True:
    try:
        goblins.append(input())
    except EOFError:
        break

left_q = deque()
right_q = deque()
for goblin in goblins:
    if goblin[0] == "+":
        right_q.append(goblin[2:])
    elif goblin[0] == "*":
        right_q.appendleft(goblin[2:])
    elif goblin[0] == "-":
        print(left_q.popleft())

    #В правой слишком много
    if len(left_q) < len(right_q):
        left_q.append(right_q.popleft())