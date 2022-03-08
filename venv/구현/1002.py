n = int(input())
for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x1-x2)**2+(y1-y2)**2)**.5
    R = max(r1, r2)
    r = min(r1, r2)
    rp = r1+r2
    rm = R - r
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    else:
        if R > d:
            if d > rm:
                print(2)
            elif d == rm:
                print(1)
            elif d < rm:
                print(0)
        elif R <= d:
            if d > rp:
                print(0)
            elif d == rp:
                print(1)
            elif d < rp:
                print(2)

