# dict형태로 input 저장하기
import sys
from collections import Counter

N = int(sys.stdin.readline())

for _ in range(N):
    my_list = []
    my_dict = {}
    Mu = 1
    M = int(sys.stdin.readline())
    for _ in range(M):
        a, b = sys.stdin.readline().split()
        my_list.append(b)
        
    my_dict = dict(Counter(my_list))
    V = list(my_dict.values())
    for i in range(len(V)):
        Mu*=(V[i]+1)
    print(Mu-1)