import math
n = input()
x = []
for i in range(len(n)):
    x.append(int(n[i]))
y = []
for i in range(10):
    y.append(x.count(i))
y[6] = math.ceil((y[6] + y[9]) / 2)
y.pop(9)
print(max(y))
