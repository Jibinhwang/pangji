import sys

N = int(sys.stdin.readline())
A = [[0 for i in range(100)] for j in range(100)]

print(type(A))
sum = 0
for i in range(N):
    a,b = map(int, sys.stdin.readline().split())
    for j in range(a-1,a+9):
        for k in range(b-1,b+9):
            if A[j][k] == 0:
                sum+=1
                A[j][k] = 1
                
print(sum)
