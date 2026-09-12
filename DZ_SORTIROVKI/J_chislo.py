from sys import stdin

def str_sort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] + arr[j+1] < arr[j+1] + arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

arr = [el.strip() for el in stdin]

print(*["".join(el for el in str_sort(arr))])