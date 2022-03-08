import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
graph = [] # 그래프
fish = [0 for _ in range(7)] # 물고기의 크기와 위치 정보 저장하는 리스트
time = 0 # 시간
baby_shark = 2 # 아기 상어의 크기
for i in range(N):
    graph.append(list(map(int, input().split())))
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            if graph[i][j] == 9:
                P, Q= i, j
            else:
                k = graph[i][j]
                fish[k] += 1

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
def empty(k):
    can = True
    count = 0
    if k > 6:
        k = 7
    for i in range(1, k):
        count += fish[i]
    if count == 0:
        can = False
    return can

def distance(x, y, k):
    if not empty(k):
        return False
    visit = [[False] * N for _ in range(N)]
    queue = deque()
    Li = []
    queue.append((x, y, 0))
    while queue:
        if len(Li) > 4*(N-1):
            break
        x, y, time = queue.popleft()
        visit[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 0:
                    if visit[nx][ny] == False:
                        queue.append((nx, ny, time+1))
                else:
                    if graph[nx][ny] < k:
                        Li.append([time+1, nx, ny])
                    elif graph[nx][ny] == k:
                        if visit[nx][ny] == False:
                            queue.append((nx, ny, time+1))
    if Li:
        Li.sort()
        return Li[0]
    else:
        return False
eat = 0
while True:
    tmp = distance(P, Q, baby_shark)
    if not tmp:
        break
    else:
        graph[P][Q] = 0
        P = tmp[1]
        Q = tmp[2]
        eat += 1
        fish[graph[P][Q]] -= 1
        graph[P][Q] = 9
        if eat == baby_shark:
            eat = 0
            baby_shark += 1
        time += tmp[0]
print(time)