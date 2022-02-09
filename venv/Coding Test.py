import heapq
import sys
input = sys.stdin.readline
N = int(input())
def doubleheap(a, b):
    global minheap
    global maxheap
    if a == 'I':
        heapq.heappush(minheap, b)
        heapq.heappush(maxheap, -b)
    elif a == 'D':
        if len(minheap) != 0:
            if b == -1:
                x = heapq.heappop(minheap)
                maxheap.remove(-x)
            if b == 1:
                x = heapq.heappop(maxheap)
                minheap.remove(-x)
    return 0
def finishheap():
    if len(minheap) == 0:
        print('EMPTY')
    elif len(minheap) == 1:
        x = heapq.heappop(heap)
        print(x, x)
    else:
        x = heapq.heappop(minheap)
        y = heapq.heappop(maxheap)
        print(-y, x)
for i in range(N):
    minheap = []
    maxheap = []
    t = int(input())
    for j in range(t):
        u, v = input().split()
        doubleheap(u, int(v))
    finishheap()