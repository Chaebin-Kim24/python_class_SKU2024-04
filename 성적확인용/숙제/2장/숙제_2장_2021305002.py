# 학번: 2021305002
# 이름: 강상연

# 1
print('나의 이름은 :', '홍길동')
print('나의 나이는 :', '27')
print('나의 키는 : ', '179')
print('10 + 20 =', '30')
print('10 * 20 = ', '200')
# 2
print('원의 반지름', 8.0)
print('원의 면적', 3.14 * 8.0 * 8.0)
print('원의 둘레', 2.0 * 8.0 * 3.14)
# 3-1
radius = 8.0
print('원의 반지름', radius)
print('원의 면적', 3.14 * radius * radius)
print('원의 둘레', 2.0 * radius * 3.14)
# 3-2
radius = 10.0
print('원의 면적', 3.14 * radius * radius)
print('원의 둘레', 2.0 * radius * 3.14)
# 3-3
width = 100
height = 200
print('너비', width, ', 높이', height, '인 사각형의 면적 : ', width * height)
# 4
name = '전우치'
print('나의 이름은:', name)
age = 27
print('나의 나이는 :', age)
height = 179
print('나의 키는', height, 'cm입니다.')
sum = 10 + 20
print('10 + 20 = ', sum)
mult = 10 * 20
print('10 * 20 =', mult)
# 5-1
# global은 키워드이므로 다른것으로변경
global1 = 300
print(global1)
# 5-2
width = 20
height = 40
area = width * height
print('사각형의 면적: ', area)
# 5-3
iixxjjkk = 20
print('나의 나이는', iixxjjkk, '세 입니다')
# 에러출력 x
# 5-4
v1 = 1
v2 = 2
thisisaverylongvariablename = v1 + v2
print(thisisaverylongvariablename)
# 오류x
# 5-5
radius = 20
depth = 10
final_length = 0.5 * radius * depth
print('삼각형의 면적은 ', final_length)
# 오류 x
# 5-6
# 1st_year = 30
# 2nd_year = 30
# 3rd_year = 16
# all_years+ = 1st_year + 2nd_year + 3rd_year
# print('all_years+')
# 오류 o, 숫자로 시작하는 식별자라 사용불가
# 6
width = 20
height = 40
width = 30
area = width * height
print('사각형의 면적', area)
#사각형의 면적 1200
# 7-1
print(123 * 456)
# 56088
print(1357 + 2468)
# 3825
print(5 ** 4)
# 625
print(10 / 4)
# 2.5
print(10 // 5)
# 2
print(10 % 5)
# 0
# 7-2
print(5 % 2)
# 7-3
print(2 ** 0.5)
print(3 ** 0.5)
# 8
a = 8 + 2j
b = 4 + 3j
print(a + b)
# (12+5j)
print(a - b)
# (4-1j)
print(a * b)
# (26+32j)
print(a / b)
# (1.52-0.64j)
# 9
a = 1024
print(a >> 1)
# 512
a = 1024
a >> 1
# 512
a >> 2
# 256
a = a >> 1
a
# 512
a = a >> 1
a
# 256
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
a = a << 1
a
# 32

# 10-1
# 김유신 님이 입장하셨습니다.

# 10-2
# 80
# -20

# 10-3
radius = int(input('반지름 radius을 입력하세요 : '))
print('원의 면적 = ', 3.14 * radius * radius)
