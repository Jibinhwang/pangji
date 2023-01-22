# 시간초과 -> 이분탐색 공부해야함

import sys

N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
B=list(map(int,sys.stdin.readline().split()))

A.sort()

for i in range(M):
    for j in range(N):
        if B[i]>A[N-1]:
            print("0")
            break
        elif B[i] == A[j]:
            print("1")
            break
        elif B[i]!=A[j] and B[i]<A[j]:
            print("0")
            break
        
        