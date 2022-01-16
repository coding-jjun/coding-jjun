import sys
import heapq
input = sys.stdin.readline
n, k = map(int, input().split()) # n : 보석의 개수, k : 가방의 개수
x, y, z = [], [], []
# x : 무게와 가격 정보를 담은 리스트
# y : 가방 리스트
# z : 가방이 담을 수 있는 보석들의 가격을 담은 리스트
b, c = 0, 0
for _ in range(n):
    m, v = map(int, input().split()) # m : 보석의 무게, v : 보석의 가격
    x.append([m, v])
x.sort(key= lambda x:x[0])
for _ in range(k):
    y.append(int(input()))
y.sort()
for a in y:
    while b < n and a >= x[b][0]:
        heapq.heappush(z, -x[b][1])
        b += 1
    if z:
        c -= heapq.heappop(z)
print(c)

