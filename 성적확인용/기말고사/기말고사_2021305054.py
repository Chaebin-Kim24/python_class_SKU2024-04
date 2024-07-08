# 학번 2021305054
# 이름 이승언

# 1
n = int(input("n을 입력하세요"))
if n < 1 or n >= 10:
    print("n 은 1보다 크고 10보다 작아야 함")
else:
    result = []
    current_num = 1
    for i in range(n):
        row = list(range(current_num, current_num + n))

        if i % 2 == 1:
            row = row[::-1]
            result.append(row)
            current_num += n

    for row in result:
        print(' '.join(map(str, row)))

'''
#2
def means_of_n(nums):
    return sum(nums) / len(nums)

def max_of_n(nums):
    return max(nums)

def min_of_n(nums):
    return min(nums)

num = input("정수를 여러 개 입력하시오: ")
num_l = list(map(int,num.split()))

av = means_of_n(num_l)
ma = max_of_n(num_l)
mi = min_of_n(num_l)

print("평균값은",av)
print("최댓값은",ma)
print("최솟값은",mi)
'''

'''
#3
a = [2, 3, 4, 5, 6]
rev_a = []

print("a =",a)

for i in range(len(a)):
    rev_a.append(a.pop())
print("reverse_a =",rev_a)

'''

'''
#4
import math

def Max(x, y):
    while y:
        x, y = y, x % y
    return x
def Min(x, y):
    return x * y // Max(x, y)

a = int(input("범위의 시작 정수: "))

b = int(input("범위의 마지막 정수: "))

result = a
for i in range(a + 1, b + 1):
    result = Min(result, i)

print(a,"에서",b,"까지의 정수들의 최소 공배수는:",result)
'''