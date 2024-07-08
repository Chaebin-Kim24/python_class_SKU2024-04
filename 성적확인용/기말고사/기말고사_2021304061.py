#학번 2021304061
#이름 이지민

문제 1번
n = int(input("n을 입력하시오: "))
num = 0
arr = [[col+row*n for col in range(1, (n+1))] for row in range(n)]


for i in range(0, n):
    if i % 2 == 1:
        print(arr[i][::-1], end=" ")
    else:
        print(arr[i][::1], end=" ")
    print()

문제 2
def mean_of_n(nums):
    return sum(nums) / len(nums)

def max_of_n(nums):
    return max(nums)

def min_of_n(nums):
    return min(nums)

# 사용자 입력 받기
print("정수를 여러 개 입력하시오 : ", end="")
nums = [int(x) for x in input().split()]

# 함수 호출 및 결과 출력
print("평균값은 {:.1f}".format(mean_of_n(nums)))
print("최댓값은 {}".format(max_of_n(nums)))
print("최솟값은 {}".format(min_of_n(nums)))

def find_lcm(a, b):
    # 최대공약수를 구하는 함수
    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x

    # 최소공배수를 구하는 함수
    def lcm(x, y):
        return (x * y) // gcd(x, y)

    # a와 b 사이의 모든 정수들의 최소공배수를 구하는 함수
    min_lcm = a
    for i in range(a + 1, b + 1):
        min_lcm = lcm(min_lcm, i)
    return min_lcm

a = int(input("범위의 시작 정수 : "))
b = int(input("범위의 마지막 정수 : "))

print(f"2에서 4까지의 정수들의 최소 공배수는 : {find_lcm(a, b)}")

문제 4
def find_lcm(a, b):
    # 최대공약수를 구하는 함수
    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x

    # 최소공배수를 구하는 함수
    def lcm(x, y):
        return (x * y) // gcd(x, y)

    # a와 b 사이의 모든 정수들의 최소공배수를 구하는 함수
    min_lcm = a
    for i in range(a + 1, b + 1):
        min_lcm = lcm(min_lcm, i)
    return min_lcm

a = int(input("범위의 시작 정수 : "))
b = int(input("범위의 마지막 정수 : "))

print("2에서 4까지의 정수들의 최소 공배수는 :", find_lcm(a, b))

문제 5

def print_date(birth_date):
    year = int(birth_date[:2])
    month = int(birth_date[2:4])
    day = int(birth_date[4:])

    if year < 25:
        year += 2000
    else:
        year += 1900

    print(year,"년",month,"월",day,"일")

birth_date = input("주민등록번호 첫 6숫자 형식 입력 : ")
print_date(birth_date)

문제 6
#include <stdio.h>
def mean_of_n(nums):
    return sum(nums) / len(nums)

def max_of_n(nums):
    return max(nums)

def min_of_n(nums):
    return min(nums)

# 사용자 입력 받기
print("정수를 여러 개 입력하시오 : ", end="")
nums = [int(x) for x in input().split()]

# 함수 호출 및 결과 출력
print("평균값은 {:.1f}".format(mean_of_n(nums)))
print("최댓값은 {}".format(max_of_n(nums)))
print("최솟값은 {}".format(min_of_n(nums)))

