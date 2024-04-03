읽기 자료는 시험 범위가 아닙니다.

파이썬 프로그래밍을 하거나 코드를 읽을 때 찾아볼 수 있는 자료를 모으고 있습니다.

현재 목록은 다음과 같습니다.

### 4장 함수

가변 키워드인자
```python
def func(**keywords):
  for key in keywords:
    print(key, ":", keywords[key])

func(width=10, height=2)
# 출력:
# width : 10
# height : 2
```
데코레이터
```python
def debugging_1(some_func):
  def wrapper(x):
    print(x)
    some_func(x)
  return wrapper

@debugging_1
def func(x):
  pass

func(1)
출력: 1
```
