# 접근자체의 오류
# 왜 0이 생기는지 생각해보자! 5의 배수!
import sys

a, b = map(int, sys.stdin.readline().split())

if b > a-b:
    b = a-b
    
M=1 
N=1
for i in range(b):
    M *= a-i
    N *= i+1
    
A = list(str(int(M/N)))

if A[-1] != '0':
    print(0)
else:
    a = len(A)
    c = 0
    for i in range(a-1,0,-1):
        if A[i] != '0':
            print(c)
            sys.exit()
        else:
            c += 1