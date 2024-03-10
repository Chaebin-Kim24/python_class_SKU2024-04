# python_class_SKU2024-04
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="img/python-logo-transparent2.png">
  <source media="(prefers-color-scheme: dark)" srcset="img/python-logo-transparent2.png">
  <img alt="파이썬 로고" src="img/python-logo-transparent2.png">
</picture>

서경대학교 파이썬 강의 4분반 2024년 1학기 수업 (강좌코드: EE1201-04, EN1004-04) 홈페이지입니다.

### 평가방법
| 중간고사 | 기말고사 |  과제  |  출석  | 프로젝트 |
|:--------:|:--------:|:------:|:------:|:-------:|
|  30%     |  30%     | 20%    |  10%   |  10%    | 

중간고사는 객관식 10문항, 주관식 5문항, 코딩 문제 5문항으로 출제됩니다. 
객관식 문제와 주관식 문제는 각 1점, 코딩 문제는 각 3점입니다. 
기말고사는 코딩 문제 5문항, 각 6점으로 출제됩니다. 
과제는 교과서 연습 문제 중 선정한 5 ~ 10 문제 입니다. 
출석은 출결앱의 인증번호 방식으로 진행합니다. 
프로젝트는 시범적으로 시행하기 때문에 Pass/Fail로 점수가 나갑니다. 
프로젝트는 자유 형식이고, C로 작성된 예제 코드가 제공됩니다. 

### 객관식 문제 예시
다음 파이썬 코드의 실행 결과를 보기에서 고르시오
```python
x = 'a'
x, y = 0, 1
x ** y > ~x
```
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; 1) True &ensp;&ensp;&ensp; 2) False &ensp;&ensp;&ensp; 3) -1 &ensp;&ensp;&ensp;&ensp; 4) 0 &ensp;&ensp;&ensp;&ensp; 5) 1  

### 주관식 문제 예시
다음 파이썬 코드의 결과가 5보다 작은 피보나치 수열이 되도록 주석으로 표시한 줄에 들어갈 알맞는 내용을 모두 고르시오
```python
def fib(n):
  a, b = 0, 1
  while a < n:
    print(a, end=' ')
    # 코드를 입력할 줄
fib(5)
```
실행 결과: 0 1 1 2 3 

### 코딩 문제 예시 
핸드폰 판매 대리점에 철수, 영희, 둘리, 마이콜, 희동이가 근무하고 있습니다.
판매에 성공할 때마다 다음과 같이 일지에 "날짜, 판매원 이름, 판매 금액" 형식의 문자열을 리스트로 기록해놓습니다.
```python
# 일지 형식
input = ["2024-03-02, 철수, 10000", "2024-03-03, 영희, 10000"]
```
문제: 2024년 3월에 총 판매액이 많은 순서로 판매원 이름을 나열하여 출력하는 함수를 작성하시오.
```python
# 출력 형식
output = ["철수", "영희", "둘리", "마이콜", "희동이"]
```
```python
def phone_sales(input):
  output = []
  return output
```

