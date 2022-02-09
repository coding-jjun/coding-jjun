import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for i in range(N+1)]
visit = [0 for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
connection = 0
def dfs(graph, start, visit):
    visit[start] = 1
    for i in graph[start]:
        if visit[i] == 0:
            dfs(graph, i, visit)
    return 0
for i in range(1, N + 1):
    if visit[i] == 0:
        connection += 1
        dfs(graph, i, visit)
print(connection)