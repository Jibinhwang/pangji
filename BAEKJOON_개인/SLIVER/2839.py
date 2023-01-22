import sys
import math

N=int(sys.stdin.readline())
M=math.floor(N/5)+1

a=1667
for i in range(M):
    b = int((N-(5*i))/3)
    if (N-(5*i))%3==0 and i+b<a:
        a=i+b
        
if a==1667:
    print(-1)
else:
    print(a)