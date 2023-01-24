import sys
A = []
M = 0

for i in range(1,10):
    A=list(map(int, sys.stdin.readline().split()))
    for j in range(9):
        if(A[j]>=M):
            M=A[j]
            a,b=i,j+1
            
print(M)
print(a,b)