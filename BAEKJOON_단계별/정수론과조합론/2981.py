import sys

N = int(sys.stdin.readline())
A = [int(sys.stdin.readline()) for _ in range(N)]
B = []

A.sort()
for i in range(N-1):
    B.append(A[i+1]-A[i])
    
