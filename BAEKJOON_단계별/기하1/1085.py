import sys

A=[]
x,y,w,h = map(int, sys.stdin.readline().split())

A.append(x)
A.append(y)
A.append(w-x)
A.append(h-y)
A.sort()

print(A[0])