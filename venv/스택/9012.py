n = int(input())
for i in range(n):
    s = input()
    c = 0
    t = 0
    N = 0
    for j in range(len(s)):
        t += 1
        if s[j] == "(":
            c += 1
        elif s[j] == ")":
            c -= 1
        if c < 0:
            print("NO")
            N += 1
            break
    if t != len(s):
        continue
    elif t == len(s):
        if N == 1:
            continue
        else:
            if c == 0:
                print("YES")
            else:
                print("NO")
