#0106
import sys

N = int(sys.stdin.readline())
A = []

for i in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    temp = A[i][1]
    A[i][1] = A[i][0]
    A[i][0] = temp
    
A.sort()

for i in A:
    print(i[1], i[0])
    
# 도훈이 풀이 확인
