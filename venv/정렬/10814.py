import sys
input=sys.stdin.readline
n = int(input())
data = []
for i in range(n):
    a, b= input().split()
    data.append([int(a),b,i])
data = sorted(data, key = lambda x: (x[0], x[2]))
for i in range(len(data)):
    print(data[i][0], data[i][1])
