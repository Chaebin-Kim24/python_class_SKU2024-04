# 학번 2023218031
# 이름 김태연

#4.1
def my_greet():
    print('환영합니다.')

my_greet()

#4.2
def square(n):
    return n*n
print('3의 제곱은 : ',square(3))
print('4의 제곱은 : ',square(4))

#4.24
sentence = input('여러 단어로 이루어진 글을 입력하세요: ')
sentence = sentence.replace(':', ' ')
sentence = sentence.replace(',', ' ')
sentence = sentence.replace('.', ' ')
sentence = sentence.split()
sentence.sort()
print('정렬 결과 : ')
print(sentence)

#4.25
s1 = 'Kang Young Min'
s2 = ' Kang Young-Min'
s3 = 'Park Dong Min'
s4 = ' Park Dong-Yun'
L = [s1, s2, s3, s4]
for i in range(4):
    result = L[i].replace(' ', '')
    result = result.replace('-', '')
    result = result.upper()
    print('{}(은)는 {}(으)로 수정됨'.format(L[i], result))
    L[i] = result
    for i in L:
        print('{} : {} 개의 N이 나타남'.format(i, i.count('N')))

#4.26
input_str = 'Park(Java city), kim(C city), Kang(Bython city), Lee(Bython city), Hong(Ruby city), Cho(Bython city), Koo(C city), Ryu(C++ city)'
print('주어진 문자열 : ')
print(input_str)
print('수정된 문자열 : ')
print(input_str.replace('Bython', 'Python'))
print('Bython 문자열은 모두 {}번 수정했습니다.'.format(input_str.count('Bython')))

#4.27
def unit_fraction(frac):
    n = int(1/frac)
    r1 = 1/n
    r2 = 1/(n+1)
    if abs(r1 - frac) < abs(r2 - frac):
        return n
    else:
        return n + 1
num = float(input('1보다 작고 0보다 큰 소수를 입력하세요: '))
n = unit_fraction(num)
print('가장 가까운 단위분수는 1/{}이며, 이 값은 {}입니다.'.format(n, 1/n))

#5.17
animals = ['dog', 'cat', 'tiger', 'lion']
print('animals : {}'.format(animals))
animals.append(animals.pop())
print('animals : {}'.format(animals))
animals = ['dog', 'cat', 'tiger', 'lion']
print('animals : {}'.format(animals))
for i in animals:
    print('I love {}.'.format(i))


#5.18
s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']
index_list = []
s_min = 999999
s_max = 0
for i in s_list:
    if len(i) < s_min:
        s_min = len(i)
    if len(i) > s_max:
        s_max = len(i)
    index_list.append(len(i))

print('가장 길이가 짧은 문자열 :', s_list[index_list.index(s_min)])
print('가장 길이가 긴 문자열 :', s_list[index_list.index(s_max)])
s_list.sort(key = len)
print('가장 길이가 짧은 문자열 : \'{}\''.format('\', \''.join(s_list[:index_list.index(s_max) + 1])))

#5.19
s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
new_s_list = list(set(s_list))
s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
new_s_list = []
for i in s_list:
    if not i in new_s_list:
        new_s_list.append(i)

#5.20
src = input()
while src != '':
    length = len(src)
    print(src[0], end = '')
    src = src.lstrip(src[0])
    print(length - len(src), end = '')
    
#5.21
num_list = list(map(str, range(10)))
src = input()
multiple_num = ''
for i in src[1:]:
    if not i in num_list:
        last_result += last_result[-1] * (int(multiple_num) - 1) + i
        multiple_num = ''
    else:
        multiple_num += i

#5.22
n = int(input('n을 입력하시오 : '))
stack = 0
for i in range(n):
    L = []
    for _ in range(n):
        stack += 1
        L.append(stack)
    if i % 2 == 1:
        L = L[::-1]
    for i in L:
        print('{:3d}'.format(i), end = '')
    print()

#5.23
person1 = ['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['혁거세', 40, 1, 150.0, 50.0]

def function_of_persons(person_list):
    result = {}
    divide_list = []
    for i in range(int(len(person_list) / 5)):
        divide_list.append(person_list[i * 5:i * 5 + 5])
        result['n_persons'] = len(divide_list)
        result['average_age'] = 0
        result['n_male'] = 0
        result['f_male'] = 0
        result['person_list'] = divide_list
        for i in divide_list:
            result['average_age'] += i[1]
            if i[2] == 1:
                result['n_male'] += 1
            else:
                result['f_male'] += 1
        result['average_age'] /= result['n_persons']
        return result

person_list = person1 + person2 + person3 + person4
print(function_of_persons(person_list))
