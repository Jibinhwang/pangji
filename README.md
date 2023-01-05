# 🔥 팡지 백준 뿌셔 🔥

[![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=hjb7165)](https://solved.ac/hjb7165/)
<br>

## 시작한 날 : 2022년 12월 30일
## 목표 : **실버 V**
### <br>풀이 일기
---
날짜 : 2022.12.30.  
푼 문제 : test  
```python
print("Hello, world!")
```
print로 출력만 하면 된다.

---
날짜 : 2022.01.05
푼 문제 : 2750
```python
N = int(input())
l = []
for i in range(N):
    a = int(input())
    l.append(a)

l.sort()

for i in l:
    print(i)
```
정렬 알고리즘을 써야하지만 일단은 내장함수 .sort()를 이용해서 풀었다.