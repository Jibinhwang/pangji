# 산술평균, 중앙값, 최빈값, 범위
import sys
from collections import Counter

N = int(sys.stdin.readline())
l = [int(sys.stdin.readline().strip()) for i in range(N)]

l.sort()

#최빈값구하는 함수
def Most(li, n):
    if n!=1:
        counter = Counter(l).most_common(2) 
        # type(counter) : list, counter의 요소는 tuple
        if counter[0][1] == counter[1][1]:
            return counter[1][0]
        else:
            return counter[0][0]
    else:
        return li[0]
        
print(round(sum(l)/N)) # 산술평균 
print(l[int(N/2)]) # 중앙값
print(Most(l, N)) #최빈값
print(l[N-1]-l[0]) #범위