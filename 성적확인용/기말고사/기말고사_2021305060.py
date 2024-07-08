# 학번 2021305060
# 이름 이종희

# 문제 1
u_num = int(input('n을 입력하시오 : '))
u_list = [x for x in range(1, u_num ** 2 + 1)]
for i in range(u_num):
    if i % 2 == 0:
        print(u_list[u_num * i:u_num * i + u_num:])
    else:
        print(u_list[u_num * i:u_num * i + u_num:][::-1])

# 문제 2

# def mean_of_n(nums):


# def max_of_n(nums):


# def min_of_n(nums):


# 문제 3
a = [2, 3, 4, 5, 6]
rev_a = []
for i in range(len(a)):
    rev_a.append(a.pop(len(a) - 1))
print(a)
print(rev_a)

# 문제 4
a = int(input('범위의 시작 정수 : '))
b = int(input('범위의 마지막 정수 : '))
m_list = []
max_num = 1
for i in range(b - a + 1):
    m_list.append(a + i)
for i in m_list:
    max_num = max_num * i
for i in m_list[::-1]:
    if (max_num / i) % i == 0:
        max_num = max_num / i
print('{}에서 {}까지의 정수들의 최소 공배수는 : {}'.format(a, b, int(max_num)))

# 문제 5
birth = int(input('주민등록번호 첫 6숫자 형식 입력 : '))
year = int(birth / 10000)
month = int((birth - year * 10000) / 100)
day = birth - year * 10000 - month * 100
if year >= 25:
    print('19{}년 {}월 {}일'.format(year, month, day))
elif year == 0:
    print('2000년 {}월 {}일'.format(month, day))
elif year < 10:
    print('200{}년 {}월 {}일'.format(year, month, day))
else:
    print('20{}년 {}월 {}일'.format(year, month, day))

# 문제 6
s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
new_s_list = []
k = 0
for i in s_list:
    for j in new_s_list:
        if i == j:
            k += 1
    if k == 0:
        new_s_list.append(i)
    k = 0

print(new_s_list)