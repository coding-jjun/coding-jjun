from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
q = deque()
for i in range(n):
    o = input().rstrip()
    if o[:10] == 'push_front':
        q.reverse()
        q.append(o[11:])
        q.reverse()
    elif o[:9] == 'push_back':
        q.append(o[10:])
    elif o[:9] == 'pop_front':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif o[:8] == 'pop_back':
        if len(q) == 0:
            print(-1)
        else:
            q.reverse()
            print(q.popleft())
            q.reverse()
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