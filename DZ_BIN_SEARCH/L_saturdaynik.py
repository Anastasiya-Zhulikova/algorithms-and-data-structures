def good(arr, n, r, c, m):
    cnt = 0
    i = 0
    while i <= n - c:
        if arr[i + c - 1] - arr[i] <= m:
            cnt += 1
            i += c
        else:
            i += 1
    return cnt >= r

n, r, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()

left = -1
right = 10**9
while right - left > 1:
    m = (left + right) // 2
    if good(arr, n, r, c, m):
        right = m
    else:
        left = m
print(right)