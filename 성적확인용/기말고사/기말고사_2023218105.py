# 학번 2023218105
# 이름 정서연


# 1.
def print_snake_matrix(n):
    # n x n 크기의 뱀 행렬 초기화
    snake_matrix = [[0] * n for _ in range(n)]
    num = 1  # 시작 숫자
    for i in range(n):
        if i % 2 == 0:
            # 짝수 번째 행: 왼쪽에서 오른쪽으로 채우기
            for j in range(n):
                snake_matrix[i][j] = num
                num += 1
        else:
            # 홀수 번째 행: 오른쪽에서 왼쪽으로 채우기
            for j in range(n - 1, -1, -1):
                snake_matrix[i][j] = num
                num += 1
    # 결과 출력
    for row in snake_matrix:
        print('\t'.join(map(str, row)))

def main1():
    # 사용자로부터 n 입력 받기
    n = int(input("n을 입력하시오 : "))

    # 뱀 행렬 출력
    print_snake_matrix(n)


if __name__ == "__main__":
    main1()


# 2.
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

def main2():
    # 사용자로부터 정수 여러 개 입력 받기
    print("정수를 여러 개 입력하시오 : ", end="")
    nums = list(map(int, input().split()))
    # 평균값, 최댓값, 최솟값 계산
    avg = mean_of_n(nums)
    maximum = max_of_n(nums)
    minimum = min_of_n(nums)
    # 결과 출력
    print(f"평균값은 {avg}")
    print(f"최댓값은 {maximum}")
    print(f"최솟값은 {minimum}")


if __name__ == "__main__":
    main2()


# 3.
a = [2, 3, 4, 5, 6]
# 새로운 리스트 rev_a 초기화
rev_a = []
length = len(a)
# a 리스트의 원소를 pop() 메소드를 사용하여 역순으로 rev_a 리스트에 추가
for _ in range(length):
    rev_a.append(a.pop())
# 결과 출력
print(f"a = {a}")
print(f"rev_a = {rev_a}")


# 4.
from math import gcd

# 두 숫자의 최소 공배수를 구하는 함수
def lcm(x, y):
    return x * y // gcd(x, y)


# 범위 [a, b]의 모든 숫자의 최소 공배수를 구하는 함수
def find_lcm_in_range(a, b):
    result = a
    for i in range(a + 1, b + 1):
        result = lcm(result, i)
    return result


def main4():
    # 사용자로부터 두 정수 입력 받기
    a = int(input("범위의 시작 정수: "))
    b = int(input("범위의 끝 정수: "))
    # a가 b보다 작아야 함
    if a < b:
        result = find_lcm_in_range(a, b)
        print(f"{a}에서 {b}까지 범위의 모든 정수의 배수이면서 가장 작은 값은 {result}입니다.")
    else:
        print("범위의 시작 정수가 끝 정수보다 작아야 합니다. 다시 입력하세요.")
if __name__ == "__main__":
    main4()


# 5,
def parse_rrn(rrn):
    # 입력된 주민등록번호 앞 6자리 분리
    year = int(rrn[:2])
    month = int(rrn[2:4])
    day = int(rrn[4:6])
    # 1900년대와 2000년대 구분
    if year >= 25:
        year += 1900
    else:
        year += 2000
    # 결과 출력
    print(f"{year}년 {month}월 {day}일")

def main5():
    # 사용자로부터 주민등록번호 첫 6자리 입력 받기
    rrn = input("주민등록번호 첫 6숫자 형식 입력 : ")

    # 입력 형식 검증
    if len(rrn) == 6 and rrn.isdigit():
        parse_rrn(rrn)
    else:
        print("올바른 형식의 주민등록번호 6자리를 입력하세요.")


if __name__ == "__main__":
    main5()


# 6.
s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
new_s_list = []
for item in s_list:
    if item not in new_s_list:
        new_s_list.append(item)
print(f"s_list = {s_list}")
print(f"new_s_list = {new_s_list}")
