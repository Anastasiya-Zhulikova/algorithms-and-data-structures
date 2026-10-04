def bin_search(arr, x):
    l = -1
    r = len(arr)
    while r - l > 1:
        m = (l + r) // 2
        if arr[m] < x:
            l = m
        else:
            r = m
    if r == len(arr) or arr[r] != x:
        return "NO"
    return "YES"

n, k = map(int, input().split())
arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))

for x in arr_2:
    print(bin_search(arr_1, x))