x = input()
y = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
b = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
c = 0
for i in y:
    c += x.count(i)
for i in b:
    c += x.count(i)
c -= x.count('c=')
c -= x.count('c-')
c -= x.count('dz=')*2
c -= x.count('d-')
c -= x.count('lj')*2
c -= x.count('nj')*2
c -= x.count('s=')
c -= x.count('z=')
print(c)