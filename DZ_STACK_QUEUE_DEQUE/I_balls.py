ls = list(map(int, input().split()))
n = ls[0]
colors = ls[1:]

#кортежи (цвет, количество подряд идущих)
stack = []
destroyed = 0

for ball in colors:
    if stack != [] and stack[-1][0] == ball:
        #Нашли тот же цвет - перезаписываем его с новым кол-вом
        c, cnt = stack.pop()
        stack.append((c, cnt + 1))
    else:
        #Уничтожаем (смотрим на кол-во)
        while stack != [] and stack[-1][1] >= 3:
            destroyed += stack.pop()[1]
        #Нашли тот же цвет - перезаписываем его с новым кол-вом
        if stack != [] and stack[-1][0] == ball:
            c, cnt = stack.pop()
            stack.append((c, cnt + 1))
        else:
            stack.append((ball, 1))

#Остаток (если последнее, что придет, совпало по цвету)
while stack and stack[-1][1] >= 3:
    destroyed += stack.pop()[1]

print(destroyed)