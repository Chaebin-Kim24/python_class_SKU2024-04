# 학번 2020305036
# 이름 원종인

##################################Q-01
from functools import reduce

print("Q01")

n = int(input('정수 입력 : '))
reverse = False
for i in range(n):
    if reverse:
        for j in range(n * (i + 1) - 1, i * n - 1, -1):
            print(j, end=' ')
    else:
        for j in range(n * i, n * (i + 1)):
            print(j, end=' ')
    reverse = not reverse
    print()

###################################Q-02
print('\nQ02')


def mean_of_n(nums):  # 평군
    return reduce(lambda a, b: a + b, nums) / len(nums)


def max_of_n(nums):  # 최대
    max = nums[0]
    for i in nums:
        if max < i:
            max = i
    return max


def min_of_n(nums):
    min = nums[0]
    for i in nums:
        if min > i:
            min = i
    return min


nums = input('정수 리스트 입력 : ')
nums = [int(n) for n in nums.split()]

print(f'평균 : {mean_of_n(nums)}')
print(f'최대 : {max_of_n(nums)}')
print(f'최소 : {min_of_n(nums)}')

###################################Q-03


print('\nQ03')
a = [2, 3, 4, 5, 6]
tmp = a
rev_a = []

for _ in range(len(a)):
    rev_a.append(a.pop())
print(f'a = {tmp}')
print(f'rev_a = {rev_a}')

####################################Q-04
print('\nQ04')


def maxDiv(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def minMult(a, b):
    return a * b / maxDiv(a, b)


start = int(input('시작정수 : '))
end = int(input('끝 정수 : '))
print(f'{start}부터 {end}까지 정수의 최소공배수는 {int(reduce(minMult, range(start, end + 1)))}')

###################################Q-05
print('\nQ05')
birth = int(input('주민등록번호 첫 6숫자 형식 입력 : '))
day = birth % 100
birth /= 100
month = int(birth % 100)
birth /= 100
birth = int(birth)
if birth < 25:
    print(f'20{birth}년 {month}월 {day}일')
else:
    print(f'19{birth}년 {month}월 {day}일')