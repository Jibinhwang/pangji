import sys
A = [int(sys.stdin.readline().strip('\n')) for i in range(9)]
# B = A 이와 같은 방법으로 하면 안됨! 같은 주소를 공유하는 꼴이됨
B = A[:] # 슬라이싱을 통해 복사해준다
A.sort()

for i in range(9):
    if A[8] == B[i]:
        print(B[i])
        print(i+1)
        break