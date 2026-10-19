# from collections import deque
#
# n, k = map(int, input().split())
# ls = list(map(int, input().split()))
#
# dq = deque()
# count = 0
# mn_in_window = 1_500_000
#
# for el in ls:
#     dq.append(el)
#     if el < mn_in_window:
#         mn_in_window = el
#     if len(dq) > k:
#         del_el = dq.popleft()
#         if del_el == mn_in_window:
#             mn_in_window = min(dq)
#     if len(dq) == k:
#         print(mn_in_window)





# n, k = map(int, input().split())
# ls = list(map(int, input().split()))
#
# for start in range(n-k+1):
#     print(min(ls[start:start+k]))




from collections import deque

n, k = map(int, input().split())
ls = list(map(int, input().split()))

dq = deque()   # пары (значение, индекс), значения возрастают

for i in range(n):
    while dq and dq[-1][0] >= ls[i]:
        dq.pop()
    dq.append((ls[i], i))
    if dq[0][1] <= i - k:
        dq.popleft()
    if i >= k - 1:
        print(dq[0][0])