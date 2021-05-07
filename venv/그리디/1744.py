import heapq
import sys
input = sys.stdin.readline
n = int(input())
x = []
y = []
c = 0
for i in range(n):
    t = int(input())
    if t <= 0:
        heapq.heappush(y, t)
    if t > 0:
        heapq.heappush(x, t)

l = len(x)
m = len(y)
h = heapq.heappop
def e(t):
    return h(t)*h(t)
o = x.count(1)
k = l-o

for i in range(o):
    c += h(x)
if k%2 == 0:
    for i in range(k//2):
        c += e(x)
else:
    c += h(x)
    for i in range(k//2):
        c += e(x)
if m%2 == 0:
    for i in range(m//2):
        c += e(y)
else:
    for i in range(m//2):
        c += e(y)
    c += h(y)

print(c)