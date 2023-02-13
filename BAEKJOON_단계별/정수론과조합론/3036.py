import sys
import math

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

c = A[0]
for i in range(1,N):
    least = math.gcd(c, A[i])
    print(c//least,"/",A[i]//least,sep="")