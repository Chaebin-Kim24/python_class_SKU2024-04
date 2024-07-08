# 학번 2021304085
# 이름 홍세헌

문제1
def snake_body(n) :
    body = [[0]* n for _ in range(n)]

    count = 1

    for a in range(n) :
        if a % 2 == 0 :
            for b in range(n) :
                body[a][b] = count
                count += 1
        else:
	for b in range(n - 1, -1, -1) :
	    body[a][b] = count
	    count += 1

    return body

while True:
    n = int(input("n을 입력하시오 : "))
    if 1 < n < 10 :
        break
    else :
        print("n을 입력하시오 : ")
        except ValueError :

result = snake_body(n)


문제2
def main() :
    nums = input_numbers()

    if nums :
        average = mean_of_n(nums)
        maximum = max_of_n(nums)
        minimum = min_of_n(nums)

        printf("정수를 여러 개 입력하시오 : {nums}")
        printf("평균값은: {average}")
        printf("최댓값은: {maximum}")
        printf("최솟값은: {minimum}")
    else:
print("입력된 숫자가 없습니다.")


문제3
a = [2, 3, 4, 5, 6]

order = []

for _ in range(len(a)) :
     order.append(a.pop())

     a = order

  print("rev_a = []", a)


문제4
import math

def math(x, y) :
    return abs(x * y)

    def find_smallest_multiple(a, b) :
    result_math = a
    for i in range(a + 1, b + 1) :
        result_math = math(result_math, i)

        return result_math

        a = int(input("범위의 시작 정수 : "))
        b = int(input("범위의 마지막 정수 : "))

        result = find_smallest_multiple(a, b)

        printf("{a}에서 {b}까지의  정수들의 최소 공배수는 : ", result)
