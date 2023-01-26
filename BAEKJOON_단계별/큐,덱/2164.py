import sys

N = int(sys.stdin.readline())
A = [i for i in range(1,N+1)]

pointer = 0
while True:
    pointer += 1 #버리기
    if pointer == 2*N-1:
        break
    A.append(A[pointer])
    pointer += 1
    print(A)

print(A[2*N-2])
    