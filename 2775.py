T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    total = 0
    
    for i in range(n):
        sum = ho(k-1,i+1)
        total += sum

    print(total)
    total = 0

def ho(a,b):
    s = 0
    if a == 0:
        s += b
    else:
         for i in range(b):
             s = s + ho(a-1,i+1)
    return s