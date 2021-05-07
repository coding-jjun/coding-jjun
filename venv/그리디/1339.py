n = int(input())
x = [0 for _ in range(10)]
for _ in range(n):
    p = input()
    l = len(p)
    k = len(p)
    while l != 0:
        x[ord(p[len(p)-l])-65] += 10 ** (l-1)
        l -= 1
x.sort()
c = 0
for i in range(10):
    c += i*x[i]
print(c)