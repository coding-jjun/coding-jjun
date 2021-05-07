d=[0]*41

def fibo(x):
    if d[x]!=0:
        return d[x]
    if x < 2:
        return x
    else:
        d[x]=fibo(x-1)+fibo(x-2)
        return d[x]

T = int(input())
for i in range(T):
    x= int(input())
    if x == 0:
        print(1, 0)
    elif x == 1:
        print(0,1)
    else:
        print(fibo(x-1), fibo(x))