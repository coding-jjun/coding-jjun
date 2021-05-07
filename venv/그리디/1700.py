import heapq
import sys
from collections import deque
input=sys.stdin.readline
n, k = map(int, input().split()) # n : 멀티탭 구멍의 개수, k : 전기용품의 총 사용 횟수
x = deque(list(map(int, input().split()))) # 전기용품의 사용순서
c = 0 # 플러그를 뽑는 횟수
s = set([])
while x:
    X = list(x)
    l = list(s)
    if len(s) < n:
        s.add(X[0])
        x.popleft()
        continue
    else:
        if X[0] in s:
            x.popleft()
            continue
        else:
            t = 0
            for j in l:
                if not j in X:
                    s.remove(j)
                    c += 1
                    t += 1
                if t == 1:
                    break
            if t == 0:
                s.remove(max(l, key=lambda i: X.index(i)))
                c += 1
            s.add(X[0])
            x.popleft()

print(c)
