# 학번 2020304049
# 이름 윤치경
#
# 4장, 5장 연습문제 풀이


# 연습문제 4.1
def my_greet():
    print('환영합니다.')

my_greet()
my_greet()


# 연습문제 4.2
def square(n):
    return n ** 2

print('3의 제곱은 : ', square(3), sep='')
print('4의 제곱은 : ', square(4), sep='')


# 연습문제 4.24
s_input = input('여러 단어로 이루어진 글을 입력하세요: ')

s_input = s_input.replace(',',' ')
s_input = s_input.replace('.',' ')
s_input = s_input.replace(':',' ')
s_input = s_input.replace('?',' ')
s_input = s_input.replace('!',' ')

print('정렬 결과 :')
print(sorted(s_input.split()))


# 연습문제 4.25
s1 = 'Kang Young Min'
s2 = ' Kang Young-Min'
s3 = 'Park Dong Min'
s4 = ' Park Dong-Yun'

ms1 = s1.replace(' ','').replace('-','').upper()
ms2 = s2.replace(' ','').replace('-','').upper()
ms3 = s3.replace(' ','').replace('-','').upper()
ms4 = s4.replace(' ','').replace('-','').upper()

print(s1, '(은)는 ', ms1, '(으)로 수정됨', sep='')
print(s2, '(은)는 ', ms2, '(으)로 수정됨', sep='')
print(s3, '(은)는 ', ms3, '(으)로 수정됨', sep='')
print(s4, '(은)는 ', ms4, '(으)로 수정됨', sep='')

print(ms1, ':', ms1.count('N'), '개의 N이 나타남')
print(ms2, ':', ms2.count('N'), '개의 N이 나타남')
print(ms3, ':', ms3.count('N'), '개의 N이 나타남')
print(ms4, ':', ms4.count('N'), '개의 N이 나타남')


# 연습문제 4.26
s_bython = 'Park(Java city), Kim(C city), Kang(Bython city), Lee(Bython city), Hong(Ruby city), Cho(Bython city), Koo(C city), Ryu(C++ city)'

print('주어진 문자열 :')
print(s_bython)
print()
print(s_bython.replace('Bython', 'Python'))
print('Bython 문자열은 모두 ', s_bython.count('Bython'), '번 수정했습니다.', sep='')


# 연습문제 4.27
def unit_fraction(frac):
    n_unit = 1
    n_fraction = 0
    while True:
        sub0 = abs(frac - (1/n_unit))
        sub1 = abs(frac - (1/(n_unit + 1)))
        sub2 = abs(frac - (1/(n_unit + 2)))

        if sub0 < sub1:
            print('가장 가까운 단위분수는 1/', n_unit,'이며, 이 값은 ', 1/n_unit,'입니다.', sep='')
            return

        if sub1 < sub2:
            print('가장 가까운 단위분수는 1/', n_unit + 1,'이며, 이 값은 ', 1/(n_unit + 1),'입니다.', sep='')
            return

        n_unit += 1

frac_input = float(input('1보다 작고 0보다 큰 소수를 입력하세요: '))
unit_fraction(frac_input)


# 연습문제 5.17.1
animals = ['dog', 'cat', 'tiger', 'lion']
print('animals =', animals)


# 연습문제 5.17.2
temp_animal = animals.pop(0)
animals.append(temp_animal)

print('animals =', animals)


# 연습문제 5.17.3
animals = ['dog', 'cat', 'tiger', 'lion']
for animal in animals:
    print('I love ', animal, '.', sep='')


# 연습문제 5.18.1
s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']
shortest_string = s_list[0]

for s in s_list:
    if len(s) < len(shortest_string):
        shortest_string = s

print('가장 길이가 짧은 문자열 :', shortest_string)


# 연습문제 5.18.2
longest_string = s_list[0]

for s in s_list:
    if len(s) > len(longest_string):
        longest_string = s

print('가장 길이가 긴 문자열 :', longest_string)


# 연습문제 5.18.3
shortest_string_list = []
for s in s_list:
    if len(s) < len(shortest_string):
        shortest_string = s
        shortest_string_list = []
        shortest_string_list.append(s)

    elif len(s) == len(shortest_string):
        shortest_string_list.append(s)

shortest_string_list.sort(key=len)
print('가장 길이가 짧은 문자열 :', shortest_string_list)


# 연습문제 5.19
s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
new_s_list = []

for s in s_list:
    if s not in new_s_list:
        new_s_list.append(s)

print('s_list =', s_list)
print('new_s_list =', new_s_list)


# 연습문제 5.20
def compress_string(in_str):
    if in_str == '':
        return ''

    count = 0
    c_buffer = ''
    result = ''

    for c in in_str:
        if c == c_buffer:
            count += 1

        else:
            if count != 0:
                result += str(count)

            c_buffer = c
            count = 1
            result += c

    result += str(count)

    return result

src = 'aaaabbb'
result_str = compress_string(src)
print('src = \'', src, '\'', sep='')
print('output = \'', result_str, '\'', sep='')

src = 'aaaabccccaaaaacccfg'
result_str = compress_string(src)
print('src = \'', src, '\'', sep='')
print('output = \'', result_str, '\'', sep='')

src = ''
result_str = compress_string(src)
print('src = \'', src, '\'', sep='')
print('output = \'', result_str, '\'', sep='')

src = 'a'
result_str = compress_string(src)
print('src = \'', src, '\'', sep='')
print('output = \'', result_str, '\'', sep='')


# 연습문제 5.21
def decompress_string(in_str):
    result = ''

    index = 0
    for c in in_str:
        if c.isdigit():
            for _ in range(0, int(c)):
                result += in_str[index - 1]

        index += 1

    return result

src = 'a2b3c6a2c3f1g1'
result_str = decompress_string(src)
print('src = \'', src, '\'', sep='')
print('output = \'', result_str, '\'', sep='')


# 연습문제 5.22
n_input = int(input('n을 입력하시오 : '))
n_list = list(range(1, n_input ** 2 + 1))

sign = 1
for row in range(n_input):
    for column in n_list[row * n_input: (row + 1) * n_input][::sign]:
        print('{0:3d}'.format(column), end='')

    print()
    sign *= -1


# 연습문제 5.23.1
def how_many_persons(in_person_list):
    return len(in_person_list) // 5

person1 = ['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['혁거새', 40, 1, 150.0, 50.0]

person_list = person1 + person3 + person4
n_persons = how_many_persons(person_list)

print(str(n_persons) + '명의 정보가 담겨 있습니다.')


# 연습문제 5.23.2
def compute_average_age(in_person_list):
    sum_of_age = sum(in_person_list[1::5])
    return sum_of_age / how_many_persons(in_person_list)

person_list = person1 + person2 + person3 + person4
average_age = compute_average_age(person_list)

print('평균 나이는 ' + str(average_age) + '세입니다.')


# 연습문제 5.23.3
def count_males_females(in_person_list):
    list1 = in_person_list[2::5]
    male_count = sum(list1)
    return male_count, len(list1) - male_count

person_list = person1 + person2 + person3 + person4
n_male, n_female = count_males_females(person_list)
print('리스트에는 남자가', n_male, '명, 여자가', n_female, '명입니다.')


# 연습문제 5.23.4
def display_persons(in_person_list):
    slice_count = how_many_persons(in_person_list)
    for n in range(slice_count):
        print(in_person_list[n * 5: (n + 1) * 5])

person_list = person1 + person2 + person3 + person4
display_persons(person_list)
