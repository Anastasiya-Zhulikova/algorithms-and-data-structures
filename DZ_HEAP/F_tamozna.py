#t - время прибытия груза
#l - время на обработку груза
#нужно найти минимальное количество аппаратов
#чтобы каждый из грузов досматривался в момент прибытия

import heapq

n = int(input())
ls = []
for _ in range(n):
    t, l = map(int, input().split())
    ls.append([t, l])
ls.sort()
#print(ls)

H = []
#в куче будет храниться время от начала,
#когда закончит работать аппарат
time = 0
mx_cnt = 0

for i in range(n):
    if len(H) == 0:
        heapq.heappush(H, ls[i][0]+ls[i][1])
    else:
        time = heapq.heappop(H)
        if time <= ls[i][0]:
            heapq.heappush(H, ls[i][0]+ls[i][1])
        else:
            heapq.heappush(H, time)
            heapq.heappush(H, ls[i][0]+ls[i][1])

    if mx_cnt < len(H):
        mx_cnt = len(H)
print(mx_cnt)