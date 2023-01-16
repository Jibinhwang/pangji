import sys
input = sys.stdin.readline
N, K = map(int,input().split())

lst = [i for i in range(1, N+1)]
result = []
idx = K-1

for i in range(N):
    if idx <= len(lst)-1:
        result.append(lst[idx])
        del lst[idx]
        idx = idx - 1 # 1개 줄어들었으므로 idx 1개 감소
        idx = idx + K
    else:
        idx = idx % len(lst)
        result.append(lst[idx])
        del lst[idx]
        idx = idx - 1 # 1개 줄어들었으므로 idx 1개 감소
        idx = idx + K
        
print("<", end="")
print(*result, sep=", ", end = "")
print(">")