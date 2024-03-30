### LAB 3-1
```python
game_score = 800

print('game_score =', game_score)
if game_score >= 1000:
    print('당신은 고수입니다')

# 출력: game_score = 800

game_score = 1300

print('game_score =', game_score)
if game_score >= 1000:
    print('당신은 고수입니다')

# 출력:
# game_score = 1300
# 당신은 고수입니다

num_a, num_b = 100, 200
print('num_a =', num_a, ', num_b =', num_b)
if num_a == num_b:
    print('두 값이 일치합니다.')

# 출력: num_a = 100, num_b = 200

num_a, num_b = 300, 300
print('num_a =', num_a, ', num_b =', num_b)
if num_a == num_b:
    print('두 값이 일치합니다.')

# 출력:
# num_a = 100, num_b = 200
# 두 값이 일치합니다.
```

### LAB 3-2
```python
n = int(input('정수를 입력하세요 : '))
print('n =', n)
if n % 2 == 0:
    print(n, '은(는) 짝수입니다.')

# 출력:
# 정수를 입력하세요 : 50
# n = 50
# 50 은(는) 짝수입니다.

n = int(input('정수를 입력하세요 : '))
print('n =', n)
if n % 2 == 0:
    print(n, '은(는) 짝수입니다.')

# 출력:
# 정수를 입력하세요 : 75
# n = 75

x = int(input('정수를 입력하세요 : '))
print('x =', x)
if x > 0:
    print(x, '은(는) 자연수입니다.')

# 출력:
# 정수를 입력하세요 : 50
# x = 50
# 50 은(는) 자연수입니다.

x = int(input('정수를 입력하세요 : '))
print('x =', x)
if x > 0:
    print(x, '은(는) 자연수입니다.')

# 출력:
# 정수를 입력하세요 : -10
# x = -10
```

### LAB 3-3
```python
print('game_score =', game_score)
if game_score >= 1000:
    print('고수입니다.')
else:
    print('입문자입니다.')

# 출력:
# 게임점수를 입력하시오 : 800
# game_score = 800
# 입문자입니다.

game_score = int(input('게임점수를 입력하시오 : '))
print('game_score =', game_score)
if game_score >= 1000:
    print('고수입니다')
else:
    print('입문자입니다')

# 출력:
# 게임점수를 입력하시오 : 1300
# game_score = 1300
# 고수입니다.

num1 = int(input('한 정수를 입력하시오 : '))
num2 = int(input('다른 정수를 입력하시오 : '))
if num1 == num2:
    print('두 값이 일치합니다.')
else:
    print('두 값이 일치하지 않습니다.')

# 출력:
# 한 정수를 입력하시오 : 100
# 다른 정수를 입력하시오 : 200
# 두 값이 일치하지 않습니다.

num1 = int(input('한 정수를 입력하시오 : '))
num2 = int(input('다른 정수를 입력하시오 : '))
if num1 == num2:
    print('두 값이 일치합니다.')
else:
    print('두 값이 일치하지 않습니다.')

# 출력:
# 한 정수를 입력하시오 : 300
# 다른 정수를 입력하시오 : 300
# 두 값이 일치합니다.

is_adult = int(input('당신은 성인인가요(성인이면 1, 미성년이면 0): '))
if is_adult == 0:
    print('당신은 미성년자입니다.')
else:
    if is_adult == 1:
        is_married = int(input('결혼을 하셨나요(기혼이면 1, 미혼이면 0): '))
        if is_married == 1:
            print('당신은 결혼한 성인입니다.')
        else:
            print('당신은 결혼하지 않은 성인입니다.')

# 출력:
# 당신은 성인인가요(성인이면 1, 미성년이면 0): 0
# 당신은 미성년자입니다.

is_adult = int(input('당신은 성인인가요(성인이면 1, 미성년이면 0): '))
if is_adult == 0:
    print('당신은 미성년자입니다.')
else:
    if is_adult == 1:
        is_married = int(input('결혼을 하셨나요(기혼이면 1, 미혼이면 0): '))
        if is_married == 1:
            print('당신은 결혼한 성인입니다.')
        else:
            print('당신은 결혼하지 않은 성인입니다.')

# 출력:
# 당신은 성인인가요(성인이면 1, 미성년이면 0): 1
# 결혼을 하셨나요(기혼이면 1, 미혼이면 0): 1
# 당신은 결혼한 성인입니다.

is_adult = int(input('당신은 성인인가요(성인이면 1, 미성년이면 0): '))
if is_adult == 0:
    print('당신은 미성년자입니다.')
else:
    if is_adult == 1:
        is_married = int(input('결혼을 하셨나요(기혼이면 1, 미혼이면 0): '))
        if is_married == 1:
            print('당신은 결혼한 성인입니다.')
        else:
            print('당신은 결혼하지 않은 성인입니다.')

# 출력:
# 당신은 성인인가요(성인이면 1, 미성년이면 0): 1
# 결혼을 하셨나요(기혼이면 1, 미혼이면 0): 0
# 당신은 결혼하지 않은 성인입니다.

```

### LAB 3-4
```python
print(num >=1 and num <= 10)

age = 10
print('age =', age)
if (age > 10 and age < 19):
    print('청소년입니다.')

age = 12
print('age =', age)
if (age > 10 and age < 19):
    print('청소년입니다.')
```

### LAB 3-5
```python
speed = int(input('자동차의 속도를 입력하세요(단위 : km/h ): '))
if speed >= 100:
    print('고속')
elif speed >= 60:
    print('중속')
else:
    print('저속')
# 출력:
# 자동차의 속도를 입력하세요(단위 : km/h ): 13
# 저속

speed = int(input('자동차의 속도를 입력하세요(단위 : km/h ): '))
if speed >= 100:
    print('고속')
elif speed >= 60:
    print('중속')
else:
    print('저속')
# 출력:
# 자동차의 속도를 입력하세요(단위 : km/h ): 130
# 고속
```

### LAB 3-6
```python
for _ in range(5):
    print('Hello, Python!')
# Hello, Python!
# Hello, Python!
# Hello, Python!
# Hello, Python!
# Hello, Python!

for i in range(5):
    print(i)
# 0
# 1
# 2
# 3
# 4
```

### LAB 3-7
```python
print( list(range(1, 101)) )
# 출력: [1, 2, 3, 4, 5, (생략), 100]

print( list(range(2, 101, 2)) )
# 출력: [2, 4, 6, 8, 10, (생략), 100]

print( list(range(1, 101, 2)) )
# 출력: [1, 3, 5, 7, 9, (생략), 99]

print( list(range(-99, 0)) )
# 출력: [-99, -98, -97, -96, -95, (생략), -1]
```

### LAB 3-8
```python
s = 0
for i in range(1, 101):
    s = s + i
print(s)
# 출력: 5050

s = 0
for i in range(0, 101, 2):
    s = s + i
print(s)
# 출력: 2550

s = 0
for i in range(1, 101, 2):
    s = s + i
print(s)
# 출력: 2500
```

### LAB 3-9
```python
for i in range(7):
    s = ''
    for j in range(6-i):
        s = s + ' '
    s = s + '#'
    print(s)
# 출력:
#       #
#      #
#     #
#    #
#   #
#  #
# #
```

