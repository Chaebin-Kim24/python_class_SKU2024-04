# 학번 2021304065
# 이름 이태희

#4.1

def my_greet():
    print("환영합니다.")
   
my_greet()
my_greet()

#4.2

def square(n):
    return n**2

print('3의 제곱은 : ',square(3))
print('4의 제곱은 : ',square(4))

#4.24

s1 = input('여러 단어로 이루어진 글을 입력하세요: ')
s1 = s1.replace(',',' ')
s1 = s1.replace('.',' ')
s1 = s1.replace(':',' ')
s1 = s1.replace(';',' ')
s1 = s1.split()
s1.sort()
print('정렬결과 : ',s1)

#4.25
from pickletools import string1
from re import S


s1 = 'Kang Young Min'
s2 = 'Kang Young-Min'
s3 = 'Park Dong Min'
s4 = 'Park Dong-Yun'
ss = [s1,s2,s3,s4]
for i in range(4):
    sss = ss[i].replace(' ', '')
    sss = sss.replace('-', '')
    sss = sss.upper()
    print('{}(은)는 {}(으)로 수정됨'.format(ss[i], sss))
    ss[i] = sss
for i in ss:
    N = 0
    for j in i:
        if j == 'N':
            N += 1
    print('{} : {} 개의 N이 나타남'.format(i, N))

#4.26

str1 = 'Park(Java city), kim(C city), Kang(Bython city), Lee(Bython city), Hong(Ruby city), Cho(Bython city), Koo(C city), Ryu(C++ city)'
print('주어진 문자열 : ')
print(str1)
print('수정된 문자열 : ')
print(str1.replace('Bython', 'Python'))
print('Bython 문자열은 모두 {}번 수정했습니다.'.format(str1.count('Bython')))

#4.27

def unit_fraction(frac):
    a  = int(1 / frac)
    a1 = 1/a
    a2 = 1/a+1
    if abs(a1 - frac) > abs(a2 - frac):
        return a
    else:
        return a+1
    
num=float(input('1보다 작고 0보다 큰 소수를 입력하세요: '))

a = unit_fraction(num)

print('가장 가까운 단위분수는 1/{}이며, 이 값은 {}입니다.'.format(a,1/a))






#5.17

#(1)
animals = ['dog','cat','tiger','lion']
print('animals = ',animals)

#(2)
animals.append(animals.pop(0))
print('animals = ',animals)

#(3)
animals = ['dog','cat','tiger','lion']
for i in animals:
    print('I love {}.'.format(i))

#5.18

#(1)
from calendar import c


s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']
s_list2=[]
min_ = 999

for i in s_list:
    if len(i) < min_:
        min_ = len(i)
    s_list2.append(len(i))
   
s_list2.sort()
print('가장 길이가 짧은 문자열: ',s_list[s_list2.index(min_)])
   
#(2)
s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']
s_list2=[]
max_ = 0

for i in s_list:
    if len(i) > max_:
        max_ = len(i)
    s_list2.append(len(i))
   
print('가장 길이가 긴  문자열: ',s_list[s_list2.index(max_)])

#(3)
s_list.sort(key = len)
print('가장 길이가 짧은 문자열 : \'{}\''.format('\', \''.join(s_list[:s_list2.index(max_) + 1])))

#5.19
s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
new_s_list=[]

for i in s_list:
    if not i in new_s_list:
        new_s_list.append(i)

print(new_s_list)

#5.20
def compress_string(src):
    if not src:  
        return src
    
    compressed = src[0]  
    count = 1

    for i in range(1, len(src)):
        if src[i] == src[i - 1]:  
            count += 1
        else:
            compressed += str(count) + src[i] 
            count = 1

    compressed += str(count)  

    return compressed

src = input('src = ')
compressed = compress_string(src)
print('output = ', compressed)

#5.21
def decompress_string(compressed):
    if not compressed:  
        return compressed
    
    decompressed = ''
    i = 0

    while i < len(compressed):
        char = compressed[i]
        count = ""

        while i + 1 < len(compressed) and compressed[i + 1].isdigit():
            count += compressed[i + 1]
            i += 1

        decompressed += char * int(count)

        i += 1

    return decompressed

compressed = input('src = ')
decompressed = decompress_string(compressed)
print('output = ', decompressed)

#5.22
n = int(input('n을 입력하시오 : '))
n2 = 0
for i in range(n):
    N = []
    for _ in range(n):
        n2 += 1
        N.append(n2)
    if i % 2 == 1:
        N = N[::-1]
    for i in N:
        print('{:3d}'.format(i), end = '')
    print()

#5.23
person1 =['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['혁거세', 40, 1, 150.0, 50.0]

def function_of_persons(person_list):
    result = {}
    list1 = []
    for i in range(int(len(person_list) / 5)):
        list1.append(person_list[i * 5:i * 5 + 5])
    result['n_persons'] = len(list1)
    result['average_age'] = 0
    result['n_male'] = 0
    result['f_male'] = 0
    result['person_list'] = list1
    for i in list1:
        result['average_age'] += i[1]
        if i[2] == 1:
            result['n_male'] += 1
        else:
            result['f_male'] += 1
    result['average_age'] /= result['n_persons']
    return result

person_list = person1 + person2 + person3 + person4
print(function_of_persons(person_list))
