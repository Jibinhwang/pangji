import sys

A = []
N = int(sys.stdin.readline())
for i in range(N):
    A.append(list(sys.stdin.readline().split()))
   
for i in range(N):
    change = lambda x: int(x)
    A[i][0] = change(A[i][0])

A.sort(key = lambda x:x[0])

for i in A:
    print(i[0], i[1])
    
# 주의 !! sys.stdin.readline()은 str로 입력받으므로 int형으로 바꿔줘야함!