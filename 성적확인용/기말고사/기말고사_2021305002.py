#학번 2021305002
#이름 강상연

1.
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
        print("\t".join(map(str, row)))

# Example usage:
n = int(input("n을 입력하시오: "))
if 1 < n < 10:
    result = snake_matrix(n)
    print_matrix(result)
else:
    print("Input must be greater than 1 and less than 10.")
2.
def mean_of_n(nums):
    return sum(nums) / len(nums)

def max_of_n(nums):
    return max(nums)

def min_of_n(nums):
    return min(nums)

# Example usage:
nums = list(map(int, input("정수를 여러 개 입력하시오: ").split()))
print(f"평균값은 {mean_of_n(nums)}")
print(f"최댓값은 {max_of_n(nums)}")
print(f"최솟값은 {min_of_n(nums)}")
3.
def reverse_list(a):
    rev_a = []
    for _ in range(len(a)):
        rev_a.append(a.pop())
    return rev_a

# Example usage:
a = [2, 3, 4, 5, 6]
rev_a = reverse_list(a.copy())
print(f"a = {a}")
print(f"rev_a = {rev_a}")
4.
from math import gcd
from functools import reduce

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_range(start, end):
    return reduce(lcm, range(start, end + 1))

# Example usage:
start = int(input("범위의 시작 정수: "))
end = int(input("범위의 마지막 정수: "))
print(f"{start}에서 {end}까지의 정수들의 최소 공배수는: {lcm_range(start, end)}")
5.
def format_rrn(rrn):
    year = int(rrn[:2])
    if year < 25:
        year += 2000
    else:
        year += 1900
    month = int(rrn[2:4])
    day = int(rrn[4:6])
    return f"{year}년 {month}월 {day}일"

# Example usage:
rrn = input("주민등록번호 첫 6숫자 형식 입력: ")
print(format_rrn(rrn))
6.
def remove_duplicates(s_list):
    new_s_list = []
    for item in s_list:
        if item not in new_s_list:
            new_s_list.append(item)
    return new_s_list

# Example usage:
s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
new_s_list = remove_duplicates(s_list)
print(f"s_list = {s_list}")
print(f"new_s_list = {new_s_list}")
