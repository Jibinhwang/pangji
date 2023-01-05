N = int(input())

l = list(map(int, input().splitlines()))

l.sort()

for i in l:
    print(i)