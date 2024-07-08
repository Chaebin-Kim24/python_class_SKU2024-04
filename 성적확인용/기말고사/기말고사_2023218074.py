# 학번 2023218074
# 이름 이서연

1.
def s_matrix(n):
    matrix = []
    count = 1
    for i in range(n):
        row = []
        if i % 2 == 0:
            for j in range(n):
                row.append(count)
                count += 1
        else:
            for j in range(n - 1, -1, -1):
                row.append(count)
                count += 1
        matrix.append(row)

    return matrix


n = int(input("n을 입력하시오: "))
result = s_matrix(n)

for row in result:
    print("\t".join(map(str, row)))

2.


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


input_str = input("정수를 여러 개 입력하시오: ")
nums = list(map(int, input_str.split()))

average = mean_of_n(nums)
print(f"avg is {평균값은 .1f}")

maximum = max_of_n(nums)
print(f"최댓값은 {maximum}")

minimum = min_of_n(nums)
print(f"최솟값은 {minimum}")

3.
a = [2, 3, 4, 5, 6]
rev_a = []
print(f"a = {a}")

for _ in range(len(a)):
    rev_a.append(a.pop())

print(f"rev_a = {rev_a}")

4.

import math


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


def lcm_range(a, b):
    current_lcm = a
    for i in range(a + 1, b + 1):
        current_lcm = lcm(current_lcm, i)
    return current_lcm


start = int(input("범위의 시작 정수 : "))
end = int(input("범위의 마지막 정수 : "))

result_lcm = lcm_range(start, end)
print(f"{start}에서 {end}까지의 최소공배수는 : {result_lcm}")

5.


def convert_to_date(jumin):
    year = int(jumin[:2])
    month = int(jumin[2:4])
    day = int(jumin[4:6])

    if year >= 25:
        full_year = 1900 + year
    else:
        full_year = 2000 + year

    return f"{full_year}년 {month}월 {day}일"


jumin = input("주민등록번호 첫 6숫자 형식 입력 : ")

result = convert_to_date(jumin)
print(result)

6.

s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
new_s_list = []

for item in s_list:
    if item not in new_s_list:
        new_s_list.append(item)

print("s_list =", s_list)
print("new_s_list =", new_s_list)






