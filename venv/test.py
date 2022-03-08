import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
def rotate_90(arr, n, m):
    result = [[0 for j in range(n)] for i in range(m)]

    for i in range(m):
        for j in range(n):
            result[i][j] = arr[n-j-1][i]

    return result
print(rotate_90(arr, N, M))
