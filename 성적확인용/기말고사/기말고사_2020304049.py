# 학번 2020304049
# 이름 윤치경


#문제 1
n = int(input('n을 입력하시오 : '))
for x in range(n):
    if x % 2 == 0:
        for y in range(1, n + 1):
            print('{:3}'.format(y + n * x), end='')
    else:
        for y in range(n, 0, -1):
            print('{:3}'.format(y + n * x), end='')

    print('')


#문제 2
def mean_of_n(nums):
    sum = 0
    for n in nums:
        sum += int(n)

    return sum / len(nums)


def max_of_n(nums):
    max = 0
    for n in nums:
        if int(n) > max:
            max = int(n)

    return max


def min_of_n(nums):
    min = max_of_n(nums)
    for n in nums:
        if int(n) < min:
            min = int(n)

    return min


n_list = (input('정수를 여러 개 입력하시오 : ').split())
print('평균값은 {:.1f}'.format(mean_of_n(n_list)))
print('최댓값은', max_of_n(n_list))
print('최솟값은', min_of_n(n_list))


#문제 3
a = [2, 3, 4, 5, 6]
rev_a = []
for x in range(len(a)):
    rev_a.insert(0, a.pop(0))

print('rev_a =', rev_a)


#문제 4
a = int(input('범위의 시작 정수 : '))
b = int(input('범위의 마지막 정수 : '))
if a > b:
    a, b = b, a

result = 1
for n in range(b, a - 1, -1):
    if not (result % n == 0):
        result *= n

print(a, '에서 ', b, '까지의 정수들의 최소공배수는 : ', result, sep='')


#문제 5
#문제 6