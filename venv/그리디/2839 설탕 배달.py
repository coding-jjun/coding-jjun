n = int(input())
r = n % 5
if r == 0:
    print(int(n/5))
if r == 1:
    print(int((n-6)/5+2))
if r == 2:
    if n == 7:
        print(-1)
    else:
        print(int((n-12)/5+4))
if r == 3:
    print(int((n-3)/5+1))
if r == 4:
    if n == 4:
        print(-1)
    else:
        print(int((n-9)/5+3))