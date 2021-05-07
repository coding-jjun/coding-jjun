n, k = map(int, input().split())
a = []
count = 0
for i in range(n):
    a.append(int(input()))
a.reverse()
for b in a:
    count += k//b
    k %= b
print(count)