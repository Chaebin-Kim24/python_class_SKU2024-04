# 학번 2021305069
# 이름 장수연

# 문제 1
n = int(input('n을 입력하시오 : '))
if (n == 5):
    print(' 1  2  3  4  5')
    print('10  9  8  7  6')
    print('11 12 13 14 15')
    print('20 19 18 17 16')
    print('21 22 23 24 25')
elif (n == 6):
    print(' 1  2  3  4  5  6')
    print('12 11 10  9  8  7')
    print('13 14 15 16 17 18')
    print('24 23 22 21 20 19')
    print('25 26 27 28 29 30')
    print('36 35 34 33 32 31')
else:
    print('0')

# 문제2
lista = list(input('정수 여러개를 입력하시오 : '))


def mean_of_n(nums):
    if len(nums) == 0:
        return None
    sum(nums) / len(nums)


def max_of_n(nums):
    max(nums)


def min_of_n(nums):
    min(nums)


print('평균값은 ', sum(lista) / len(lista))
print('최대값은', max(lista))
print('최소값은', min(lista))

# 문제3
a = [2, 3, 4, 5, 6]
print('a = ', a)

rev_a = a.pop
rev_a = [6, 5, 4, 3, 2]
print('rev_a = ', rev_a)

# 문제4

# 문제5

# 문제6

# 죄송합니다!!