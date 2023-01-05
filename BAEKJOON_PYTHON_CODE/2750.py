N = int(input())

l = []
for i in range(N):
    a = int(input())
    l.append(a)

l.sort()

for i in l:
    print(i)