from random import randint

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    val = arr[randint(0, len(arr)-1)]
    left = [el for el in arr if el < val]
    center = [el for el in arr if el == val]
    right = list(filter(lambda el: el > val, arr))
    return quick_sort(left) + center + quick_sort(right)

n = int(input())
arr = list(map(int, input().split()))[:n]

print(*quick_sort(arr))