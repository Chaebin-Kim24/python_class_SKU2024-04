# 학번 2021304042
# 이름 신원철

#4.1
def greet():
    print("환영합니다.")

greet()
greet()

#4.2
def square(n):
    return n * n

print("3의 제곱은:", square(3))
print("4의 제곱은:", square(4))

#4.24
input_sentence = input("여러 단어로 이루어진 문장을 입력하세요: ")

words = input_sentence.replace(":", ": ").replace(",", " ").replace(".", " ").lower().split()

sorted_words = sorted(words)

print("정렬 결과", sorted_words)

#4.25
s1 = 'Kang Young Min'
s2 = 'Kang Young-Min'
s3 = 'Park Dong Min'
s4 = 'Park Dong-Yun'

s1_cleaned = s1.replace(" ", "").replace("-", "").upper()
s2_cleaned = s2.replace(" ", "").replace("-", "").upper()
s3_cleaned = s3.replace(" ", "").replace("-", "").upper()
s4_cleaned = s4.replace(" ", "").replace("-", "").upper()

print(f"{s1}(은)는 {s1_cleaned}(으)로 수정됨")
print(f"{s2}(은)는 {s2_cleaned}(으)로 수정됨")
print(f"{s3}(은)는 {s3_cleaned}(으)로 수정됨")
print(f"{s4}(은)는 {s4_cleaned}(으)로 수정됨\n")

print(f"{s1_cleaned}: {s1_cleaned.count('N')} 개의 N이 나타남")
print(f"{s2_cleaned}: {s2_cleaned.count('N')} 개의 N이 나타남")
print(f"{s3_cleaned}: {s3_cleaned.count('N')} 개의 N이 나타남")
print(f"{s4_cleaned}: {s4_cleaned.count('N')} 개의 N이 나타남")

#4.26
input_string = "Park(Java city), Kim(C city), Kang(Bython city), Lee(Bython city), Hong(Ruby city), Cho(Bython city), Koo(C city), Ryu(C++ city)"

modified_string = input_string.replace("Bython", "Python")
count = input_string.count("Bython")

print("주어진 문자열:", input_string)
print("수정된 문자열:", modified_string)
print(f"'Bython' 문자열은 모두 {count}번 수정했습니다.")

#4.27
rac = float(input("1보다 작고 0보다 큰 소수를 입력하세요: "))

closest_fraction = (1, 1)
min_difference = 1

for denominator in range(1, 1000):
    numerator = round(denominator * rac)
    difference = abs(numerator / denominator - rac)
    if difference < min_difference:
        min_difference = difference
        closest_fraction = (numerator, denominator)

result_fraction = f"{closest_fraction[0] / closest_fraction[1]:.15f}"

print(f"가장 가까운 단위 분수는 {closest_fraction[0]}/{closest_fraction[1]}이며, 이 값은 {result_fraction}입니다.")

#5.17
#(1)
animals = ['dog', 'cat', 'tiger', 'lion']
print("animals =", animals)
#(2)
animals = ['dog', 'cat', 'tiger', 'lion']

first_element = animals.pop(0)
animals.append(first_element)

print("animals =", animals)

#(3)
animals = ['dog', 'cat', 'tiger', 'lion']

print("animals =", animals)

for animal in animals:
    print(f"I love {animal}.")

#5.18
#(1)
s_list = ['abc', 'bcd', 'bedefg', 'abba', 'cdde', 'opa']

shortest_string = s_list[0]
for string in s_list:
    if len(string) < len(shortest_string):
        shortest_string = string

print("가장 길이가 짧은 문자열:", shortest_string)

#(2)
s_list = ['abc', 'bcd', 'bedefg', 'abba', 'cdde', 'opa']

longest_string = s_list[0]
for string in s_list:
    if len(string) > len(longest_string):
        longest_string = string

print("가장 길이가 긴 문자열:", longest_string)

#(3)
s_list = ['abc', 'bcd', 'opq', 'abcd', 'bcde', 'opqr']

s_list.sort(key=len)

shortest_length = len(s_list[0])
shortest_strings = [string for string in s_list if len(string) == shortest_length]

print("가장 길이가 짧은 문자열:", ", ".join(f"'{string}'" for string in shortest_strings))

#5.19
s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']

new_s_list = []

for string in s_list:
    if string not in new_s_list and string != 'abc' and string != 'opq':
        new_s_list.append(string)

print("s_list =", s_list)
print("new_s_list =", new_s_list)

#5.20
src = 'aaaabbb'
compressed = ''
count = 1

for i in range(1, len(src)):
    if src[i] == src[i - 1]:
        count += 1
    else:
        compressed += src[i - 1] + str(count)
        count = 1

compressed += src[-1] + str(count)

print("src =", src)
print("output =", compressed)

src = 'aaaabccccaaaaacccfg'
compressed = ''
count = 1

for i in range(1, len(src)):
    if src[i] == src[i - 1]:
        count += 1
    else:
        compressed += src[i - 1] + str(count)
        count = 1

compressed += src[-1] + str(count)

print("src =", src)
print("output =", compressed)

#5.21
src = 'a263c6a2c3f1g1'

decompressed = ''
for i in range(0, len(src), 2):
    char = src[i]
    count = int(src[i + 1])
    decompressed += char * count

print("src =", "'" + src + "'")
print("output =", "'" + decompressed + "'")

#5.22
n = int(input("n을 입력하시오: "))

array = [[0] * n for _ in range(n)]
num = 1
for i in range(n):
    if i % 2 == 0:
        for j in range(n):
            array[i][j] = num
            num += 1
    else:
        for j in range(n - 1, -1, -1):
            array[i][j] = num
            num += 1

for row in array:
    print(" ".join(map(str, row)))

#5.23
#(1)
def how_many_persons(person_list):
    num_persons = len(person_list) // 5
    return num_persons

person1 = ['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.6]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['혁거세', 40, 1, 150.0, 50.0]
person_list = person1 + person2 + person3 + person4

n_persons = how_many_persons(person_list)
print(str(n_persons) + '명의 정보가 담겨 있습니다.')

#(2)
def compute_average_age(person_list):
    num_persons = len(person_list) // 5
    total_age = 0
    for i in range(num_persons):
        total_age += person_list[i * 5 + 1]
    average_age = total_age / num_persons
    return average_age

person1 = ['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.6]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['혁거세', 40, 1, 150.0, 50.0]
person_list = person1 + person2 + person3 + person4

average_age = compute_average_age(person_list)
print('평균 나이는 ' + str(average_age) + '세입니다.')

#(3)
def count_males_females(person_list):
    num_persons = len(person_list) // 5
    n_male = 0
    n_female = 0
    for i in range(num_persons):
        gender = person_list[i * 5 + 2]
        if gender == 1:
            n_male += 1
        elif gender == 0:
            n_female += 1
    return n_male, n_female

person1 = ['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.6]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['혁거세', 40, 1, 150.0, 50.0]
person_list = person1 + person2 + person3 + person4

n_male, n_female = count_males_females(person_list)
print('리스트에는 남자가', n_male, '명, 여자가', n_female, '명입니다.')

#(4)
def display_persons(person_list):
    num_persons = len(person_list) // 5
    for i in range(num_persons):
        person_info = person_list[i * 5: (i + 1) * 5]
        print(person_info)

person1 = ['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['혁거세', 40, 1, 150.0, 50.0]
person_list = person1 + person2 + person3 + person4

display_persons(person_list)
