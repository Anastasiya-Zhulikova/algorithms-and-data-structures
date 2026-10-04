#X деревьев всего
#Дмитрий A деревьев в день, каждый K день отдых
#Федор B деревьев в день, каждый M день отдых
#За сколько дней срубятся все деревья?

def good(a, k, b, m, x, d):
    #trees = (a * d) - (a * d // k) + (b * d) - (b * d // m)
    trees = a * (d - d // k) + b * (d - d // m)
    return trees >= x


a, k, b, m, x = map(int, input().split())
l = -1
r = 10**18 + 1
while r - l > 1:
    d = (l + r) // 2
    if good(a, k, b, m, x, d):
        r = d
    else:
        l = d
print(r)