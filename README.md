# python_class_SKU2024-04
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="img/python-logo-transparent2.png">
  <source media="(prefers-color-scheme: dark)" srcset="img/python-logo-transparent2.png">
  <img alt="파이썬 로고" src="img/python-logo-transparent2.png">
</picture>


서경대학교 파이썬 강의 4분반 2024년 1학기 수업 (강좌코드: EE1201-04, EN1004-04) 홈페이지입니다.

---

### 카톡 오픈채팅방 안내

수업 오픈채팅방이 개설되었습니다. 수업 공지 내용을 전달할 예정이니 참여 부탁드립니다.

[https://open.kakao.com/o/gYu9jZfg](https://open.kakao.com/o/gYu9jZfg)
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="img/Python_QRcode_Small.PNG">
  <source media="(prefers-color-scheme: dark)" srcset="img/Python_QRcode_Small.PNG">
  <img alt="파이썬 로고" src="img/Python_QRcode_Small.PNG">
</picture>



---

### 숙제 안내

안녕하세요, 수업시간에 말씀을 다 드리지 못한 숙제 내용 공지드립니다.

숙제 내용은 실습문제 폴더의 [2장 변수와 연산자.cpp](https://github.com/Chaebin-Kim24/python_class_SKU2024-04/tree/2512f7c749d7df457e9fa6de579a509ae20c6dee/%EC%8B%A4%EC%8A%B5%20%EB%AC%B8%EC%A0%9C)에 있는 
C/C++ 코드를 파이썬 코드로 바꿔서 제출하는 것입니다. 

제출기한은 다음주 수업시간 (3/21) 전까지입니다.

제 이메일 chaebinkim@skuniv.ac.kr 로 소스코드를 보내주시면 실행해서 채점하겠습니다.

에디터는 어떤 프로그램을 쓰셔도 무방합니다.

C/C++ 코드 중 마지막에 있는 심화학습은 숙제에서 제외입니다.

> [!WARNING]
> [2장 변수와 연산자.cpp](https://github.com/Chaebin-Kim24/python_class_SKU2024-04/tree/2512f7c749d7df457e9fa6de579a509ae20c6dee/%EC%8B%A4%EC%8A%B5%20%EB%AC%B8%EC%A0%9C)의 LAB2-6에서 문제는 result = result + num을 하고 result를 출력하는 것인데, c/c++ 코드에서는 num을 출력하는 것으로 되어있었습니다. result 출력과 num 출력 모두 정답처리하겠습니다.
---

### 교과서
"으뜸 파이썬", 박동규, 강영민 저, 생능 출판사, 2020

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
채점은 여러 테스트 케이스들에 대해서 통과한 개수를 기준으로 합니다.  

### 강의 피드백
1. 수업 방식 중 기본 개념 설명
* PPT에 처음 등장하는 모든 단어 및 내용을 설명하겠습니다.
2. 수업 방식 및 시험 방식 결정
* 수업 방식은 PPT 강의 및 실습으로 하겠습니다.
* 평가 방식은 상기 서술된 내용과 같습니다.
3. 학교에서 배우는 양, 기본 사용 방법 및 콘솔 결정
* 저자 유튜브 시청은 평가 방식에서 제외하겠습니다.
* 콘솔은 비쥬얼 스튜디오로 하겠습니다.
4. C/C++과의 차이점 및 차별점
* 실습 문제 풀이에서 C, C++ 코드와 비교하겠습니다.
5. 시험 문제를 교재 안에서만 출제
* 시험 문제에 교재 관련 페이지 숫자를 표기하겠습니다.
6. 파이썬 기초, 기본 작동방식, 코딩 방법
* 파이썬을 교재 내용에 충실하게 기초부터 다루겠습니다.
* 파이썬의 기본 실행모드를 다루겠습니다.
* 파이썬 코딩 방법을 실습 시간에 설명하겠습니다.
