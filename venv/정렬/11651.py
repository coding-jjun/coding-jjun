import sys
import heapq
input = sys.stdin.readline
x = []
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    heapq.heappush(x, [b, a])

for i in range(n):
    t = heapq.heappop(x)
    print(t[1], t[0])

#가장 빠르고 간결한 풀이
from sys import stdin, stdout

stdout.write(
    '\n'.join(
        f'{v % 1000000 - 100000} {v // 1000000 - 100000}'
        for v
        in sorted(
            (int(line.split()[1])+100000) * 1000000
            + int(line.split()[0])+100000
            for line in stdin.read().splitlines()[1:]
        )
    ) + '\n'
)
#두번째로 간결하고 빠른 풀이
import sys
input = sys.stdin.readline
coords = [input() for _ in range(int(input()))]
coords = sorted(coords, key = lambda coord: (int(coord.split()[1]), int(coord.split()[0])))

print(''.join(coords))