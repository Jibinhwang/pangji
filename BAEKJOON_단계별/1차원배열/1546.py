import sys

sum = 0
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A.sort()
M = A[0]

# for i in range(N):
#    A[i] = A[i]/M*100
#    sum += A[i]
    
# print(sum/3)