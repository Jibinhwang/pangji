K = int(input())

A = []
for i in range(K):
    N = int(input())
    if N != 0:
        A.append(N)
    else:
        del A[-1]
        
print(sum(A))