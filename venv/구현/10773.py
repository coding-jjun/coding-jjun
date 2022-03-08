import sys
input = sys.stdin.readline
n = int(input())
x = []
for i in range(n):
    k = int(input())
    if k == 0:
        x.pop()
    else:
        x.append(k)
print(sum(x))