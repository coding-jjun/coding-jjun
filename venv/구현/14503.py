n, m = map(int, input().split())
x, y, d = map(int, input().split())
visited = [[0]*m for _ in range(n)]
visited[x][y] = 1
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3
c = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]
    if visited[nx][ny] == 0 and graph[nx][ny] == 0:
        visited[nx][ny] = 1
        x = nx
        y = ny
        c += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if graph[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
print(c)