import sys
input=sys.stdin.readline
n, m = map(int, input().split())
c = list(map(int, input().split()))
ssum = []
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            ssum.append(c[i]+c[j]+c[k])
s = list(set(ssum))
k =[]
for i in s:
    if i <= m:
        k.append(i)
print(max(k))