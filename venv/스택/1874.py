import sys
input = sys.stdin.readline
n = int(input())
s = []
op = []
count = 1
temp = True

for i in range(n):
    num = int(input())
    while count <= num:
        s.append(count)
        op.append('+')
        count +=1
    if s[-1]==num:
        s.pop()
        op.append('-')
    else:
        temp=False
if temp==False:
    print('N0')
else:
    for j in op:
        print(j)
