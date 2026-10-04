n, k = map(int, input().split())
arr_1 = list(map(int, input().split())) #n
arr_2 = list(map(int, input().split())) #k

#ИДЕЯ: число может быть ближайшим либо больше данного, либо меньше.
#Значит, ищем по одному числу с каждой стороны и сравниваем разницу с исходным.
#Последнее число <= x
#Первое число => x

def last_bin_search(arr, x):
    l = -1
    r = len(arr)
    while r - l > 1:
        m = (l + r) // 2
        if arr[m] <= x:
            l = m
        else:
            r = m
    return l

def first_bin_search(arr, x):
    l = -1
    r = len(arr)
    while r - l > 1:
        m = (l + r) // 2
        if arr[m] >= x:
            r = m
        else:
            l = m
    if r == len(arr):
        return -1
    return r

#Прошлись по каждому, нашли два числа, сравнили, вывели
for x in arr_2:
    ind_1 = last_bin_search(arr_1, x)
    ind_2 = first_bin_search(arr_1, x)
    if (ind_1 == -1) and (ind_2 != -1):
        print(arr_1[ind_2])
    elif (ind_1 != -1) and (ind_2 == -1):
        print(arr_1[ind_1])
    else:
        if abs(x - arr_1[ind_1]) <= abs(x - arr_1[ind_2]):
            print(arr_1[ind_1])
        else:
            print(arr_1[ind_2])