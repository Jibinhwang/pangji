# 🔥 팡지 백준 뿌셔 🔥

[![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=hjb7165)](https://solved.ac/hjb7165/)
<br>

## 시작한 날 : 2022년 12월 30일
## 목표 : **실버 V**
### <br>백준 풀이 일기
---
날짜 : 2022.12.30.  
푼 문제 : test  
```python
print("Hello, world!")
```
print로 출력만 하면 된다.

---
날짜 : 2022.01.05.  
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

---
날짜 : 2022.01.05.  
푼 문제 : 2587  
```python
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
```
2750번과 같은 방식으로 .sort()를 이용해서 정렬했다
```python
import sys
l = [int(sys.stdin.readline().strip()) for i in range(5)]

l.sort()

print(int(sum(l)/5))
print(l[2])
```
sys.stdin.readline()과 list comprehension을 이용해서 append함수와 input()을 쓰지 않고 2587번을 다시 풀어보았다.   

---
날짜 : 2022.01.05.  
푼 문제 : 2751  
```python
import sys
N = int(sys.stdin.readline())
l = [int(sys.stdin.readline().strip()) for i in range(N)]

l.sort()

for i in l:
    print(i)
```
## :rocket: sys.stdin.readline()  
_input()대신 sys.stdin.readline()를 사용해야한다!!!_   
놀랍게도 모든 입력 중 input()이 가장 느리다고 한다.  
2751에서는 무려 1,000,000개 이하의 숫자를 입력받아야 하므로 for문을 돌면서 계속 input()으로만 받다보니 시간초과 문제가 발생하였다.  
앞으로는 sys.stdin.readline()을 습관화하자!  
**사용법은 <https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline>를 참고하였다.**  

```python
l = [int(sys.stdin.readline().strip()) for i in range(N)]
```
위 코드는 N개의 숫자를 여러줄로 받아줄 때 사용한다  
이 때, int()는 꼭 붙여줘야한다!  
int를 붙이지 않으면 입력시 문자열로 받기때문에 1 14 2를 오름차순 시켰더니 1 14 2로 출력되었다   

---
날짜 : 2022.01.05.  
푼 문제 : 2751  
```python
N, k = map(int, input().split())

x = list(map(int, input().split()))
x.sort(reverse=True)

print(x[k-1])   
```
한 줄에 여러개의 변수를 입력받거나, 여러개의 숫자들을 for문을 이용하지 않고 입력받기 위해 map함수를 활용할 수 있다.  
# <br>map함수
```python
map(적용시킬 함수, 리스트나 튜플 등)
```
map함수의 반환값은 map객체이므로 형 변환 필수!!  