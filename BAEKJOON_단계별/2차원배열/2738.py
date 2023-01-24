import sys
N, M = map(int, sys.stdin.readline().split())
A=[]
B=[]

for i in range(N):
    A.append(list(map(int,sys.stdin.readline().split())))
    
for i in range(N):
    B.append(list(map(int,sys.stdin.readline().split())))    
    
for i in range(N):
    for j in range(M):
        print(A[i][j]+B[i][j], end=" ")
    print()