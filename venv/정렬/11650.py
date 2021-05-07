import heapq
import sys
input = sys.stdin.readline
n = int(input())
x = []
for i in range(n):
    a, b=map(int, input().split())
    heapq.heappush(x, [a, b])
for i in range(n):
    k = heapq.heappop(x)
    print(k[0], k[1])