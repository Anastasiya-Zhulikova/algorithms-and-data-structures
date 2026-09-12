distance = list(map(int, input().split()))
money = list(map(int, input().split()))

distance.sort()
money.sort(reverse=True)

summa = 0
for i in range(len(distance)):
    summa += distance[i] * money[i]

print(summa)