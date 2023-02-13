import sys

a, b = map(int, sys.stdin.readline().split())

if b > a-b:
    b = a-b
    
M=1 
N=1
for i in range(b):
    M *= a-i
    N *= i+1
    
print(int(M/N))