import sys
import math

while True:
    A=input()
    flag=0
    if A=="0":
        sys.exit()
    else:
        l=math.ceil(len(A)/2)
        for i in range(l):
            if A[i] != A[len(A)-1-i]:
                flag=1
                print("no")
                break
        if flag==0:
            print("yes")