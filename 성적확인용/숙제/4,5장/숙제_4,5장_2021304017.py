# 학번 2021304017
# 이름 김연우

# 4-1
def my_greet():
    print('환영합니다.')

    
my_greet()
my_greet()

# 4-2
def square(n):
   return n**2

print('3의 제곱은 : ', square(3))
print('4의 제곱은 : ', square(4))

# 4-24
import re
def main():
    input_sentence = input("여러 단어로 이루어진 글을 입력하세요: ")
    
    words = re.findall(r'\b\w+\b', input_sentence.lower())
    
    sorted_words = sorted(words)
    
    print("정렬 결과:")
    print(sorted_words)

    
if __name__ == "__main__":
    main()


# 4-25
def remove_space_hyphen_and_count_N(s):
    s_modified = s.replace(' ', '').replace('-', '').upper()
    count_N = s_modified.count('N')
    return s_modified, count_N

def main():
    s1 = 'Kang Young Min'
    s2 = ' Kang Young-Min'
    s3 = 'Park Dong Min'
    s4 = ' Park Dong-Yun'

    strings = [s1, s2, s3, s4]
    for s in strings:
        modified_string, count_N = remove_space_hyphen_and_count_N(s)
        print(f"{s} (은)는 {modified_string}(으)로 수정됨")
        print(f"{modified_string} : {count_N} 개의 N이 나타남")

        
if __name__ == "__main__":
    main()

    

# 4-26
def replace_bython_with_python(s):
    count_replace = s.count('Bython')
    modified_string = s.replace('Bython', 'Python')
    return modified_string, count_replace

def main():
    original_string = "Park(Java city), Kim(C city), Kang(Bython city), Lee(Bython city), Hong(Ruby city), Cho(Bython city), Koo(C city), Ryu(C++ city)"

    modified_string, count_replace = replace_bython_with_python(original_string)

    print("주어진 문자열:")
    print(original_string)
    print("\n수정된 문자열:")
    print(modified_string)
    print(f"\nBython 문자열은 모두 {count_replace}번 수정했습니다.")

    
if __name__ == "__main__":
    main()

    

# 4-27
def unit_fraction(frac):
    n = 1
    diff = 1.0
    while True:
        new_diff = abs(1/n - frac)
        if (new_diff <= diff):
            diff = new_diff      
        else:
            break
        n += 1
    return n - 1

f_val = float(input("1보다 작고 0보다 큰 소수를 입력하세요: "))
if f_val <= 0.0 or f_val > 1.0 :
    print('입력 오류입니다.')
else :
    nf = unit_fraction(f_val)
    print('가장 가까운 단위분수는 1/{0}이며, 이 값은 {1:.17f}입니다.'.format(nf, 1/nf))

    

# 5-17
#1
animals = ['dog', 'cat', 'tiger', 'lion']
print("animals =", animals)

#2
animals = ['dog', 'cat', 'tiger', 'lion']
animals.append(animals.pop(0))
print("animals =", animals)

#3
animals = ['dog', 'cat', 'tiger', 'lion']
print("animals =", animals)
for animal in animals:
    print("I love", animal + ".")

    

# 5-18
#1
s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']
shortest_length = float('inf')
shortest_strings = []
for s in s_list:
    if len(s) < shortest_length:
        shortest_length = len(s)
        shortest_strings = [s]
    elif len(s) == shortest_length:
        shortest_strings.append(s)

        
print("가장 길이가 짧은 문자열:", shortest_strings[0])


#2
s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']
longest_length = 0
longest_string = ''
for s in s_list:
    if len(s) > longest_length:
        longest_length = len(s)
        longest_string = s

        
print("가장 길이가 긴 문자열:", longest_string)


#3
s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']
s_list.sort(key=len)
print("가장 길이가 짧은 문자열:", s_list[:3])

# 5-19
s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
new_s_list = []
for s in s_list:
    if s not in new_s_list:
        new_s_list.append(s)

print("s_list =", s_list)
print("new_s_list =", new_s_list)

# 5-20
def compress_string(src):
    if not src:
        return src
    compressed = ""
    count = 1
    for i in range(len(src) - 1):
        if src[i] == src[i + 1]:
            count += 1
        else:
            compressed += src[i] + str(count)
            count = 1
    compressed += src[-1] + str(count)
    return compressed

examples = ['aaaabbb','aaaabccccaaaaacccfg','','a']
for src in examples:
    output = compress_string(src)
    print(f"src = '{src}' \noutput = '{output}'")

    

# 5-21
def decompress_string(src):
    decompressed = ""
    count = ""
    current_char = src[0]
    for char in src[1:]:
        if char.isdigit():
            count += char
        else:
            decompressed += current_char * int(count)
            current_char = char
            count = ""
    decompressed += current_char * int(count)
    return decompressed

src = 'a2b3c6a2c3f1g1'
output = decompress_string(src)
print(f"src = '{src}'\noutput = '{output}'")

# 5-22
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

    

# 5-23-1
def how_many_persons(person_list):
    return len(person_list) // 5

person1 = ['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['혁거세', 40, 1, 150.0, 50.0]

person_list = person1 + person3 + person4
n_persons = how_many_persons(person_list)
print(str(n_persons) + '명의 정보가 담겨 있습니다.')

# 5-23-2
def compute_average_age(person_list):
    n=int(len(person_list)/5) 
    t_age=0
    for i in range(n):
        t_age += person_list[5*i + 1] 
    return t_age/n

person1 = ['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['혁거세', 40, 1, 150.0, 50.0]

person_list = person1 + person2 + person3 + person4
average_age = compute_average_age(person_list)
print('평균 나이는 ' + str(average_age) +'세입니다.')

# 5-23-3
def count_males_females(person_list):
    n=int(len(person_list)/5) 
    cmf=0
    for i in range(n):
        cmf += person_list[5*i + 2] 
    return cmf,n-cmf

person1 = ['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['혁거세', 40, 1, 150.0, 50.0]

person_list = person1 + person2 + person3 + person4
n_male, n_female = count_males_females(person_list)
print('리스트에는 남자가', n_male, '명, 여자가', n_female, '명입니다.')

# 5-23-4
def display_persons(person_list):
    for i in range(0, len(person_list), 5):
        person_info = person_list[i:i+5]  
        print(person_info)

person1 = ['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['혁거세', 40, 1, 150.0, 50.0]

person_list = person1 + person2 + person3 + person4
display_persons(person_list)
