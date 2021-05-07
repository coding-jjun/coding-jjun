from collections import deque
import sys
q = deque()
input = sys.stdin.readline
n = int(input())
for i in range(1, n+1):
    q.append(i)
for _ in range(n-1):
    q.popleft()
    q.append(q.popleft())
print(str(q[0]))

# 가장 간결하고 빠른 풀이
n,s=int(input()),1
while s<n:
    s*=2
print(s if s==n else 2*n-s)