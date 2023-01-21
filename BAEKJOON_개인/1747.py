import math
import sys

A = input()
N = int(A)

def prime(M):
    f = 0
    for i in range(2,M):
        if (M%i)==0:
            f=1 #소수가 아님
            break
    if f==0:
        print(N)
        return 0
    else:
        return M
    
while True:
    flag=0
    l=math.ceil(len(A)/2)
    for i in range(0,l):
        if A[i] != A[len(A)-1-i]:
            flag=1
            N+=1
            A=str(N)
            break
    if flag==0:
        if prime(N) == 0:
            sys.exit()
        else:
            N+=1
            A=str(N)