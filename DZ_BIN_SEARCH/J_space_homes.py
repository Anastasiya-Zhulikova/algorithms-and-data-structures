#Блоки влезут либо так |, либо так —
def good(n, a, b, w, h, d):
    a_d = (a + 2*d)
    b_d = (b + 2*d)
    return (((w//a_d) * (h//b_d)) >= n) or (((w//b_d) * (h//a_d)) >= n)

n, a, b, w, h = map(int, input().split())
#Берем заведомо маленькую и большую сторону
l = -1
r = 10**18

#Найдём последнее число, в которое влезут блоки
while r - l > 1:
    m = (l + r) // 2
    if good(n, a, b, w, h, m):
        l = m
    else:
        r = m
d = l
if l == -1:
    d = 0
print(d)