import heapq

#количество аквариумов
n = int(input())
aquariums = []
for _ in range(n):
    aquariums.append(int(input()))

H = []
igor_place = 0
time = 0

for i in range(n):
    heapq.heappush(H, (max(1000 - aquariums[i], 1), aquariums[i], i))

while True:
    birth_time, population, aqua_i = heapq.heappop(H)
    if birth_time < time + abs(igor_place - aqua_i):
        print(birth_time)
        break
    else:
        time = birth_time
        population += 1
        igor_place = aqua_i
        heapq.heappush(H, (time + max(1000 - population, 1), population, aqua_i))