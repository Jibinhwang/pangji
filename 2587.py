# 평균과 중앙값 구하기

l = []
sum = 0
for i in range(5):
    a = int(input())
    sum+=a
    l.append(a)

l.sort()

print(int(sum/5))
print(l[2])