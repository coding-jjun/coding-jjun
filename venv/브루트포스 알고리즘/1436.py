s = set([666])
for i in range(1, 10):
    s.add(int(str(i)+str(666)))
for i in range(10):
    s.add(int(str(666)+str(i)))
for i in range(10, 100):
    s.add(int(str(i)+str(666)))
    s.add(int(str(i)[0]+str(666)+str(i)[1]))
    s.add(int(str(666)+str(i)))
    s.add(int(str(6660)+str(i)))
    s.add(int(str(66600)+str(i)))
for i in range(10):
    s.add(int(str(6660)+str(i)))
    s.add(int(str(66600)+str(i)))
    s.add(int(str(666000)+str(i)))
for i in range(100, 1000):
    s.add(int(str(i)+str(666)))
    s.add(int(str(i)[0:2]+str(666)+str(i)[2]))
    s.add(int(str(i)[0]+str(666)+str(i)[1:]))
    s.add(int(str(666)+str(i)))
    s.add(int(str(6660)+str(i)))
for i in range(1000,10000):
    s.add(int(str(i)+str(666)))
    s.add(int(str(i)[0:3]+str(666)+str(i)[3]))
    s.add(int(str(i)[0:2]+str(666)+str(i)[2:]))
    s.add(int(str(i)[0]+str(666)+str(i)[1:]))
    s.add(int(str(666)+str(i)))
six = list(s)
six.sort()
print(six[int(input())-1])

#가장 빠르고 간결한 풀이
N = int(input())
if N == 1:
    print(666)
else:
    count = 1
    for i in range(2, N + 1):
        base_title = "{0}666".format(i - 1)
        num_of_extra_six_in_row = 0
        for k in range(len(base_title) - 3):
            if base_title[-4 - k] == '6':
                num_of_extra_six_in_row += 1
            else:
                break
        count += int(10 ** num_of_extra_six_in_row)
        if count >= N:
            break

    if num_of_extra_six_in_row > 0:
        base = int(10 ** num_of_extra_six_in_row)
        count -= base
        base_title = int(base_title) - int(base_title) % base + (N - count - 1)

    print(base_title)