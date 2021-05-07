import sys
input=sys.stdin.readline
n = int(input())
cnt = [0]*10001
for i in range(n):
    cnt[int(input())] += 1
for i in range(1, 10001):
    for j in range(cnt[i]):
        print(i)

#가장 빠르고 간결한 풀이
f = open(0)
f.readline()
li=[0]*10001
for line in f:
    li[int(line)] += 1

for i in range(1, 10001):
    print(f'{i}\n' * li[i], end='')