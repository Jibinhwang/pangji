N = int(input())

A = [list(map(str,input())) for _ in range(N)]

def count(arr):
    a=0
    for i in range(N):
        temp=0
        for j in range(N):
            if arr[i][j]=='.':
                temp += 1
                if j==N-1 and temp>=2:
                    a+=1
            elif arr[i][j]=='X':
                if temp >= 2:
                    a+=1
                temp=0 
    return a

print(count(A), end=" ")

for i in range(N):
    for j in range(N):
        if i<j:
            A[i][j], A[j][i]=A[j][i], A[i][j]
            
print(count(A))