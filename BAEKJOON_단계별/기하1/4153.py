import sys

while True:
    A = list(map(int, sys.stdin.readline().split()))
    A.sort()
    if(A[0]==0):
        sys.exit()
    elif((A[0]**2)+(A[1]**2)==(A[2]**2)):
        print("right")
    else:
        print("wrong")     