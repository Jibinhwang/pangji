A = [0] * 42 # 1차원 배열을 0으로 채움

cnt = 0

for i in range(10):
    N=(int(input())%42)-1
    if A[N] == 0:
        A[N] += 1
        cnt+=1
        
print(cnt)