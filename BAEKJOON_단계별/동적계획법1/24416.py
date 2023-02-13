# 전역변수 함수 안에서 사용하는 법
# https://codingpractices.tistory.com/entry/Python-%EC%A0%84%EC%97%AD-%EB%B3%80%EC%88%98-%EC%A7%80%EC%97%AD-%EB%B3%80%EC%88%98-%EC%82%AC%EC%9A%A9%EB%B2%95-%EC%B4%9D-%EC%A0%95%EB%A6%AC-global-nonlocal

import sys

N = int(sys.stdin.readline())
cnt1 = 0
cnt2 = 0
f=[1]*N

def fib(n):
    global cnt1
    if (n==1 or n==2):
        cnt1 += 1
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
def fibonacci(n):
    global cnt2
    global f
    for i in range(2,n):
        f[i]=f[i-1]+f[i-2]
        cnt2 += 1
    return cnt2

fib(N)
print(cnt1,fibonacci(N),sep=" ")