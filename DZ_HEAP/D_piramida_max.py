import heapq

#индексация с нуля
#pop возвращает минимум

H = []

while True:
    try:
        command = input()
        if command == "CLEAR":
            H = []
        elif command[:3] == "ADD":
            el = (-1) * int(command[4:])
            heapq.heappush(H, el)
        elif command == "EXTRACT":
            if len(H) == 0:
                print("CANNOT")
            else:
                print((-1) * heapq.heappop(H))
    except EOFError:
        break