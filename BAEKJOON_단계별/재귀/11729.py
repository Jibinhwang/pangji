#11729 하노이 탑 이동 순서
N = int(input())
print(2**N-1)

def hanoi(n, a, b, c):
    if n==1:
        print(a, c)
    else:
        hanoi(n-1, a, c, b)
        print(a,c)
        hanoi(n-1, b, a, c)

hanoi(N, 1, 2, 3)
