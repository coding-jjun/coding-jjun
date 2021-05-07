import sys
input = sys.stdin.readline
n = int(input())
N = list(map(int, input().split()))
m = int(input())
M = list(map(int, input().split()))
N.sort()

def search_front(num, start, end):
    while (end > start):
        mid = (start+end)//2
        if N[mid] >= num:
            end = mid
        else:
            start = mid + 1
    return end

def search_back(num, start, end):
    if N[n-1] == num:
        return n
    while (end > start):
        mid = (start + end)//2
        if N[mid] > num:
            end = mid
        else:
            start = mid + 1
    return end

for a in M:
    back = search_back(a, 0, n-1)
    front = search_front(a, 0, n-1)
    if back - front == 0 and N[back] != a:
        print(0, end=' ')
    else:
        print(back-front, end=' ')

#가장 빠르고 간결한 풀이
import sys
r = sys.stdin.readline
from collections import Counter
_, c, _ = r(), Counter(r().split()), r()
print(' '.join(str(c[m]) if m in c else '0' for m in r().split()))