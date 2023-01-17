import sys

A = []
N = int(sys.stdin.readline())
for i in range(1,N+1):
    if i == 1:
        A.append(1)
    elif i ==2 :
        A.append(2)
    else:
        A.append(A[i-2]+A[i-3])

print(A[N])
