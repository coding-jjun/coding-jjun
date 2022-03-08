import sys
input = sys.stdin.readline
x = []
n = int(input())
for _ in range(n):
    x.append(int(input()))
s = list(set(x))
s.sort()
x.sort()
t = []
c = 1

print(round(sum(x)/n))
print(x[n//2])
if n == 1:
    print(x[0])
else:
    for i in range(1, len(x)):
        if x[i] == x[i-1]:
            c += 1
            if i == len(x) -1:
                t.append(c)
        else:
            t.append(c)
            c = 1
    if t.count(max(t)) >= 2:
        k = t.index(max(t))
        t.pop(k)
        s.pop(k)
        print(s[t.index(max(t))])
    else:
        print(s[t.index(max(t))])
print(max(x)-min(x))