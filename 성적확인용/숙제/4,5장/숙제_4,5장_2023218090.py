# 학번 2023218090
# 이름 임상환

#4-1

def my_greet():
    print('환영합니다.')
my_greet()
my_greet()


#4-2

def square(n):
    return n*n
print('3의 제곱은 : ',square(3))
print('4의 제곱은 : ',square(4))


#4-24

dots = '.,;:!?-_'
s=input('여러 단어로 이루어진 글을 입력하세요: ')
for dot in dots:
    s=s.replace(dot,'')
terms = sorted(s.split())
print('정렬 결과 : \n', terms)


#4-25

s1 = 'Kang young Min'
s2 = ' Kang Young-Min'
s3 = 'Park Dong Min'
s4 = ' Park Dong-yun'
ss = [s1, s2, s3, s4]

cleaned_strings = []
for s in ss:
    cleaned_string = s.replace('-', '').replace(' ', '').upper()
    cleaned_strings.append(cleaned_string)
for original, cleaned in zip(ss, cleaned_strings):
    print('{}은(는) {}으로 변경'.format(original, cleaned))
for original, cleaned in zip(ss, cleaned_strings):
    print('{} : {} 개의 N이 나타남'.format(cleaned,cleaned.count('N')))

#4-26

a_st='Park(Java city), Kim(C city), Kang(Bython city),Lee(Bython city), Hong(Ruby city), Cho(Bython city), Koo(C city), Ryu(C++ city)'
print('주어진 문자열 : \n', a_st)
print('수정된 문자열 : \n', a_st.replace('Bython','Python'))
print('Bython 문자열은 모두', a_st.count('Bython'), '번 수정했습니다.' )


#4-27

def unit_fraction(frac):
    denom=int(1/frac)
    d1=frac-1/(denom+1)
    d2=1/denom-frac
    if d1<d2:
        return denom+1
    else:
        return denom
f_val=float(input('1보다 작고 0보다 큰 소수를 입력하세요: '))
if f_val<=0.0 or f_val>1.0:
    print('입력 오류입니다')
else:
    denom=unit_fraction(f_val)
    print('가장 가까운 단위분수는 1/{0}이며, 이 값은 {1:.50f}입니다.'.format(denom, 1/denom))


#5-17

animals=['dog','cat','tiger','lion']
print(animals)

def shift_left(lst):
    if len(lst) <= 1:
        return lst
    
    temp = lst[0]
    
    for i in range(len(lst) - 1):
        lst[i] = lst[i + 1]    
    lst[-1] = temp    
    return lst
shift_left(animals)
print(animals)

for i in animals:
    print('I love ', i)

#5-18

s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']
short = s_list[0]

for string in s_list:
    if len(string) < len(short):
        short = string
print('가장 길이가 짧은 문자열:', short)

long=s_list[0]
for string in s_list:
    if len(string) > len(long):
        long = string
print('가장 길이가 긴 문자열:', long)

s_list.sort(key=len)
shortest_length = len(min(s_list, key=len)) 

shortest_strings = [string for string in s_list if len(string) == shortest_length]

print('가장 길이가 짧은 문자열:', shortest_strings)
#5-19
s_list = ['abc', 'bcd', 'abc', 'bcdefg', 'abba', 'cddc', 'opq', 'opq']
print('s_list = ',s_list)
new_s_list = []
for value in s_list:
    if value not in new_s_list:
        new_s_list.append(value)
print('new_s_list = ',new_s_list)

#5-20

def compress_string(s):
    compressed = '' 
    count = 1
    for i in range(len(s)):
        if i < len(s) - 1 and s[i] == s[i + 1]:
            count += 1
        else:
            compressed += s[i] + str(count)
            count = 1
    return compressed
src='aaaabbb'
print('src= ',src)
print('output= ', compress_string(src))
src='aaaabccccaaaaacccfg'
print('src= ',src)
print('output= ', compress_string(src))

#5-21

def decompress_string(compressed):
    decompressed = ''
    i = 0
    while i < len(compressed):
        char = compressed[i]
        count_str = ''
        while i + 1 < len(compressed) and compressed[i + 1].isdigit():
            count_str += compressed[i + 1]
            i += 1
        count = int(count_str) if count_str else 1
        decompressed += char * count
        i += 1
    return decompressed

compressed_string = 'a2b3c6a2c3f1g1'
original_string = decompress_string(compressed_string)
print('src= ', compressed_string)
print('output= ', original_string)



#5-22

n = int(input("n을 입력하시오: "))
num = 0
arr = [[col+row*n for col in range(1, (n+1))] for row in range(n)]


for i in range(0, n):
    if i % 2 == 1:
        print(arr[i][::-1], end=" ")
    else:
        print(arr[i][::1], end=" ")
    print()

#5-23
def how_many_persons(person_list):
    return len(person_list)/5
person1=['온달',20,1,180.0,100.0]
person2=['이사부',25,1,170.0,70.0]
person3=['평강',22,0,169.0,60.0]
person4=['혁거세',40,1,150.0,50.0]

person_list=person1+person3+person4

n_persons=how_many_persons(person_list)
print(str(n_persons)+'명의 정보가 담겨 있습니다')

def compute_average_age(person_list):
    s = 0
    for person in person_list:
        s += person[1]
    return s / len(person_list)

person1 = ['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['혁거세', 40, 1, 150.0, 50.0]

person_list = [person1, person2, person3, person4]

average_age = compute_average_age(person_list)

print('평균 나이는 {:.2f}세 입니다.'.format(average_age))

def count_gender(person_list):
    male_count = sum(person[2] == 1 for person in person_list)
    female_count = sum(person[2] == 0 for person in person_list)
    return male_count, female_count
male_count, female_count = count_gender(person_list)
print('남자는 {}명, 여자는 {}명입니다.'.format(male_count, female_count))
 
def display_persons(person_list):
    for person in person_list:
        print(person)
display_persons(person_list)

