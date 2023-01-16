import sys
from collections import Counter

a = []
for i in range(3):
    a.append(list(map(int,sys.stdin.readline().split())))
    
first = Counter([i[0] for i in a]).most_common()[-1]
second = Counter([i[1] for i in a]).most_common()[-1]

print(first[0], second[0])

# 2차원 배열에서 열 추출