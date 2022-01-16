import sys
import heapq
input = sys.stdin.readline
N = int(input())
x, y, z, w = [], [], [], []
for i in range(N):
    s, f = map(int, input().split())
    x.append([s, f]) # 시작시간과 회의진행시간을 담은 리스트
    y.append([s, f]) # 시작시간과 끝나는 시간을 담은 리스트
    z.append([s, f])
    w.append([s, f-s])
x.sort(key = lambda x:x[1])
x.sort(key = lambda x:x[0])
z.sort(key = lambda z:z[0])
y.sort(key = lambda y:y[1])
w.sort(key = lambda w:w[0])
w.sort(key = lambda w:w[1])
end_time = y[0][1]
count = 1
print(x)
print(y)
print(z)
print(w)
# y를 y[0] 정렬 후 y[1]로 정렬