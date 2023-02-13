import sys

N = int(sys.stdin.readline())

M = 1
for i in range(1,N+1):
    M *= i

A = list(str(M))

if A[-1] != '0':
    print(0)
else:
    a = len(A)
    c = 0
    for i in range(a-1,0,-1):
        if A[i] != '0':
            print(c)
            sys.exit()
        else:
            c += 1