#Про структуры в Python подсмотрела, честно. Первый раз вижу, что они вообще есть.

from dataclasses import dataclass
from math import sqrt

@dataclass(frozen=True)
class Point:
    x: int
    y: int

n = int(input())
p_arr = []
for i in range(n):
    x, y = list(map(int, input().split()))
    p_arr.append(Point(x, y))

p_arr.sort(key=lambda p: sqrt(p.x**2 + p.y**2))

for p in p_arr:
    print(p.x, p.y)