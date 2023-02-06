import sys

N = int(sys.stdin.readline())

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    for i in range(1,min(a,b)+1):
        if a % i == 0 and b % i == 0:
            factor = i
    print(factor * int(a/factor) * int(b/factor))