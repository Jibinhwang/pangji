import sys

a = list(sys.stdin.readline().strip())

# 2개
b = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=', 'dz=']
c = []

i = 0
count = 0

if len(a) == 1:
    print(1)
elif len(a) == 2:
    if str(a[0]+a[1]) in b:
        print(1)
    else:
        print(2)
else:
    while i < len(a)-2:
        first, second, third = a[i], a[i+1], a[i+2]
        two = str(first + second)
        three = str(first + second + third)

        if two in b:
            c.append(two)
            count+=2
            i = i + 2
        elif three in b:
            c.append(three)
            count+=3
            i = i + 3
        else:
            c.append(a[i])
            count+=1
            i = i + 1
    if len(a)-count == 0:
        print(len(c))
    elif len(a)-count == 1:
        print(len(c)+1)
    elif len(a)-count == 2:
        if str(a[-2] + a[-1]) in b:
            print(len(c) + 1)
        else:
            print(len(c) + 2)
