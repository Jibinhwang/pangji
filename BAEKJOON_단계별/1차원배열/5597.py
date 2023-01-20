A = [0] * 30 # 1차원 배열을 0으로 채움

for i in range(28):
    N = int(input())-1
    A[N] = A[N] + 1

for i in range(30):
    if A[i] == 0:
        print(i+1)