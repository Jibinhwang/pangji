import sys

N = int(sys.stdin.readline())
Word = [sys.stdin.readline().strip('\n') for i in range(N)]
A = [[len(Word[i]),Word[i]] for i in range(N)]

A.sort(key = lambda x:(x[0],x[1]))
Word = [A[i][1] for i in range(N)]

result = list(dict.fromkeys(Word))
for i in result:
    print(i)

# key = lambda 쓰는법 정리 (11650, 11651) - 다중 조건 정렬
# https://infinitt.tistory.com/122
# dictionary를 이용한 중복제거
# https://blockdmask.tistory.com/543