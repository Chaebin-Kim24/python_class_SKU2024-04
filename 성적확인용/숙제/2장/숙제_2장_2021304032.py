# 학번: 2021304032
# 이름: 박지원

# LAB 2-1
print('나의 이름은 :', '홍길동')
print('나의 나이는 :', 27)
print('나의 키는 :', 179, 'cm 입니다.')
print('10 + 20 =', 10 + 20)
print('10 * 20 =', 10 * 20)
# LAB 2-2
print('원의 반지름', 8.0)
print('원의 면적', 3.14 * 8.0 * 8.0)
print('원의 둘레', 2.0 * 3.14 * 8.0)
# LAB 2-3
# 2-3 1)
radius = 8.0
print('원의 반지름', radius)
print('원의 면적', 3.14 * radius * radius)
print('원의 둘레', 3.14 * 2.0 * radius)
# 2-3 2)
radius = 10.0
print('원의 반지름', radius)
print('원의 면적', 3.14 * radius * radius)
print('원의 둘레', 3.14 * 2.0 * radius)
# 2-3 3)
width = 100
height = 200
area = width * height
print('너비', width , '높이', height, '인 사각형의 면적 :', area)
# LAB 2-4
name = '전우치'
print('나의 이름은:', name)
age = 27
print('나의 나이는 :', age)
height = 179
print('나의 키는 :', height)
sum = 10 + 20
print('10 + 20 = ', sum)
mult = 10 * 20
print('10 * 20 = ', mult)
# LAB 2-5
# 2-5 1)
# global = 300
# print(global)
# number = 300
# print(number)
#global은 사용 용도가 정해져 있어서 식별자로 사용할 수 없다.
# 2-5 2)
width = 20
height = 40
area = (width * height)
print('사각형의 면적', area)
#에러 발생 X
# 2-5 3)
iixxjjkk = 20
print('나의 나이는', iixxjjkk, '세 입니다')
#1) 에러 발생 X
#2) 식별자가 무엇을 가르키는지 명확하지 않음
# 2-5 4)
v1 = 1
v2 = 2
thisissaverylongvariablename = v1 + v2
print(thisissaverylongvariablename)
#1) 에러 발생 X
#2) 식별자의 명칭이 너무 길다
# 2-5 5)
radius = 20
depth = 10
final_length = 0.5 * radius * depth
print('삼각형의 면적은', final_length)
#1) 에러 발생 X
#2) 식별자의 명칭과 결과값이 가리키는 것이 다름
# 2-5 6)
# 1st_year = 30
# 2nd_year = 30
# 3rd_year = 16
# all_years+ = 1st_year + 2nd_year + 3rd_year
# print(all_years+)
#1) 에러 발생
#2) 식별자의 첫 글자는 반드시 문자나 밑줄 문자로 시작해야함
# LAB 2-6
width = 20
height = 40
width = 30
area = width * height
print('사각형의 면적', area)
# 먼저 선언한 width = 20이 너비로써 계산되지 않고 이후 재선언한 width = 30이 너비의 값이 되어 30 x 40 = 1200의 값이 나온다
# LAB 2-7
# 2-7 1)
123 * 456
1357 +  2468
5 ** 4
10 / 4
10 // 5
10 % 5
# 2-7 2)
5 % 2
# 2-7 3)
2 ** 0.5
3 ** 0.5
# LAB 2-8
a = 8 + 2j
b = 4 + 3j
a + b
a - b
a * b
a / b
# LAB 2-9
a = 1024
a >> 1
a >> 2
a = a >> 1
a
a = a >> 1
a
a = 1
a << 1
a = a << 1
a
a = a << 1
a
a = a << 1
a
a = a << 1
a
# LAB 2-10
# 2-10 2)
name = input('이름을 입력하세요 : ')
print(name, '님이 입장하셨습니다.')
# 2-10 1)
m = int(input('숫자 m을 입력하세요 : '))
n = int(input('숫자 n을 입력하세요 : '))
print('m + n =', m + n)
print('m - n =', m - n)
