from math import floor

order_list = []
def merge_sort(A, p, r):
    if p < r:
        q = floor((p+r)/2)
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)
    return A
        
def merge(A, p, q, r):
    global cnt
    i = p
    j = q+1
    tmp = []
    while (i<=q and j<=r):
        if A[i] <= A[j]:
            tmp.append(A[i])
            order_list.append(A[i])
            i = i+1
            cnt = cnt+1
        else:
            tmp.append(A[j])
            order_list.append(A[j])
            j = j+1
            cnt = cnt+1
    while i <= q:
        tmp.append(A[i])
        order_list.append(A[i])
        i = i+1
        cnt = cnt+1
    while j <= r:
        tmp.append(A[j])
        order_list.append(A[j])
        j = j+1
        cnt = cnt+1
    i = p
    t = 0
    while i <= r:
        A[i] = tmp[t]
        i = i+1
        t = t+1

global cnt
cnt = 0
A, N = map(int, input().split())

lst = list(map(int, input().split()))
merge_sort(lst, 0, len(lst)-1)

if N > len(order_list):
    print(-1)
else:
    print(order_list[N-1])