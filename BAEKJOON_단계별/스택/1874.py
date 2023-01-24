import sys

N = int(sys.stdin.readline())
A = [i for i in range(0,N+1)]
P = []

pointer = 0
idx = 0
flag=0

for i in range(N):
    M = int(sys.stdin.readline())
    if pointer < M:
        while pointer != M:
            if A[pointer+1] == 0:
                pointer +=1
            else:
                pointer += 1
                P.append('+')
        P.append('-') # pop
        A[pointer] = 0
        
    elif pointer > M:
        while pointer != M:
            if A[pointer-1] == 0:
                pointer -= 1
            elif A[pointer-1]!=0 and pointer-1 != M:
                flag=1
                pointer -= 1
            else:
                pointer -= 1
                P.append('-')
                A[pointer] = 0

if flag == 1:
    print('NO')
else:
    print(*P, sep='\n')