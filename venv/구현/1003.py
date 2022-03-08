import sys
input = sys.stdin.readline
def fibonacci(n):
    global z
    global o
    if n == 0:
        z += 1
        return 0
    elif n == 1:
        o += 1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(int(input())):
    z = 0
    o = 0
    fibonacci(int(input()))
    print(str(z)+" "+str(o))