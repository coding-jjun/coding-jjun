import sys
input = sys.stdin.readline
n = int(input())
X = []
for i in range(n):
    o = input().rstrip()
    if o[:4] == 'push':
        X.append(o[5:])
    elif o == 'pop':
        if len(X) == 0:
            print(-1)
        else:
            print(X.pop())
    elif o == 'size':
        print(len(X))
    if o == 'empty':
        if len(X) == 0:
            print(1)
        else:
            print(0)
    if o == 'top':
        if len(X) == 0:
            print(-1)
        else:
            print(X[len(X)-1])