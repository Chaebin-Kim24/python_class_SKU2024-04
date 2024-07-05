# 학번 2020305036
# 이름 원종인

#4.24
print(4.24)
s = input('문장 입력 : ')
specialC = '~!@#$%^&*()_+-=`[]{};:\'\",./?<>\|'
for i in range(len(specialC)):
    s = s.replace(specialC[i], ' ')
s = s.split()
print(s)

#4.25
print(4.25)
s1 = 'Kang Young Min'
s2 = ' Kang Young-Min'
s3 = 'Park Dong Min'
s4 = ' Park Dong-Yun'
def editStr(s):
    print('문자열', s, '이(가)', end = '')
    s = s.replace(' ', '')
    s = s.replace('-', '')
    s = s.upper()
    print(s,'로 수정됨')
    return s

s1 = editStr(s1)
s2 = editStr(s2)
s3 = editStr(s3)
s4 = editStr(s4)
print(s1,': N의 개수가', s1.count('N'),'개 있습니다.')
print(s2,': N의 개수가', s2.count('N'),'개 있습니다.')
print(s3,': N의 개수가', s3.count('N'),'개 있습니다.')
print(s4,': N의 개수가', s4.count('N'),'개 있습니다.')

#4.26
s = 'Park(Java city), Kim(C city), Kang(Bython city), Lee(Bython city), Hong(Ruby city), Cho(Bython city), Koo(C city), Ryu(C++ city)'
n = s.count('Bython')
s = s.replace('Bython', 'Python')
   
print('수정된 문자열 : \n',s,'\n문자열이 총', n ,'번 수정되었습니다.')

#4.27
def getdanwebunsu(n):
    i = 1
    jumpRange = 1
    lastJumpRange = 0
    term = 1
    minTerm = 2
    while 1:
        while n <= 1/(i + jumpRange):
            lastJumpRange = jumpRange#이전 점프 범위 저장
            jumpRange *= 2#점프 구간이 2배씩 증가
        if jumpRange == 1:#1/(i + 1)이 n보다 작고 1/i가 n보다 크거나 같을때
            if 1/i - n < n - 1/(i+1):#1/i가 1/(i + 1)보다 n에 가까울때
                return i
            else :
                return i + 1
        #1/(i + jumpRange)는 0보다 작고 1/(i + lastJumpRange)는 n보다 크다
        #점프 범위 절반으로 감소
        i = i + int(lastJumpRange)
        jumpRange = jumpRange / 2
        lastJumpRange = 0

        

n = float(input('1보다 작고 0보다 큰 소수 입력 : '))
n = getdanwebunsu(n)
print('가장 가까운 단위분수는 1/{}이며, 이 값은 {}입니다.'.format(n, 1/n))



#5.17
print(5.17, '(1)')
animals = ['dog', 'cat', 'tiger', 'lion']
print('animals =', animals)

print('(2)')
animals.remove('dog')
animals.append('dog')
print('animals =', animals)

print('(3)')

print('animals =', animals)
for animal in animals:
    print('i love {}.\n'.format(animal))

#5.18
print(5.18,'(1)')
s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']
minLen = len(s_list[0])
mins = s_list[0]
for s in s_list:
    if len(s) < minLen:
        minLen = len(s)
        mins = s
print('가장 길이가 짧은 문자열 :', mins)

print('(2)')
longLen = len(s_list[0])
longS = s_list[0]
for s in s_list:
    if len(s) > minLen:
        minLen = len(s)
        mins = s
print('가장 길이가 긴 문자열 :', mins)

print('(3)')
s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']
minLen = len(s_list[0])
mins = [s_list[0]]
for s in s_list:
    if len(s) < minLen:
        minLen = len(s)
        mins = [s]
    elif len(s) == minLen:
        mins.append(s)
            
print('가장 길이가 짧은 문자열 : ', end = '')
for min in mins:
    print('\'{}\' '.format(min), end = ' ')
print()

#5.19
print('\n', 5.19)
s_list = ['abc','bcd','abc','abba','cddc','opq','opq']
new_s_list = []

for s in s_list:
    if s not in new_s_list:
        new_s_list.append(s)

print('s_list =', s_list)
print('new_s_list =', new_s_list)

#5.20
print('\n5.20')
def zip(s):
    if 0 == len(s):
        return s
    zip_s = s[0]
    cnt = 0
    for i in range(len(s)):
        if zip_s[-1] == s[i]:
            cnt += 1
        else:
            zip_s += str(cnt)
            zip_s += s[i]
            cnt = 1
    zip_s += str(cnt)
    return zip_s

src = 'aaaabbb'
print('src =', src)
print('output =',zip(src))

src = 'aaaabccccaaaaacccfg'
print('src =', src)
print('output =',zip(src))

src = ''
print('src =', src)
print('output =',zip(src))

src = 'a'
print('src =', src)
print('output =',zip(src))


#5.21
print('\n5.21')
def unzip(s):
    unzip_s = ''
    
    if len(s) == 0:
        return s

    for i in range(0,len(s), 2):
        for j in range(int(s[i + 1])):
            unzip_s += s[i]
    return unzip_s

src = 'a2b3c6a2c3f1g1'
print('src =', src)
print('output =', unzip(src))


#5.22
print('\n5.22')
n = int(input('n을 입력하시오 : '))
n_list = list(range(n * n))
for i in range(n):
    if 1 & i:
        for j in n_list[(i + 1) * n  - 1 : i * n - 1 : -1]:
            print('{:4d}'.format(j), end = ' ')
    else:
        for j in n_list[i * n : (i + 1) * n]:
            print('{:4d}'.format(j), end = ' ')
    print()


#5.23
def how_many_persons(person_list):
    return int(len(person_list) / 5)

def compute_average_age(person_list):
    return sum(person_list[1::5]) / how_many_persons(person_list)

def count_males_females(person_list):
    n_male = 0
    n_female = 0
    for sex in person_list[2::5]:
        if sex == 1:
            n_male += 1
        else:
            n_female += 1
    return n_male, n_female

def display_persons(person_list):
    for i in range(how_many_persons(person_list)):
        print(person_list[i * 5 : (i + 1) * 5])

person1 = ['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['혁거세', 40, 1, 150.0, 50.0]

person_list = person1 + person2 + person3 + person4

print('(1)')
print('{}명의 정보가 담겨있습니다.'.format(how_many_persons(person_list)))
print('(2)')
print('평균 나이는 {}세 입니다.'.format(compute_average_age(person_list)))
print('(3)')
n_male, n_female = count_males_females(person_list)
print('리스트에는 남자가 {}명, 여자가 {}명 입니다.'.format(n_male, n_female))
print('(4)')
display_persons(person_list)

