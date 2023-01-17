# 평균과 중앙값 구하기
import sys
l = [int(sys.stdin.readline().strip()) for i in range(5)]

l.sort()

print(int(sum(l)/5))
print(l[2])