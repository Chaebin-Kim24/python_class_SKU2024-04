# 학번 2021304053
# 이름 윤영주

# #1번 문제
n = int(input("n을 입력하시오: "))

matrix = [[0] * n for _ in range(n)]

num = 1
for i in range(n):
    if i % 2 == 0:
        matrix[i] = list(range(num, num + n))
    else:
        matrix[i] = list(range(num + n - 1, num - 1, -1))
    num += n

for row in matrix:
    print(' '.join(map(str, row)))


# #2번 문제
from functools import reduce

n = int(input("정수를 여러개 입력하시오 : "))

n = [3, 45, 32, 5,	7,	8,	4,	44,	5,	90,	17]



print(n)
print('평균값 : {}\n 최댓값 : {}\n최솟값 : {}'.format(mean_of_n(n_list), max_of_n(n_list), min_of_n(n_list)))

def mean_of_n(nums)(lst):
    return reduce(lambda x, y: x + y, lst) / len(lst)

def max_of_n(nums)(list):
    cur = 0
    for i in lst:
        if cur < i:
            cur = i

    return cur

def max_of_n(nums)(lst):
    cur = max_of_n(nums)(lst)
    for i in lst:
        if cur > i:
            cur = i

    return cur

print(n_list)
print('최댓값 : {}\n최솟값 : {}'.format(max_of_n(nums)(n_list), min_of_n(nums)(n_list)))


# #3번 문제
a = [2, 3, 4, 5, 6]
rev_a = []

for _ in range(len(a)):
    rev_a.append(a.pop())

a = rev_a

print("a = ", a)
print("rev_a = ", reversed_a)


# #4번 문제
import math


a = int(input("범위의 시작 정수 (a): "))
b = int(input("범위의 마지막 정수 (b): "))

if a > b:
    print ("a가 b보다 작아야 합니다.")

else:
    a < b
    #a, b 사이의 모든 숫자 최소공배수
    최소공배수 = abs(a * b) // math.gcd(a, b)

print(a, "에서", b, "까지의 최소공배수는 : ", 최소공배수)


# #5번 문제
from datetime import datetime

def convert_date(wnals_number):
    year = int(wnals_number[:2])
    month = int(wnals_number[2:4])
    day = int(wnals_number[4:6])

    if year >= 25:
        year += 1900
    else:
        year += 2000

    date = datetime(year, month, day)
    formatted_date = date.strftime("%Y년 %m월 %d일")

    return formatted_date

wnals_number = input("주민등록번호 첫 6숫자 형식 입력: ")
formatted_date = convert_date(wnals_number)
print(formatted_date)

# #6번 문제
s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
new_s_list = []

for s in s_list:
    if s not in new_s_list:
        new_s_list.append(s)

print("s_list = ", s_list)
print("new_s_list = ", new_s_list)


