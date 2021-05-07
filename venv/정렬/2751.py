import sys
input = sys.stdin.readline
n = int(input())
a=[]
for i in range(n):
    a.append(int(input()))
a.sort()
for i in range(n):
    print(a[i])


# 조금 더 빠르고 간결한 풀이
import sys
n = int(sys.stdin.readline())
a = sorted(list(map(int,sys.stdin.read().split())))
print('\n'.join(map(str,a)))