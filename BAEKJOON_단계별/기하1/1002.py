T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = (x2-x1)**2 + (y2-y1)**2
    sum = (r1+r2)**2
    sub = (r1-r2)**2
    if dist == 0 and r1 == r2:
        print(-1)
    elif dist == 0:
        print(0)
    elif sum == dist or sub == dist:
        print(1)
    elif sub<dist<sum:
        print(2)
    else:
        print(0)