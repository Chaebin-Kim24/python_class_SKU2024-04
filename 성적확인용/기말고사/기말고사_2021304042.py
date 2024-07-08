# 학번 2021304042
# 이름 신원철

# 1
def snake_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    num = 1

    for i in range(n):
        if i % 2 == 0:
            for j in range(n):
                matrix[i][j] = num
                num += 1
        else:
            for j in range(n - 1, -1, -1):
                matrix[i][j] = num
                num += 1

    return matrix


n = int(input("Enter a number (1 < n < 10): "))

snake = snake_matrix(n)
for row in snake:
    print(" ".join(map(str, row)))


# 2
def mean_of_n(nums):
    if not nums:
        return 0
    return sum(nums) / len(nums)

def max_of_n(nums):
    if not nums:
        return None
    return max(nums)

def min_of_n(nums):
    if not nums:
        return None
    return min(nums)

nums = list(map(int, input("정수를 여러 개 입력하시오: ").split()))

average = mean_of_n(nums)
maximum = max_of_n(nums)
minimum = min_of_n(nums)

print(f"평균값은 {average}")
print(f"최댓값은 {maximum}")
print(f"최솟값은 {minimum}")

# 3
a = [2, 3, 4, 5, 6]
rev_a = []

for i in range(len(a)):
    rev_a.append(a[len(a) - 1 - i])

print("a =", a)
print("rev_a =", rev_a)

# 4
import math


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def range_lcm(start, end):
    if start > end:
        start, end = end, start

    result_lcm = start
    for num in range(start + 1, end + 1):
        result_lcm = lcm(result_lcm, num)

    return result_lcm


start = int(input("범위의 시작 정수: "))
end = int(input("범위의 마지막 정수: "))

result = range_lcm(start, end)

print(f"{start}에서 {end}까지의 정수들의 최소 공배수는: {result}")

# 5
def format_birth(jumin):
    year = int(jumin[:2])
    month = int(jumin[2:4])
    day = int(jumin[4:6])

    if year >= 25:
        century = 1900
    else:
        century = 2000

    full_year = century + year

    return f"{full_year}년 {month}월 {day}일"

jumin = input("주민등록번호 첫 6숫자 형식 입력: ")

formatted_date = format_birth(jumin)
print(formatted_date)


# 6
s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
new_s_list = []

for item in s_list:
    if item not in new_s_list:
        new_s_list.append(item)

print(f"s_list = {s_list}")
print(f"new_s_list = {new_s_list}")
