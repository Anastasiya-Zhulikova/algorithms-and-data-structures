class Heap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def shiftUp(self, i):
        while i // 2 > 0 and self.heap[i] > self.heap[i//2]:
            self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i = i//2

    def insert(self, el):
        self.heap.append(el)
        self.size += 1
        self.shiftUp(self.size)

    def indMaxChild(self, i):
        if 2*i+1 > self.size:
            return 2*i
        if self.heap[2*i] > self.heap[2*i+1]:
            return 2*i
        return 2*i+1

    def shiftDown(self, i):
        while 2*i <= self.size: # Пока есть хотя бы один сын (левый), то есть не упадём ниже пола
            j = self.indMaxChild(i) # Если мы будем менять местами с наибольшим ребенком, то он будет гарантированно большим, чем другой сын
            if self.heap[i] < self.heap[j]:
                self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
                i = j
            else:
                break

    def extract(self):
        if self.size == 0:
            return None
        else:
            removed = self.heap[1]
            self.heap[1] = self.heap[self.size]
            self.size -= 1
            self.heap.pop()
            self.shiftDown(1)
            return removed


heap = Heap()

n = int(input())
for _ in range(n):
    command = input()
    if command == "1":
        print(heap.extract())
    else:
        heap.insert(int(command[2:]))
