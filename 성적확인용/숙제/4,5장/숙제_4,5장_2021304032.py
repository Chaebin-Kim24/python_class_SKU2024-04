# 학번 2021304032
# 이름 박지원 

# 4.26

s1 = 'Park(Java city)'
s2 = 'Kim(C city)'
s3 = 'Kang(Bython city)'
s4 = 'Lee(Bython city)'
s5 = 'Hong(Ruby city)'
s6 = 'Cho(Bython city)'
s7 = 'Koo(C city)'
s8 = 'Ryu(C++ city)'

original_strings = [s1, s2, s3, s4, s5, s6, s7, s8]
print('주어진 문자열:')
print(', '.join(original_strings))

modified_strings = [string.replace('Bython', 'Python') for string in original_strings]
print('\n주어진 문자열:')
print(', '.join(modified_strings))

change_count = sum(string.count('Bython') for string in original_strings)
print('\nBython 문자열은 모두', change_count, '번 수정했습니다')

# 5.17

animals = ['dog', 'cat', 'tiger', 'lion']
animals
animals[1:]+animals[:1] 
for animal in animals:
    print('I love', animal)

# 5.18

s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']

shortest_string = s_list[0] 
for string in s_list[1:]:  
    if len(string) < len(shortest_string): 
        shortest_string = string

print("가장 길이가 짧은 문자열:", shortest_string)

longest_string = s_list[0] 
for string in s_list[1:]:  
    if len(string) > len(longest_string): 
        longest_string = string

print("가장 길이가 긴 문자열:", longest_string)

s_list.sort(key=len)

shortest_length = len(s_list[0])

for string in s_list:
    if len(string) == shortest_length:
        print(string)
    else:
        break

# 5.19

s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
print(s_list)

new_list = []

for item in s_list:
    if item not in new_list:
        new_list.append(item)
print(new_list)

# 5.20
def compress_string(src):
    compressed_string = ""
    count = 1
    
    for i in range(1, len(src)):
        if src[i] == src[i - 1]:
            count += 1
        else:
            compressed_string += src[i - 1] + str(count)
            count = 1
    
    compressed_string += src[-1] + str(count)
    
    return compressed_string

src = 'aaaabccccaaaaacccfg'
output = compress_string(src)
print(output)

def compress_string(src):
    if not src:  # 빈 문자열인 경우
        return ""
    
    compressed_string = ""
    count = 1
    
    for i in range(1, len(src)):
        if src[i] == src[i - 1]:
            count += 1
        else:
            compressed_string += src[i - 1] + str(count)
            count = 1
    
    compressed_string += src[-1] + str(count)
    
    return compressed_string

src = ''
output = compress_string(src)
print(output)

src = 'a'
output = compress_string(src)
print(output)

# 5.21

def decompress_string(src):
    decompressed_string = ""
    current_char = ""
    count = ""

    for char in src:
        if char.isalpha():  
            decompressed_string += current_char * int(count) if current_char else ""  
            current_char = char 
            count = ""  
        else:
            count += char  

    decompressed_string += current_char * int(count) if current_char else ""
    
    return decompressed_string

src = 'a2b3c6a2c3f1g1'
output = decompress_string(src)
print(output)

# 5.22

n = int(input("n을 입력하시오: "))

snake_matrix = []

for i in range(1, n**2 + 1, n):
    row = list(range(i, i + n))
    if len(snake_matrix) % 2 == 1:
        row = row[::-1]
    snake_matrix.append(row)

for row in snake_matrix:
    print(*row)
