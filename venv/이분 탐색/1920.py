import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
A.sort()
m = int(input())
L = list(map(int, input().split()))
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in range(m):
    result = binary_search(A, L[i], 0, n-1)
    if result == None:
        print(0)
    else:
        print(1)


# 가장 빠르고 간결한 풀이
import sys
input = sys.stdin.readline

def BOJ_1920():
    n,A,m = input(),set(input().split()),input()
    res=""
    for i in input().split():
        res += "1\n" if i in A else "0\n"
    print(res)
BOJ_1920()