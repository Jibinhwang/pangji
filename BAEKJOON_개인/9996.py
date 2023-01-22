import re
N = int(input())
a,b = input().split('*')
p = re.compile(a+'*'+b)

for _ in range(N):
    S = input()
    print(p.search(S))
    
