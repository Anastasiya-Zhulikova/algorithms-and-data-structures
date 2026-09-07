#Разделяют до одиночных/нулевых массивов, сравнивают и слепляют
#РЕКУРСИЯ

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    ind = len(arr) // 2
    left = arr[:ind]
    right = arr[ind:]
    return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i = i + 1
        else:
            res.append(right[j])
            j = j + 1
    res = res + left[i:] + right[j:]
    return res

arr = [9, 5, 0, 1, 9, 3, 6]
print(merge_sort(arr))