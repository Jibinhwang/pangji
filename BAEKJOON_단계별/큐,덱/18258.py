# 스택에서 조금만 수정했더니 시간초과가 떴다. POP할때 하나씩 다 앞으로 밀리는게 시간초과 유발 원인
# pointer 이용해서 del을 쓰지말고 구현해보자
import sys 

N = int(sys.stdin.readline())
B = []
pointer = 0

def back():
    if len(B) == pointer:
        return -1
    else:
        return B[len(B)-1]

def empty():
    if len(B) == pointer:
        return 1
    else:
        return 0

for i in range(N):
    a = sys.stdin.readline()
    if 'push' in a:
        a, b = a.split()
        B.append(int(b))
    if 'pop' in a:
        if len(B) == pointer:
            print(-1)
        else:
            print(B[pointer])
            pointer += 1
    if 'size' in a:
        print(len(B)-(pointer))
    if 'empty' in a:
        print(empty())    
    if 'front' in a:
        if len(B) == pointer:
            print(-1)
        else:
            print(B[pointer])
    if 'back' in a:
        print(back())