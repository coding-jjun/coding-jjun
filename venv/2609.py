a, b = map(int, input().split())
A, B = [], []
i = 2
r = int(a**0.5)
while i <= r:
    while not a%i:
        A.append(i)
        a /= i
    i += 1
if a > 1:
    A.append(a)
j = 2
s = int(b**0.5)
while j <= s:
    while not b%j:
        B.append(j)
        b /= j
    j += 1
if b > 1:
    B.append(b)
sa = set(A)
sb = set(B)
si = list(sa & sb)
su = list(sa | sb)
x = 1
for i in range(len(si)):
    x *=si[i]**min(A.count(si[i]), B.count(si[i]))
y = 1
for i in range(len(su)):
    y *= su[i]**max(A.count(su[i]), B.count(su[i]))
print(int(x))
print(int(y))