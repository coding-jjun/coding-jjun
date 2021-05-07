import sys
input = sys.stdin.readline
S = set([])
n = int(input())
for i in range(n):
    k = input()
    if k == 'all\n' or k == 'empty\n':
        o = k
    else:
        o, m = map(str, k.split())
    if o == 'add':
        S.add(m)
    elif o == 'remove':
        if m in S:
            S.remove(m)
        else:
            continue
    elif o == 'check':
        if m in S:
            print(1)
        else:
            print(0)
    elif o == 'toggle':
        if m in S:
            S.remove(m)
        else:
            S.add(m)
    elif o[:3] == 'all':
        S = set([str(i) for i in range(1, 21)])
    elif o[:5] == 'empty':
        S = set([])