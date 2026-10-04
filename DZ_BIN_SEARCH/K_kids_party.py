#m шариков всего
#n человек
#время одного, количество, отдых

def good(arr, m, n, center_time):
    all_balls = 0
    for ls in arr:
        balls = 0
        #Время одного цикла
        one_cycle = ls[0] * ls[1] + ls[2]
        #Время всех циклов
        all_cycles = center_time // one_cycle
        #За каждый цикл он надувает ls[1] штук
        balls += all_cycles * ls[1]
        #Если осталось свободное время, он может ещё надуть шарики
        free_time = center_time % one_cycle
        if free_time >= ls[0]:
            #Если вдруг шариков будет больше, чем нужно до отдыха,
            #   то минимум вернет до максимально возможного надутия за работу
            balls += min(free_time // ls[0], ls[1])  #Если не успеет до отдыха
        ls[3] = balls
        all_balls += balls
    return all_balls >= m

m, n = map(int, input().split())
arr = []
for ls in range(n):
    arr.append([])
    arr[ls] = list(map(int, input().split()))
    arr[ls].append(0)

l = -1
r = 10**9
while r - l > 1:
    center_time = (l + r) // 2
    if good(arr, m, n, center_time):
        r = center_time
    else:
        l = center_time
print(r)

#Чтобы получить конкретные надутые шарики
good(arr, m, n, r)

#Так как шариков может быть больше, лишние нужно выкинуть
all_balls = []
balls = 0
for ls in arr:
    if balls + ls[3] <= m:
        all_balls.append(ls[3])
        balls += ls[3]
    else:
        all_balls.append(m-balls)
        balls += m-balls

print(*all_balls)
