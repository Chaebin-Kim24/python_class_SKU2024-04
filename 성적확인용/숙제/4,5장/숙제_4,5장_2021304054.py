# 학번 2021304054
# 이름 윤종서

# _4_1
def my_greet():
    print('환영합니다')
    
my_greet()
my_greet()
# _4_2
def square(n):
    return n**2

print('3의 제곱은 : ',square(3))
print('4의 제곱은 : ',square(4))


# _4_24
a = input('여러 단어로 이루어진 글을 입력하세요: ')

a = a.replace(':' , ' ')
a = a.replace(',' , ' ')
a = a.replace('.' , ' ')

a = a.split()

a.sort()

print('정렬 결과 : ')
print(a)

# _4_25
a = 'Kang Young Min'
b = ' Kang Young-Min'
c = 'Park Dong Min'
d = ' Park Dong-Yun'
A = [a, b, c, d]

for i in range(4):
    result = A[i].replace(' ', '')
    result = result.replace('-', '')
    result = result.upper()
    print('(은)는 {}(으)로 수정됨'.format(A[i], result))
    A[i] = result

for i in A:
    N = 0
    for j in i:
        if j == 'N':
            N += 1
    print('{} : {} 개의 N이 나타남'.format(i, N))
# _4_26
input_a = 'Park(Java city), kim(C city), Kang(Bython city), Lee(Bython city), Hong(Ruby city), Cho(Bython city), Koo(C city), Ryu(C++ city)'

print('주어진 문자열 : ')
print(input_a)
print()

print('수정된 문자열 : ')
print(input_a.replace('Bython', 'Python'))

print('Bython 문자열은 모두 {}번 수정했습니다.'.format(input_a.count('Bython')))

# _4_27
def number(a):
    n = int(1/a)
    r1 = 1/n
    r2 = 1/(n+1)
    
    if abs(r1 - a) < abs(r2 - a):
        return n
    else:
        return n + 1
    
num = float(input('1보다 작고 0보다 큰 소수를 입력하세요: '))
n = number(num)
print('가장 가까운 단위분수는 1/{}이며, 이 값은 {}입니다.'.format(n, 1/n))
print()

def number(b):
    n = int(1/b)
    r1 = 1/n   
    r2 = 1/(n+1)
    
    if abs(r1 - b) < abs(r2 - b):
        return n
    else:
        return n + 1

num = float(input('1보다 작고 0보다 큰 소수를 입력하세요: '))
n = number(num)
print('가장 가까운 단위분수는 1/{}이며, 이 값은 {}입니다.'.format(n, 1/n))
# _5_17
animals = ['dog', 'cat', 'tiger', 'lion']
print('animals : {}'.format(animals))
print()

animals.append(animals.pop(0))
print('animals : {}'.format(animals))
print()

animals = ['dog', 'cat', 'tiger', 'lion']
print('animals : {}'.format(animals))
for i in animals:
    print('I love {}.'.format(i))

# _5_18
s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']

s_min = 100
s_max = 0
index_list = []

for i in s_list:
    if len(i) < s_min:
        s_min = len(i)
        
    if len(i) > s_max:
        s_max = len(i)
        

    index_list.append(len(i))

print('1번')    
print('가장 길이가 짧은 문자열 :', s_list[index_list.index(s_min)])

print('2번')
print('가장 길이가 긴 문자열 :', s_list[index_list.index(s_max)])

s_list.sort(key = len)

print('3번')
print('가장 길이가 짧은 문자열 : \'{}\''.format('\', \''.join(s_list[:index_list.index(s_max) + 1])))

# _5_19
s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
new_s_list = list(set(s_list))

print('s_list = ',s_list)
print('new_s_list = ',new_s_list)

# _5_20
src = input('src = ')
print('output = ')
while src != '':
    length = len(src)
    print(src[0],  end = '')
    src = src.lstrip(src[0])
    print(length - len(src), end = '')
print()    

# _5_21
num_list = list(map(str, range(10)))
src = input('src = ')
a = src[0]
b = ''
for i in src[1:]:
    if not i in num_list:
        a += a[-1] * (int(b) - 1) + i
        b = ''
    else:
        b += i
a += a[-1] * (int(b) - 1)
print('output = ',a)

# _5_22
n = int(input('n을 입력하시오 : '))
a = 0
print()

for i in range(n):
    A = []
    print()

    for _ in range(n):
        a += 1
        A.append(a)
    
    if i % 2 == 1:
        A = A[::-1]
    
    for i in A:
        print('{:3d}'.format(i), end = '')
    
    print()
print()
    

# _5_23
person1 =['온달', 20, 1, 180.0, 100.0]
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


print((function_of_persons(person_list)))
