# 학번 2021305020
# 이름 김학준

# 2
def mean_of_n(nums):
    if len(nums) == 0:
        return None
    return sum(nums) / len(nums)


def max_of_n(nums):
    if len(nums) == 0:
        return None
    return max(nums)


def min_of_n(nums):
    if len(nums) == 0:
        return None
    return min(nums)


numbers = []
print("정수를 여러 개 입력하시오 (type 'done' to finish):")

while True:
    user_input = input()
    if user_input.lower() == 'done':
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("유효한 수를 입력하시오 혹은 끝내기위해 'done'을 입력하시오 .")

if numbers:
    print(f"평균값은 {mean_of_n(numbers)}")
    print(f"최댓값은 {max_of_n(numbers)}")
    print(f"최솟값은 {min_of_n(numbers)}")
else:
    print("입력받은 정수가 없습니다.")

# 3

a = [2, 3, 4, 5, 6]

reversed_list = []

for _ in range(len(a)):
    reversed_list.append(a.pop())

print("rev_a = ", reversed_list)

# 4
import math


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


def find_lcm_range(a, b):
    lcm_value = a
    for i in range(a + 1, b + 1):
        lcm_value = lcm(lcm_value, i)
    return lcm_value


a = int(input("범위의 시작 정수 (a): "))
b = int(input("범위의 마지막 정수 (b): "))

result = find_lcm_range(a, b)
print(f" {a} 에서 {b} 까지의 정수들의 최소공배수는 : {result}")


# 5
def format_date(rrn):
    # 주민등록번호에서 생년월일 부분 추출
    year = int(rrn[:2])
    month = int(rrn[2:4])
    day = int(rrn[4:6])

    # 연도 계산
    if year >= 25:
        year += 1900
    else:
        year += 2000

    # 결과 문자열 생성
    formatted_date = f"{year}년 {month}월 {day}일"
    return formatted_date


# 사용자로부터 입력받기
rrn_input = input("주민등록번호의 앞 6자리를 입력하세요 (예: 921030): ")

# 결과 출력
print(format_date(rrn_input))

# 6

s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
new_s_list = []

for item in s_list:
    if item not in new_s_list:
        new_s_list.append(item)

print(new_s_list)
