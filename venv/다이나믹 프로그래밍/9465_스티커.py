import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    n = int(input())
    sticker = []
    for _ in range(2):
        sticker.append(list(map(int, input().split())))
