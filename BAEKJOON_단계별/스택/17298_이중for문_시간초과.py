#시간초과
import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
R = []
flag = 0

for i in range(N):
    pointer = i
    flag = 0
    while pointer != N:
        if A[pointer] > A[i]:
            R.append(A[pointer])
            flag = 1
            break
        elif A[pointer] <= A[i]:
            pointer += 1
    if flag == 0:
        R.append(-1)
        
print(*R)