import sys 

N = int(sys.stdin.readline())
B = []

def push(i):
    B.append(i)
    
def top():
    if len(B) == 0:
        return -1
    else:
        return B[-1]

def empty():
    if len(B) == 0:
        return 1
    else:
        return 0
    
def pop():
    if len(B) == 0:
        print(-1)
    else:
        print(B[-1])
        del B[-1]
    

for i in range(N):
    a = sys.stdin.readline()
    if 'push' in a:
        a, b = a.split()
        push(int(b))
    if 'top' in a:
        print(top())
    if 'size' in a:
        print(len(B))
    if 'empty' in a:
        print(empty())    
    if 'pop' in a:
        pop()