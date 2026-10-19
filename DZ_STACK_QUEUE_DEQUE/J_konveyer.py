n = int(input())

for _ in range(n):
    ls = input().split()
    k = int(ls[0])
    a = list(map(float, ls[1:]))

    #Чем меньше число - тем важнее в цех
    need_ceh = sorted(a)
    sklad = []           #склад
    real_ceh = 0         #сколько уже отдали в цех В
    i = 0                #указатель по ленте

    while real_ceh < k:
        if sklad != [] and sklad[-1] == need_ceh[real_ceh]:
            sklad.pop()
            real_ceh += 1
        elif i < k:
            if a[i] == need_ceh[real_ceh]:
                real_ceh += 1
                i += 1
            else:
                sklad.append(a[i])
                i += 1
        else:
            break

    if real_ceh == k:
        print(1)
    else:
        print(0)