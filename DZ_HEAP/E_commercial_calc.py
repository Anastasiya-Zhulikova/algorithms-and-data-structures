import heapq

#5% от результата операции
#нужно найти минимальную стоимость

n = int(input())
H = []
money = 0

for el in map(int, input().split()):
    heapq.heappush(H, el)

while len(H) != 1:
    a = heapq.heappop(H)
    b = heapq.heappop(H)
    money += (a + b) * 0.05
    heapq.heappush(H, a+b)

print(money)