# 학번: 2021304071
# 이름: 장민혁

#교과서 문제를 풀었습니다.

#LAB 2-1
print('나의 이름은 :', '홍길동')
print('나의 나이는 :', '27')
print('나의 키는 :', 179, 'cm 입니다')
print('10 + 20 =', 10 + 20)
print('10 * 20 = ', 10 * 20)

#LAB 2-2
print('원의 반지름', 8.0)
print('원의 면적', 3.14 * 8.0 * 8.0)
print('원의 둘레', 2.0 * 3.14 * 8.0)

#LAB 2-3
#1.
radius = 8.0
print('원의 반지름', radius)
print('원의 면적', 3.14 * radius * radius)
print('원의 둘레', 2.0 * 3.14 * radius)

#2
radius = 10.0
print('원의 반지름', radius)
print('원의 면적', 3.14 * radius * radius)
print('원의 둘레', 2.0 * 3.14 * radius)

#3
width = 100
height = 200
print('너비 100, 높이 200인 사각형의 면적 : ', width * height)

#LAB 2-4
name = '전우치'
print('나의 이름은 :', name)
age = 27
print('나의 나이는 :', age)
height = 179
print('나의 키는 :', height, 'cm 입니다')
sum = 10 + 20
print('10 + 20 =', sum)
mult = 10 * 20
print('10 * 20 = ', mult)

#LAB 2-5
#1
#global은 파이썬의 키워드이므로 식별자로 사용 불가함. 따라서 다른 식별자 사용
nice = 300
print(nice)

#2
width = 20
height = 40
area = ( width * height ) #교제에서는 area = ( width * Height )로 앞에서 선언한 식별자와 달리 대문자를 사용했다. 파이썬은 대소문자가 구분되므로 오류가 발생
print('사각형의 면적 :', area)

#3
iixxjjkk = 20
print('나의 나이는', iixxjjkk, '세 입니다')
# 1) 이 코드는 에러를 출력하지 않는다.
# 2) 이 코드는 i,l 혹은 o,0과 같은 구분하기 힘든 문자를 사용하였다.

#4
v1 = 1
v2 = 2
thisissaverylongvariablename = v1 + v2
print(thisissaverylongvariablename)
# 1) 이 코드는 에러를 출력하지 않는다.
# 2) 이 코드의 문제점은 시별자 이름이 단어의 연결을 밑줄이나 대문자로 구분하지 않아 알아보기 어렵다.

#5
radius = 20
depth = 10
final_length = 0.5 * radius * depth
print('삼각형의 면적은 ', final_length)
# 1) 이 코드는 에러를 출력하지 않는다.
# 2) 

#6
# 1) 이 코드는 에러를 출력한다
# 2) 이 코드의 문제점은 식별자들의 첫 글자가 숫자로 시작되었고, 특수기호가 사용된 것이다.
first_year = 30
second_year = 30
third_year = 16
all_years = first_year + second_year + third_year
print(all_years)

#LAB 2-6
width = 20
height = 40
width = 30
area = width * height
print('사각형의 면적', area)
# width 변수의 값이 30으로 재지정 되어 area= 30 * 40, 1200이 될 것이다.

#LAB 2-7
#1
 # 1)
print(123 * 456) #56088
 # 2)
print(1357 + 2468) #3825
 # 3)
print(5 ** 4) #625
 # 4)
print(10 / 4) #2.5
 # 5)
print(10 // 5) #2
 # 6)
print(10 % 5) #0

#2
print(5 % 2)

#3
print(2 ** 0.5) #1.4142135623730951
print(3 ** 0.5) #1.7320508075688772

#LAB 2-8
a = 8 + 2j
b = 4 + 3j
print(a + b) #(12+5j)
print(a - b) #(4-1j)
print(a * b) #(26+32j)
print(a / b) #(1.52-0.64j)

#LAB 2-9
#1
a = 1024
print(a >> 1) #512
print(a >> 2) #256
a = a >> 1
print(a) #512
a = a >> 1
print(a) #256
a = 1
print(a << 1) #2
a = a << 1
print(a) #2
a = a << 1
print(a) #4
a = a << 1
print(a) #8
a = a << 1
print(a) #16

#LAB 2-10
# 1
name = input('이름을 입력하세요 : ')
#김유신
print(name, '님이 입장하셨습니다.')
#김유신 님이 입장하셨습니다.

# 2
m = int(input('숫자 m을 입력하세요 : '))
# m=30
n = int(input('숫자 n을 입력하세요 : '))
# n=50
print('m + n =', m + n)
#80
print('m - n =', m - n)
#-20

# 3
radius = int(input('원의 반지름을 입력하세요 : '))
print('원의 면적은 : ', 3.14 * radius ** 2)
