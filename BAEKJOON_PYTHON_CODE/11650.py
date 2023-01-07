import sys

N = int(sys.stdin.readline())
A = []

for i in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))

A.sort()    

for i in A:
    print(*map(int, i))