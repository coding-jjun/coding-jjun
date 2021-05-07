n = int(input())
y = [0 for _ in range(26)]
for _ in range(n):
    p = input()
    l = len(p)
    for j in range(l):
        y[ord(p[j])-65] += 10 ** (l-j-1)
y.sort()
y.reverse()
c = 0
for i in range(10):
    c += (9-i)*y[i]
print(c)