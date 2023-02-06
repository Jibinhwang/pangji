import sys

cnt = 0

def factor(N,M):
    global cnt
    for i in range(1,N+1):
        if M % i == 0:
            cnt = 1
            print("factor")
            break

while True:
    cnt = 0
    a,b = map(int, sys.stdin.readline().split())
    if a==0 and b==0:
        break
    if a < b:
        factor(a,b)
    elif a > b:
        if a % b == 0:
            cnt = 1
            print("multiple")
    if cnt == 0:
        print("neither")