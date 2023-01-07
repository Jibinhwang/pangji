import sys

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
S = list(dict.fromkeys(A))
S.sort()

dict = {S[i] : i for i in range(len(S))}
for i in A:
    print(dict[i], end=' ')

# 임의의 개수의 정수를 한줄에 입력받아 리스트에 저장하는 법
# 이중for문 -> 시간초과
# dict 정리