import sys
from fractions import Fraction

a, b = map(int, sys.stdin.readline().split())

if b > a-b:
    b = a-b
    
M=1 
N=1
for i in range(b):
    M *= a-i
    N *= i+1
    
F = Fraction(M, N)
print(int(F)%10007)
# 유리수 표현방식 Fraction 함수
# 부동소숫점 이슈 확인