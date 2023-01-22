N=int(input())

for _ in range(N):
    A=list(map(str,input()))
    result=0
    temp=0
    for i in range(len(A)):
        if A[i]=='X':
            temp=0
        if A[i]=='O':
            temp+=1
            result+=temp
    print(result)