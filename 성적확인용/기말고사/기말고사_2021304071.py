# 학번 2021304071
# 이름 장민혁

# 문제1
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


def print_matrix(matrix):
    for row in matrix:
        print('\t'.join(map(str, row)))


n = int(input("insert n: "))
if 1 < n < 10:
    result_matrix = snake_matrix(n)
    print_matrix(result_matrix)
else:
    print("Input value is out of range")


# 문제2
def mean_of_n(nums):
    if not nums:
        return 0
    return sum(nums) / len(nums)


def max_of_n(nums):
    if not nums:
        return float('-inf')
    return max(nums)


def min_of_n(nums):
    if not nums:
        return float('inf')
    return min(nums)


def main():
    user_input = input("Enter multiple integers: ")

    nums = list(map(int, user_input.split()))

    mean_value = mean_of_n(nums)
    max_value = max_of_n(nums)
    min_value = min_of_n(nums)

    print(f"average value is {mean_value}")
    print(f"maximum value is {max_value}")
    print(f"minimum value is {min_value}")


if __name__ == "__main__":
    main()

# 문제3
a = [2, 3, 4, 5, 6]
a_copy = a[:]
rev_a = []

for _ in range(len(a_copy)):
    rev_a.append(a_copy.pop())

print(f"a = {a}")
print(f"rev_a = {rev_a}")

# 문제4
import math


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    return x * y // gcd(x, y)


def lcm_of_range(a, b):
    lcm_value = a
    for num in range(a + 1, b + 1):
        lcm_value = lcm(lcm_value, num)
    return lcm_value


a = int(input("starting integer: "))
b = int(input("Last integer: "))

result = lcm_of_range(a, b)

print(f"minimum common multiple of integers from {a} to {b} is: {result}")


# 문제5
def parse_Resident_number(Resident):
    year = int(Resident[:2])
    month = int(Resident[2:4])
    day = int(Resident[4:6])

    if year >= 0 and year <= 24:
        full_year = 2000 + year
    else:
        full_year = 1900 + year

    return f"{full_year}year {month}month {day}day"


Resident = input("Enter the first six digits of Resident registration number : ")

formatted_date = parse_Resident_number(Resident)
print(formatted_date)