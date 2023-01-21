import sys

sum = 0
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A.sort(reverse=True)
M = A[0] # 최대값이 저장되어 있음

for i in range(N):
    A[i] = A[i]/M*100
    sum += A[i]
    
print(sum/3)