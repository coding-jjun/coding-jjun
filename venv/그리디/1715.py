import heapq
import sys
n = int(sys.stdin.readline())
x = []
c = 0
for _ in range(n):
    heapq.heappush(x, int(input()))

for _ in range(n-1):
    a = heapq.heappop(x) + heapq.heappop(x)
    c += a
    heapq.heappush(x, a)
print(c)