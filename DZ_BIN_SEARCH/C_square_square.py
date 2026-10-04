c = float(input())

eps = 10**(-6)
l = 1
r = 10**10
while r - l > eps:
    m = (l + r) / 2
    if m**2 + m**0.5 <= c:
        l = m
    else:
        r = m
print(round(l, 6))