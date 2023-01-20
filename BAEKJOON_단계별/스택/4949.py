import sys

while True:
    A = input()
    S = []
    if A[0] == '.':
        sys.exit()
    for i in range(len(A)):
        if(A[i] == '(' or A[i] == '['):
            S.append(A[i])
        elif(A[i] == ')'):
            l = len(S)
            if l == 0:
                print('no')
                break
            elif S[l-1] == '(':
                del S[l-1]
            else:
                print('no')
                break
        elif(A[i] == ']'):
            l = len(S)
            if l == 0:
                print('no')
                break
            elif S[l-1] == '[':
                del S[l-1]
            else:
                print('no')
                break
        elif(A[i] == '.' and len(S) == 0):
            print('yes')
        elif(A[i] == '.' and len(S) != 0):
            print('no')