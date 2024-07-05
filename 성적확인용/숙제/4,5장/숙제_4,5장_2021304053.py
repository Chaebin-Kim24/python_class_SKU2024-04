# 학번 2021304053
# 이름 윤영주

# 4장 #1, 2, 24, 25, 26, 27

# 1
def my_greet():
    print("환영합니다.")

my_greet()
my_greet()


# 2
def squre(n):
    return n*n

print('3의 제곱은 : ', squre(3))
print('4의 제곱은 : ', squre(4))

# 24
s = input('여러 단어로 이루어진 글을 입력하세요 : ')

s = s.replace(',', ' ')
s = s.replace(':', ' ')
s = s.replace('.', ' ')
s = s.split()
s.sort()
print('정렬결과 :', s)
#임의의 문장을 입력:출력, 이것은 테스트 문장. 가:가나:나:나나:다람쥐 : 마린보이.

# 25
s1 = 'Kang Young Min'
s2 = ' Kang Young-Min'
s3 = 'Park Dong Min'
s4 = ' Park Dong-Yun'

# 공백과 하이픈 제거, 대문자로 변환
s1_modified = s1.replace(' ', '').replace('-', '').upper() 
s2_modified = s2.strip().replace(' ', '').replace('-', '').upper()
s3_modified = s3.replace(' ', '').replace('-', '').upper()
s4_modified = s4.strip().replace(' ', '').replace('-', '').upper()

# 결과 출력
print(f"{s1}(은)는 {s1_modified}(으)로 수정됨")
print(f"{s2.strip()}(은)는 {s2_modified}(으)로 수정됨")
print(f"{s3}(은)는 {s3_modified}(으)로 수정됨")
print(f"{s4.strip()}(은)는 {s4_modified}(으)로 수정됨")

# 각 문자열에서 문자 'N'이 몇 번 나타나는지 표시
print(f"{s1_modified} : {s1_modified.count('N')} 개의 N이 나타남")
print(f"{s2_modified} : {s2_modified.count('N')} 개의 N이 나타남")
print(f"{s3_modified} : {s3_modified.count('N')} 개의 N이 나타남")
print(f"{s4_modified} : {s4_modified.count('N')} 개의 N이 나타남")


# 26
s = 'Park(Java city), Kim(C city), Kang(Bython city), Lee(Bython city), Hong(Ruby city), Cho(Bython city), Koo(C city), Ryu(C++ city)'

# 'Bython'을 'Python'으로 변경하고 변경 횟수 계산
s_modified, count = s.replace('Bython', 'Python'), s.count('Bython')

# 결과 출력
print("주어진 문자열 :")
print(s)
print("수정된 문자열 :")
print(s_modified)
print(f"'Bython' 문자열은 모두 {count}번 수정했습니다.")


# 27
def unit_fraction(frac):
    denom = int(1/frac)
    
    d1 = frac -1/(denom+1)
    d2 = 1/denom - frac
    if d1 < d2:
        return denom+1
    else:
        return denom

f_val   = float(input('1보다 작고 0보다 큰 소수를 입력하세요 : '))

if f_val <= 0.0 or f_val > 1.0:
    print('입력오류')
else:
    denom = unit_fraction(f_val)
    print('가장 가까운 단위 분수의 분수는 1/{0}이며, 이 값은 {1:.50f}입니다. '.format(denom, 1/denom))
    

# 5장 연습문제 #17, 18, 19, 20, 21, 22, 23

# 17
#1
animals = ['dog', 'cat', 'tiger', 'lion']

print('animals =', animals)
#2
animals = ['dog', 'cat', 'tiger', 'lion']

animals = animals[1:] + [animals[0]]
print('animals =', animals)
#3
animals = ['dog', 'cat', 'tiger', 'lion']

print('animals =', animals)

a = 0
for n in animals:
    animals[a] = print('I love {}.'.format(n))
    

# 18
#1
s_list = ['abc', 'bed', 'bcdefg', 'abba', 'cddc', 'opq']

shortest_string = min(s_list, key=len)
print('가장 길이가 짧은 문자열 :', shortest_string)

#2
s_list = ['abc', 'bed', 'bcdefg', 'abba', 'cddc', 'opq']

longest_string = max(s_list, key=len)
print('가장 길이가 긴 문자열 :', longest_string)
#3
s_list = ['abc', 'bed', 'bcdefg', 'abba', 'cddc', 'opq']

shortest_len = min(map(len, s_list))

shortest_string = [s for s in s_list if len(s) == shortest_len]

print('가장 길이가 짧은 문자열 :', shortest_string)


# 19
s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
new_s_list = []

for element in s_list:
    if element not in new_s_list:
        new_s_list.append(element)

print("s_list =", s_list)
print("new_s_list =", new_s_list)


# 20
def compress_string(src):
    compressed_string = ""
    count = 1
    for i in range(len(src)):
        if i == len(src) - 1 or src[i] != src[i+1]: # 마지막 문자이거나 다음 문자와 다른 경우
            compressed_string += src[i] + str(count) # 문자와 문자의 개수를 연결하여 추가
            count = 1 
        else:
            count += 1
    return compressed_string

src = 'aaaabbb'
output = compress_string(src)
print("src = '", src, "'")
print("output = '", output, "'")

src = 'aaaabccccaaaaacccfg'
output = compress_string(src)
print("src = '", src, "'")
print("output = '", output, "'")

src = ''
output = compress_string(src)
print("src = '", src, "'")
print("output = '", output, "'")

src = 'a'
output = compress_string(src)
print("src = '", src, "'")
print("output = '", output, "'")


# 21
# 도저히 모르겠습니다
"""
def decompress_string(src): # 문자열 src를 입력받아 압축을 해제한 문자열을 반환하는 함수
    
    decompressed_string = "" # 압축을 해제한 문자열을 저장할 변수
    count = "" # 압축된 문자의 반복 횟수를 저장할 변수
    
    for i in range(len(src)): # 문자열 src를 처음부터 끝까지 반복
        if src[i].issentence(): 
            count += src[i] # count에 src[i]를 추가
        else:
            
            decompressed_string += src[i] * int(count) # src[i]를 count만큼 반복하여 decompressed_string에 추가
            count = "" # count를 초기화

src = 'a2b3c6a2c3f1g1' # 압축된 문자열
output = decompress_string(src) # decompress_string 함수를 호출하여 압축을 해제한 문자열을 반환받음
print("src ='", src, "'") # src 출력
print("output ='", output, "'") # output = 'aabbbccccccaaccfg' 출력
"""

# 22
n = int(input("n을 입력하시오: "))

matrix = [[0] * n for _ in range(n)]  # n x n 행렬 생성

num = 1
for i in range(n): # n x n 행렬에 숫자 채우기
    if i % 2 == 0: # 짝수 행은 1부터 n까지
        matrix[i] = list(range(num, num + n)) # 짝수 행은 1부터 n까지
    else:
        matrix[i] = list(range(num + n - 1, num - 1, -1)) # 홀수 행은 n부터 1까지
    num += n # 다음 행의 시작 숫자

for row in matrix:
    print(' '.join(map(str, row))) # 각 행을 출력


# 23
#1
def how_many_persons(person_list):
    return len(person_list)//5

person1 = ['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['혁거세', 40, 1, 150.0, 50.0]

person_list = person1 + person3 + person4
n_persons = how_many_persons(person_list)
print(str(n_persons) + '명의 정보가 담겨 있습니다.')

#2
def average_age(person_list):
    return len(person_list)//5

person1 = ['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['혁거세', 40, 1, 150.0, 50.0]

person_list = person1 + person2 + person3 + person4
average_age = sum(person_list[1::5]) / average_age(person_list) 
print('평균 나이는 ' + str(average_age) + '세입니다.')

#3
def count_males_females(person_list):
    n_male = 0
    n_female = 0
    for i in range(2, len(person_list), 5):
        if person_list[i] == 1:
            n_male += 1
            
        elif person_list[i] == 0:
            n_female += 1
    return n_male, n_female

person1 = ['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['혁거세', 40, 1, 150.0, 50.0]


person_list = person1 + person2 + person3 + person4
n_male, n_female = count_males_females(person_list)
print('리스트에는 남자가', n_male, '명, 여자가', n_female, '명입니다.')

#4
def display_persons(person_list):
    for i in range(0, len(person_list), 5):
        person = person_list[i:i+5]
        print(person)

person1 = ['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['혁거세', 40, 1, 150.0, 50.0]

person_list = person1 + person2 + person3 + person4
display_persons(person_list)
