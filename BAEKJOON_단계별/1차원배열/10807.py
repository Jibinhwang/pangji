import sys

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
V = int(sys.stdin.readline())

print(A.count(V))