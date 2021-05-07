n, k = list(map(int, input().split()))
array=[]
for i in range(n):
    array.append(int(input()))
start = 1
end = max(array)

result = 0
while(start <= end ):
    total = 0
    mid = (start+end)//2
    for x in array:
        if x >= mid:
            total += x//mid
    if total < k:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)

#가장빠르고간결한풀이
from sys import stdin
K, N = map(int,stdin.readline().split())
li = list(map(int,stdin.readlines()))
h, l = sum(li)//N, 1
while l <= h :
    mid = (h+l)//2
    cnt = sum([x//mid for x in li])
    if cnt < N:
        h = mid - 1
    elif cnt >= N:
        l = mid + 1
        ans = mid
print(ans)