# 학번 2021304061
# 이름 이지민

#4-1번
def my_greet():
    print('환영합니다.')

my_greet()
my_greet()


#4-2번
def squre(n):
    return n ** 2
    
print('3의 제곱은 : ',squre(3))
print('3의 제곱은 : ',squre(4))

#4-24번
import re
def sort_sentence_words():
    sentence = input('여러 단어로 이루어진 글을 입력하세요: ')
    cleaned_sentence = re.sub(r'[,.:;]',' ',sentence)
    words = cleaned_sentence.split()
    sorted_words = sorted(words)
    print('정렬 결과 : ')
    print(sorted_words)
sort_sentence_words()


#4-25번

s1 = 'kang Young Min'
s2 = ' kang Young-Min'
s3 = 'park Dong Min'
s4 = ' park Dong-Yun'

def format_and_count_n(s):
    formatted_s =s.replace(" ","").replace("-","").upper()
    n_count = formatted_s.count("N")
    return formatted_s, n_count
for s in [s1,s2,s3,s4]:
    formatted_s, n_count = format_and_count_n(s)
    print(s,'(은)는',formatted_s,'(으)로 수정됨')
    
for s in [s1,s2,s3,s4]:
    formatted_s, n_count = format_and_count_n(s)
    print(formatted_s,":",n_count,"개의 N이 나타남")

#4-26번
original_string = "park(java city), kim(C city ), kang(Bython city), Lee(Bython city), Hong(Ruby city), cho(Bython city), koo(C city), Ryu(C++ city)"
modified_string = original_string.replace("Bython", "Python")
count = original_string.count("Bython")

print("주어진 문자열 :", original_string)
print("수정된 문자열 :", modified_string)
print(f"Bython 문자열은 모두 {count}번 수정했습니다.")

#4-27번
def unit_fraction(frac):
    denominator = round(1 / frac)
    closest_fraction = 1 / denominator
    return denominator, closest_fraction

frac_input = float(input("1보다 작고 0보다 큰 소수를 입력하세요: "))

closest_denominator, closest_fraction = unit_fraction(frac_input)
print(f"가장 가까운 단위 분수는 1/{closest_denominator}이며, 이 값은 {closest_fraction}입니다.")

#5-17번,1)번
animals = ['dog', 'cat', 'tiger', 'lion']
print("animals =", animals)

#5-17번,2)번
animals = ['dog', 'cat', 'tiger', 'lion']

first_element = animals.pop(0)
animals.append(first_element)
print("animals =", animals)

#5-17번,3)번
animals = ['dog', 'cat', 'tiger', 'lion']

print("animals =", animals)
for animal in animals:
    print(f"I love {animal}.")

#5-18번,1)번
s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']

shortest_string = s_list[0]
for s in s_list:
    if len(s) < len(shortest_string):
        shortest_string = s
print(f'가장 길이가 짧은 문자열: {shortest_string}')

#5-18번,2)
s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']
longest_string = s_list[0]  # 첫 번째 요소를 초기 가장 긴 문자열로 설정
for s in s_list:
    if len(s) > len(longest_string):
        longest_string = s

print(f'가장 길이가 긴 문자열: {longest_string}')

#5-18번 3)
s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']

s_list.sort(key=len)

shortest_length = len(s_list[0])


print('가장 길이가 짧은 문자열들:')
for s in s_list:
    if len(s) == shortest_length:
        print(s)
    else:
        break 

#5-19번 
s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']

print('s_list =', s_list)
from collections import OrderedDict
s_list_no_duplicates = list(OrderedDict.fromkeys(s_list))

new_s_list = [s for s in s_list_no_duplicates if s not in ['abc', 'opq']]

new_s_list.insert(0, 'abc') 
new_s_list.append('opq') 

print('new_s_list =', new_s_list)

#5-20번 
def compress_string(src):
    if not src:
        return ""
    output = src[0]  
    count = 1 
    for i in range(1, len(src)):
        if src[i] == src[i-1]:
            count += 1
        else:
            output += str(count)
            output += src[i]
            count = 1
    
    output += str(count)

    return output
src = input("scr: ")
output = compress_string(src)
print("output:", output)

#5-21번
def decompress_string(compressed_str):
    decompressed = ""  
    i = 0  

    while i < len(compressed_str):
        char = compressed_str[i]  
        i += 1
        repeat_count = ""  

        while i < len(compressed_str) and compressed_str[i].isdigit():
            repeat_count += compressed_str[i]
            i += 1
        
        if repeat_count == "":
            repeat_count = "1"  

    
        decompressed += char * int(repeat_count)

    return decompressed

compressed_str = 'a2b3c6a2c3flg1'

decompressed_str = decompress_string(compressed_str)
print('src =',compressed_str)
print("output =", decompressed_str)

#5-22번
def print_snake_matrix(n):
    matrix = [[0] * n for _ in range(n)]  
    num = 1 
    for i in range(n):
        if i % 2 == 0:
          
            matrix[i][:] = range(num, num + n)
        else:
          
            matrix[i][:] = range(num + n - 1, num - 1, -1)

        num += n 

    for row in matrix:
        print(" ".join(map(str, row)))

n = int(input("n을 입력하시오 : "))

if 1 < n < 10:
    print_snake_matrix(n)
else:
    print("입력 값이 조건에 맞지 않습니다.")

#5-23번,1)번
def how_many_persons(person_list):
    count = len(person_list) // 5
    return count
person1 = ['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부',25,1,170.0,70.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['헉거세',40,1,150.0,50.0]

person_list = person1 +person3 +person4
print(how_many_persons(person_list),'명의 정보가 담겨 있습니다.')

#5-23번,2)번
def compute_average_age(person_list):

    total_age = 0
    for i in range(1, len(person_list), 5):
        total_age += person_list[i]
    
    number_of_people = len(person_list) // 5
    
    average = total_age / number_of_people
    return average

person1 = ['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부',25,1,170.0,70.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['헉거세',40,1,150.0,50.0]

person_list = person1 +person2 +person3 +person4
average_age =compute_average_age(person_list)
print('평균 나이는 ' +str(average_age) +'세입니다.')

#5-23번,3)번
def count_males_females(person_list):
    n_male = 0
    n_female = 0

    for i in range(2, len(person_list), 5):
        if person_list[i] == 1:
            n_male += 1
        elif person_list[i] == 0:
            n_female += 1
    
    return n_male,n_female
person1 = ['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부',25,1,170.0,70.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['헉거세',40,1,150.0,50.0]

person_list = person1 +person2 +person3 +person4
n_male,n_female = count_males_females(person_list)
print("리스트에는 남자가:",n_male,'명, 여자가',n_female,'명입니다.')

#5-23번,4)번
def display_persons(person_list):
    for i in range(0, len(person_list), 5):
        print(person_list[i:i+5])

person1 = ['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['헉거세', 40, 1, 500.0, 50.0]

person_list = person1 + person2 + person3 + person4
display_persons(person_list)

