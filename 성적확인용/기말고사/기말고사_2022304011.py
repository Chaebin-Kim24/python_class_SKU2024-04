# 학번 2022304011
# 이름 김수연


# 문제 1
def 뱀_행렬(n):
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


n = int(input())
while n <= 1 or n >= 10:
    n = int(input())
result = 뱀_행렬(n)


# 문제 2
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


def main():
    nums = list(map(int, input("정수를 여러 개 입력하시오 : ").split()))

    if not nums:
        print("입력된 숫자가 없습니다.")
    return

    평균값 = mean_of_n(nums)
    최댓값 = max_of_n(nums)
    최솟값 = min_of_n(nums)

    print(f"평균값은 {average:.1f}")
    print(f"최댓값은 {maximum}")
    print(f"최솟값은 {minimum}")


if __name__ == "__main__":
    main()

# 문제 3
a = [2, 3, 4, 5, 6]
rev_a = []
while a:
    rev_a.append(a.pop())
print(f"a = {a}")
print(f"rev_a = {rev_a}")


# 문제 4
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    return (x * y) // gcd(x, y)


a = int(input("범위의 시작 정수 : "))
b = int(input("범위의 마지막 정수 : "))
최소공배수 = a
for num in range(a + 1, b + 1):
    최소공배수 = lcm(최소공배수, num)
print(f"{a}에서 {b}까지의 정수들의 최소 공배수는 : {최소공배수}")


# 문제 5
def format_birthday(num):
    생년 = int(num[:2])
    생월 = int(num[2:4])
    생일 = int(num[4:6])
    if 생년 >= 25:
        생년 += 1900
    else:
        생년 += 2000
    return f"{생년}년 {생월}월 {생일}일"
    num = input("주민등록번호 첫 6숫자 형식 입력 : ")


print(format_birthday(num))

# 문제 6
s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
new_s_list = []
for element in s_list:
    if element not in new_s_list:
        new_s_list.append(element)
print("s_list =", s_list)
print("new_s_list =", new_s_list)