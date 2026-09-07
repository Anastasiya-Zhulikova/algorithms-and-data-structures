def counter_sort(arr):
    k = max(arr)
    counter = [0] * (k+1)
    for el in arr:
        counter[el] += 1
    arr.clear()
    for el in range(k+1):
        arr = arr + [el] * counter[el]
    return arr

arr = list(map(int, input().split()))
print(*counter_sort(arr))
