import sys

N = int(sys.stdin.readline())
A = [int(sys.stdin.readline()) for _ in range(N)]
B = []

A.sort()
a, b = A[0], A[1]

flag = 1
for i in range(b,0,-1):
    if a%i == b%i:
        M = a%i
        for j in range(N-2):
            if(A[j+2]%i != M):
                flag = 0
                break
        if flag == 1:
            B.append(i)
        
B.sort() 
B.remove(1)   
print(*B)