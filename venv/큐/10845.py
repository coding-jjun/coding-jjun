from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
q = deque()
for i in range(n):
    o = input().rstrip()
    if o[:4] == 'push':
        q.append(o[5:])
    elif o == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif o == 'size':
        print(len(q))
    elif o == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif o == 'front':
        if len(q) ==0:
            print(-1)
        else:
            print(q[0])
    elif o == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])