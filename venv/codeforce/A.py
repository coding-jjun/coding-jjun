import sys
input = sys.stdin.readline
N = int(input())
def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

for i in range(N):
    t = int(input())
    l1 = list(map(int, input().split()))
    l2 = l1[:]
    k = quick_sort(l2)
    count = 0
    for j in range(1, t):
        a = l1[:j]
        b = l1[j:]
        quick_sort(a)
        quick_sort(b)
        c = a + b
        if k == c:
            print('NO')
            break
        else:
            count += 1
    if count == t - 1:
        print('YES')