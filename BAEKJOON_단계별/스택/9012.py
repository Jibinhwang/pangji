N = int(input())

for _ in range(N):
    left = 0
    right = 0
    flag = 0
    A = input()
    for i in range(len(A)):
        if A[i] == '(':
            left += 1
        elif A[i] == ')':
            right += 1
        if right > left:
            flag += 1
    if flag == 0 and left == right:
        print('YES')
    else:
        print('NO')