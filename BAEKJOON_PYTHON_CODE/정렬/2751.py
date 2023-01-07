# 2750번과 다른점 : N은 1000이하 / N은 1,000,000이하 
import sys
N = int(sys.stdin.readline())
l = [int(sys.stdin.readline().strip()) for i in range(N)]

l.sort()

for i in l:
    print(i)