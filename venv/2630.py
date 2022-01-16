import sys
input = sys.stdin.readline
n = int(input())
paper = [[] for i in range(n)]
for i in range(n):
    paper[i] = list(map(int, input().split()))
