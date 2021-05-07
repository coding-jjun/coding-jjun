n, k = map(int, input().split())
L =[]
for i in range(1, n+1):
    L.append(i)
c = 0
x = []
t = 0
while c < n:
    c+=1
    l=len(L)
    t = (t + (k-1))%l
    x.append(L.pop(t))
print('<', end='')
print(str(x)[1:-1], end='')
print('>', end='')
