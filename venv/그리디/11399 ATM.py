n = int(input())
l = list(map(int, input().split()))
l.sort()
t = 0
for i in range(n):
    t += sum(l[:i+1])
print(t)