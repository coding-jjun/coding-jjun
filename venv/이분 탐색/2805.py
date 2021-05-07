import sys
input = sys.stdin.readline
n, m = list(map(int, input().split()))
array = list(map(int, input().split()))
start = 0
end = max(array)
result = 0
while start <= end:
    mid = (start+end)//2
    total = sum(i-mid if i > mid else 0 for i in array)
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)

#가장 빠르고 간결한 풀이
import sys
from collections import Counter
r=sys.stdin.readline
N,M=map(int,r().split())
woods=Counter(map(int,r().split()))
def cnt_wood(woods, h):
    tmp=0
    for wood,cnt in woods.items():
        if wood>h:
            tmp+=(wood-h)*cnt
    return tmp
lo,hi=0,max(woods)
while lo <= hi:
    mid = (lo+hi)//2
    wood=cnt_wood(woods,mid)
    if wood >=M:
        result = mid
        lo = mid + 1
    else:
        hi = mid -1
print(result)

