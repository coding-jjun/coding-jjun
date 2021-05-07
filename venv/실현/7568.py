n =int(input())
x = []
for i in range(n):
    x.append(list(map(int, input().split())))

for i in range(n):
    c = 1
    v = x[0]
    x.pop(0)
    for j in x:
        if v[0] < j[0] and v[1] < j[1]:
            c += 1
    x.append(v)
    print(c)