import math
import sys
input = sys.stdin.readline
n, m, b = map(int, input().split())
just = [] #높이들의 집합
height = [0] * 257
for i in range(n):
    just += list(map(int, input().split()))
for i in range(n*m):
    height[just[i]] += 1
h = sum(just)
s = list(set(just))
s.sort()
infi = math.inf
def time_cal(x):
    t = 0
    if int(x)*n*m > h+b:
        return infi
    for i in range(257):
        if x >= i:
            t += (x-i)*height[i]
        else:
            t += 2*(i-x)*height[i]
    return t
mini = time_cal(s[0])
for i in range(min(s), max(s)+1):
    if time_cal(i) < mini:
        mini = time_cal(i)
li = []
for i in range(min(s), max(s)+1):
    if time_cal(i) == mini:
        li.append(i)
print(mini, max(li))