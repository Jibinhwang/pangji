import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

A.sort()
if len(A)%2 == 0:
    print(A[0]*A[N-1])
else:
    M = int((N+1)/2)-1
    print(A[M]*A[M])