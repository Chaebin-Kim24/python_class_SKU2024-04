# 학번 2021305069
# 이름 장수연

#4.1

def my_greet():
    print('환영합니다.')

my_greet()
my_greet()

#4.2

def sqare(n):
    return n*n

print('3의 제곱은 : ', sqare(3))
print('4의 제곱은 : ', sqare(4))

#4.24

s = input('여러 단어로 이루어진 글을 입력하세요: ')
s = s.replace(':',' ')
s = s.replace('.',' ')
s = s.replace(',',' ')
s = s.split()
s.sort()
print('정렬 결과 :')
print(s)

#4.25

s1 = 'Kang Young Min'
s2 = ' Kang Young-Min'
s3 = 'Park Dong Min'
s4 = ' Park Dong-Yun'

A = [s1, s2, s3, s4]

for i in range(4):
    result = A[i].replace(' ','')
    result = result.replace('-','')
    result = result.upper()
    print(A[i],'(은)는',result, '(으)로 수정됨')
    A[i] = result

for i in A:
    N=0
    for j in i:
        if j == 'N':
            N += 1
    print(i,':',N,'개의  N이 나타남')

#4.26

c = 'Park(Java city), Kim(C city), Kang(Bython city), Lee(Bython city), Hong(Ruby city), Cho(Bython city), Koo(C city), Ryu(C++ city)'
print('주어진 문자열 :')
print(c)
print('수정된 문자열 :')
print(c.replace('Bython','Python'))
print('Bython 문자열은 모두 {}번 수정했습니다.'.format(c.count('Bython')))

#4.27

def unit_fraction(frac):
    n = int(1/frac)
    a1 = 1/n
    a2 = 1/(n+1)
    if (a1 - frac) < (a2 - frac):
        return n
    else:
        return n+1
    
num = float(input('1보다 작고 0보다 큰 소수를 입력하세요: '))
n = unit_fraction(num)
print('가장 가까운 단위 분수는 1/{}이며, 이 값은 {}입니다.'.format(n,1/n)) #0.0732


#5.17 (1)

animals = ['dog', 'cat', 'tiger', 'lion']
print('animals = ', animals)

#5.17 (2)

animals.append(animals.pop(0))
print('animals = ',animals)

#5.17 (3)

animals = ['dog', 'cat', 'tiger', 'lion']
print('animals = ', animals)
for i in animals:
    print('I love {}'.format(i))

#5.18

s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']
i_list = []
min = 999
max = 0
for i in s_list:
    if len(i) < min:
        min = len(i)
    if len(i) > max:
        max = len(i)
    i_list.append(len(i))

#5.18 (1)
print('가장 길이가 짧은 문자열 : ', s_list[i_list.index(min)])

#5.18 (2)
print('가장 길이가 긴 문자열 : ', s_list[i_list.index(max)])

#5.18 (3)
s_list.sort(key = len)
print('가장 길이가 짧은 문자열 : \'{}\''.format('\', \''.join(s_list[:i_list.index(max) + 1])))


#5.19

s_list = ['abc','bcd','abc','abba','cddc','opq','opq']
print(s_list)
new_s_list = []
for i in s_list:
    if not i in new_s_list:
        new_s_list.append(i)
print(new_s_list)


#5.20

src = input('src = ')
print('output = ', end = '')
while src != '':
    print(src[0] + '{}'.format(len(src) - len(src.lstrip(src[0])), end = ''))
    src = src.lstrip(src[0])

#5.21

src = input('src = ')
print('output = ', end = '')
for i in range(int(len(src)/2)):
    print(src[i*2]*int(src[i*2+1]), end = '')

#5.22

n = int(input(' \nn을 입력하시오 : '))
stack = 0
for i in range(n):
    L = []
    for _ in range(n):
        stack += 1
        L.append(stack)
    if i % 2 == 1:
        L = L[::-1]
    for i in L:
        print('{}'.format(i),'\t', end = '')
    print()

#5.23

person1 = ['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['혁거세', 40, 1, 150.0, 50.0]

person_list = person1 + person2 + person3 + person4

#5.23 (1)
def how_many_persons(person_list):
    num = len(person_list) // 5
    return num
n_persons = how_many_persons(person_list)
print(str(n_persons) + '명의 정보가 담겨 있습니다.')

#5.23 (2)
def compute_average_age(person_list):
    age_list = list()
    for i in range(1,len(person_list),5):
        age_list.append(person_list[i])
    average = sum(age_list) / len(age_list)
    return average
average_age = compute_average_age(person_list)
print('평균 나이는 ' + str(average_age) + '세입니다.')

#5.23 (3)
def count_males_females(person_list):
    male = 0
    female = 0
    for i in range(2,len(person_list), 5):
        if person_list[i] == 1:
            male += 1
        elif person_list[i] == 0:
            female += 1
    return male, female
n_male, n_female = count_males_females(person_list)
print('리스트에는 남자가', n_male,'명, 여자가', n_female, '명입니다.')

#5.23 (4)
def display_persons(person_list):
    num = len(person_list) // 5
    for i in range(0,len(person_list),5):
        person_all_list = person_list[i:i+5]
        print(person_all_list) 
display_persons(person_list)
