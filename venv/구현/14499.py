import sys
input = sys.stdin.readline
n, m, x, y, k = map(int, input().split())
mapp = []
for i in range(n):
    mapp.append(list(map(int, input().split())))
command = list(map(int, input().split()))
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0]
def move(g):
    A = dice[0]
    B = dice[1]
    C = dice[2]
    D = dice[3]
    E = dice[4]
    F = dice[5]
    if g == 1:
        dice[0] = B
        dice[1] = F
        dice[2] = A
        dice[3] = D
        dice[4] = E
        dice[5] = C
    elif g == 2:
        dice[0] = C
        dice[1] = A
        dice[2] = F
        dice[3] = D
        dice[4] = E
        dice[5] = B
    elif g == 3:
        dice[0] = D
        dice[1] = B
        dice[2] = C
        dice[3] = F
        dice[4] = A
        dice[5] = E
    elif g == 4:
        dice[0] = E
        dice[1] = B
        dice[2] = C
        dice[3] = A
        dice[4] = F
        dice[5] = D

for i in range(k):
    nx = x + dx[command[i]-1]
    ny = y + dy[command[i]-1]
    if nx >= n or nx < 0 or ny >= m or ny < 0:
        continue
    else:
        x = nx
        y = ny
        move(command[i])
        v = dice[0]
        w = mapp[x][y]
        if w == 0:
            mapp[x][y] = v
        else:
            dice[0] = w
            mapp[x][y] = 0
        print(dice[5])