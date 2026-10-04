from random import randint

n = int(input())
arr_1 = list(map(int, input().split()))
m = int(input())
arr_2 = list(map(int, input().split()))

#1. Отсортирую списки через quick_sort
def quick_sort(arr, left, right):
    if left < right:
        val = arr[randint(left, right)]
        l, r = left, right
        while l <= r:
            while arr[l] < val:
                l += 1
            while arr[r] > val:
                r -= 1
            if l <= r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
        if left < r:
            quick_sort(arr, left, r)
        if right > l:
            quick_sort(arr, l, right)
    return arr

#2. Найду начальное и конечное одинаковое число
def first_bin_search(arr, x):
    l = -1
    r = len(arr)
    while r - l > 1:
        m = (l + r) // 2
        if arr[m] >= x:
            r = m
        else:
            l = m
    if r == len(arr) or arr[r] != x:
        return -1
    return r

def last_bin_search(arr, x):
    l = -1
    r = len(arr)
    while r - l > 1:
        m = (l + r) // 2
        if arr[m] <= x:
            l = m
        else:
            r = m
    if l == -1 or arr[l] != x:
        return -1
    return l

cnt_arr = []

arr_1 = quick_sort(arr_1, 0, n-1)

for el in arr_2:
    first_ind = first_bin_search(arr_1, el)
    last_ind = last_bin_search(arr_1, el)
    if first_ind == -1 or last_ind == -1:
        cnt_arr.append(0)
    else:
        cnt_arr.append(last_ind - first_ind + 1)

print(*cnt_arr)