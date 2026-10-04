#Нужно найти число, равное x

a, b, c, d = map(int, input().split())

eps = 10**(-4)
l = -1_000_000
r = 1_000_000

while r - l > eps:
    m = (l + r) / 2
    uslovie = a * m**3 + b * m**2 + c * m + d
    if a > 0:
        if uslovie <= 0:
            l = m
        else:
            r = m
    else:
        if uslovie >= 0:
            l = m
        else:
            r = m
print(round(l, 4))