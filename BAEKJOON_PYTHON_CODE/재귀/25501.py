import sys
A=[]
N = int(sys.stdin.readline())
for i in range(N):
    A.append(sys.stdin.readline().strip('\n'))
 
def recursion(s, l, r, c):
    if l >= r: return 1, c
    elif s[l] != s[r]: return 0, c
    else: 
        c = c + 1
        return recursion(s, l+1, r-1, c)

def isPalindrome(s):
    cnt = 1
    return recursion(s, 0, len(s)-1, cnt)

for i in A:
    a, b = isPalindrome(i)
    print(a,b, sep=" ")
# .strip('\n') 주의