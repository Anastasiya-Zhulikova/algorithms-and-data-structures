import heapq
import sys  #импортируем sys для быстрого ввода
input = sys.stdin.readline

#ширина w клеток
#n фигур шириной wi и высотой 1

n, w = map(int, input().split())
ls = []
for i in range(n):
    ai, wi = map(int, input().split())
    #кортежи весят меньше, чем списки, потому что они неизменяемые
    ls.append((ai, ai+wi, i+1))

#чтобы удобно было искать непересекающиеся блоки
ls.sort()

#все готовые уровни
all_levels = []

#куча хранит концы фигур и индекс уровня.
#так мы будем знать конец ближайшей фигуры
H = []

for ai, bi, i in ls:

    if H != [] and ai >= H[0][0]:
        last_bi, level_ind = H[0]

        all_levels[level_ind].append(i)  #добавляем фигуру на этот уровень
        last_bi = bi  #обновляем правую границу

        heapq.heapreplace(H, (last_bi, level_ind))  #возвращаем уровень в кучу
    else:
        #фигура пересекается, создаем новый уровень
        level_ind = len(all_levels)
        all_levels.append([i])

        last_bi = bi
        heapq.heappush(H, (last_bi, level_ind))  #добавляем новый уровень в кучу

del ls, H  #освобождаем память перед выводом

print(len(all_levels))  #количество получившихся уровней (высота)

#выводим по уровням, не собирая общий список order
for level in all_levels:
    sys.stdout.write(' '.join(map(str, level)) + ' ')
print()