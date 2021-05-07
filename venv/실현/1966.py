from collections import deque
t = int(input())
for i in range(t):
    c = 0
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    x = deque()
    y = deque()
    for j in range(n):
        x.append(l[j])
        y.append(j)
    while True:
            if x[0] == max(list(x)):
                x.popleft()
                d = y.popleft()
                c += 1
                if d == k:
                    print(c)
                    break
                continue
            else:
                x.append(x.popleft())
                y.append(y.popleft())

