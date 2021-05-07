n = int(input())
l = [[] for _ in range(51)]
for i in range(n):
    k = input()
    l[len(k)].append(k)
for i in range(51):
    l[i] = list(set(l[i]))
    l[i].sort()
for i in range(1,51):
    l[0] += l[i]
for i in range(len(l[0])):
    print(l[0][i])


# 제일 빠르고 간결한 다른 풀이
import sys
word=set()
for i in range(int(input())):
    word.add(sys.stdin.readline().rstrip())
word=list(word)
word.sort()
word.sort(key=lambda x:len(x))
print("\n".join(word))