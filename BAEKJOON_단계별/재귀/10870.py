import sys
N = int(sys.stdin.readline())

def Fib(i):
    if(i==0):
        return 0
    elif(i==1):
        return 1
    else:
        return Fib(i-1)+Fib(i-2)
    
print(Fib(N))