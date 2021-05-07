import sys
import heapq
input = sys.stdin.readline
n, k = map(int, input().split())
x, y, z = [], [], []
b, c = 0, 0
for _ in range(n):
    m, v = map(int, input().split())
    x.append([m, v])
x.sort(key= lambda x:x[0])
for _ in range(k):
    y.append(int(input()))
y.sort()
for a in y:
    while b < n and a >= x[b][0]:
        heapq.heappush(z, -x[b][1])
        b += 1
    if z:
        c -= heapq.heappop(z)
print(c)

