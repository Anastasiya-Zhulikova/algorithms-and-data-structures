from collections import deque

first = deque(map(int, input().split()))
second = deque(map(int, input().split()))

cnt = 0

while first and second and cnt < 10**6:
    #Из начала берем по карте
    a = first.popleft()
    b = second.popleft()
    cnt += 1

    # 0 бьёт 9
    #Если у первого карта круче, он забирает себе карты (в конец)
    if a == 0 and b == 9:
        first_wins = True
    elif a == 9 and b == 0:
        first_wins = False
    else:
        first_wins = a > b

    if first_wins:
        first.append(a)
        first.append(b)
    else:
        second.append(a)
        second.append(b)

if not first:
    print("second", cnt)
elif not second:
    print("first", cnt)
else:
    print("botva")