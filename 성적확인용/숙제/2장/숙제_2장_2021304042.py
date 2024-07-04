# 학번: 2021304042
# 이름: 신원철

# LAB 2-1
print('나의 이름은 :', '홍길동')
print('나의 나이는 :', 27)
print('10+20=', 10+20)
print('10*20=',10*20)

# LAB 2-2
print('원의 반지름', 8.0 )
print('원의 면적', 3.14*8.0*8.0)
print('원의 둘레',  2.0*8.0*3.14 )

# LAB 2-3-1
radius = 8.0
print('원의 반지름', radius)
print('원의 면적', 3.14*radius*radius )
print('원의 둘레', 2.0 * 3.14 * radius )

# LAB 2-3-2
radius = 10.0
print('원의 반지름', radius)
print('원의 면적', 3.14*radius*radius )
print('원의 둘레', 2.0 * 3.14 * radius )

# LAB 2-3-3
radius = 10.0
print('원의 반지름', radius)
print('원의 면적', 3.14*radius*radius )
print('원의 둘레', 2.0 * 3.14 * radius )

# LAB 2-4
name = '전우치'
print('나의 이름은 :', name)
age = 27
print('나의 나이는 :', age )
height = 179
print('나의 키는', height, 'cm 입니다.' )
sum = 10 + 20
print('10 + 20 =', sum)
mult = 10 * 20
print('10 * 20 =', mult )

# LAB 2-5
# 1.문제가 발생한다. global을 다른 단어로 바꿔야한다.
# 2.area의 식에 높이 너비 단어의 첫 글자가 대문자이다.
width= 20
height = 40
area=(width * height)
print('사각형의 면적', area)
# 3.아니오, 출력값의 문장에 띄어쓰기가 제대로 안되어있다.
# 4.아니오, 식별자 이름은 밑줄로 띄어쓴다.
# 5.아니오, 삼각형은 반지름이 존재하지 않는다.
# 6.예, 식별자에 +같은 특수기호는 사용 불가능하다.

# LAB 2-6
# 사각형의 면적 1200

# LAB 2-7
# 1.
123 * 456
# 56088
1357 + 2468
# 3825
5 ** 4
# 625
10 / 4
# 2.5
10 // 5
# 2
10 % 5
# 0

# 2.
1, 5 % 2

# 3.
2 ** 0.5, 3 ** 0.5

# LAB 2-8
a = 8 + 2j
b = 4 + 3j
a+b
# (12+5j)
a-b
# (4-1j)
a*b
# (26+32j)
a/b
# (1.52-0.64j)

# LAB 2-9
a = 1024
a >> 1
# 512

a >> 2
# 256

a = a >> 1
a
# 512

a = 1
a << 1
# 2

a = a << 1
a
# 2

a = a << 1
a
# 4

a = a << 1
a
# 8

a = a << 1
a
# 16

# LAB 2-10
# 1. 김유신님이 입장하셨습니다.
# 2. 80, -20
# 3.
radius = int(input('반지름을 입력하세요: '))
circle= radius * radius * 3.14
print('원의 면적은 ', circle)
