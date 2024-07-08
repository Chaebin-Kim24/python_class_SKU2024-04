# 학번 2021304032
# 이름 박지원

문제 1번


def snake_array(n):
    if n >= 10 or n <= 1:
        raise ValueError('n은 1보다 크고 10보다 작은 값')

    array = [[0] * n for _ in range(n)]
    num = 1
    for i in range(n):
        if i % 2 == 0:
            for j in range(n):
                array[i][j] = num
                num += 1
        else:
            for j in range(n - 1, -1, -1):
                array[i][j] = num
                num += 1
    return array


def print_array(array):
    for row in array:
        print(' '.join(map(str, row)))


# 사용자에게 직접 입력 받기
n = int(input('1보다 크고 10보다 작은 값을 입력하세요: '))
snake_array = snake_array(n)
print_array(snake_array)

문제 2번


def mean_of_n(nums):
    return sum(nums) / len(nums)


def max_of_n(nums):
    return max(nums)


def min_of_n(nums):
    return min(nums)


def main():
    nums = []
    print('정수를 여러 개 입력하시오 : ')
    while True:
        user_input = input()

    if nums:
        print(f'평균값은: {mean_of_n(nums)}')
        print(f'최댓값은: {max_of_n(nums)}')
        print(f'최솟값은: {min_of_n(nums)}')
    else:
        print('입력된 숫자가 없습니다.')


if __name__ == '__main__':
    main()

문제 3번

a = [2, 3, 4, 5, 6]
rev_a = []

# 리스트 a의 원소를 하나씩 pop()하여 rev_a에 추가
for _ in range(len(a)):
    rev_a.append(a.pop())

print('a =', a)
print('rev_a =', rev_a)

문제 4번

import math


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    return x * y // gcd(x, y)


def lcm_range(a, b):
    result = a
    for num in range(a + 1, b + 1):
        result = lcm(result, num)
    return result


# 사용자에게 직접 입력 받기
a = int(input('첫 번째 정수를 입력하세요 (a < b): '))
b = int(input('두 번째 정수를 입력하세요 (a < b): '))

# 결과 출력
print(f'범위의 시작 정수 : ', a)
print(f'범위의 마지막 정수 : ', b)
print(f'{a}에서 {b}까지의 정수들의 최소공배수는 : {lcm_range(a, b)}')



