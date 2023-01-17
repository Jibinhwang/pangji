import sys

N = list(sys.stdin.readline().strip('\n'))
N.sort(reverse=True)

A = map(int, N)
print(*A, sep = '')