# 학번 2021304065
# 이름 이태희

# 1

def snake(n):
    array = [[0] * n for _ in range(n)]
    num = 1

    for i in range(n):
        for j in range(n):
            array[i][j if i % 2 == 0 else n - 1 - j] = num
            num += 1

    return array


n = int(input('n을 입력하시오 : '))
if n > 1 and n < 10:
    result = snake(n)
    for row in result:
        print(' '.join(f'{num:2d}' for num in row))
else:
    print('1<n<10')


# 2

def mean_of_n(nums):
    return sum(nums) / len(nums)


def max_of_n(nums):
    return max(nums)


def min_of_n(nums):
    return min(nums)


nums = list(map(float, input('정수를 여러 개 입력하시오: ').split()))

if nums:
    print(f'평균값: {mean_of_n(nums)}')
    print(f'최댓값: {max_of_n(nums)}')
    print(f'최솟값: {min_of_n(nums)}')
else:
    print('다시 입력하시오.')

# 3

a = [2, 3, 4, 5, 6]
rev_a = []

temp_a = a.copy()

for _ in range(len(temp_a)):
    rev_a.append(temp_a.pop())

print(a)
print(rev_a)

# 4

import math


def least(x, y):
    return x * y // math.gcd(x, y)


def least_in_range(a, b):
    result = a
    for i in range(a + 1, b + 1):
        result = least(result, i)
    return result


a = int(input('범위의 시작 정수 : '))
b = int(input('범위의 마지막 정수 : '))

if a < b:
    answer = least_in_range(a, b)
    print(f'{a}에서 {b}까지의 정수들의 최소 공배수는 : {answer}')
else:
    print('a<b')


# 5

def convert_id(id_number):
    year = int(id_number[:2])
    month = int(id_number[2:4])
    day = int(id_number[4:6])

    if year >= 25:
        year += 1900
    else:
        year += 2000

    date = f"{year}년 {month}월 {day}일"
    return date


id_number = input('주민등록번호 첫 6숫자 형식 입력: ')
print(convert_id(id_number))

# 6

s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
new_s_list = []

for item in s_list:
    if item not in new_s_list:
        new_s_list.append(item)

print(f's_list = {s_list}')
print(f'new_s_list = {new_s_list}')



