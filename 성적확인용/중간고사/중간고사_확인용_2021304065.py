'''
        파이썬 프로그래밍(EN1004-04) / 프로그래밍언어기초및실습(EE1201-04)
        중간고사                          학번: 2021304065
                                          이름: 이태희
'''


'''
합계: 16.5점

##### 객관식 문제 성적 (문항당 만점: 1점) #####
          제출한 답안     정답         점수   
문제 1.     1, 3       1          0.5  
문제 2.     4, 5       1          0    
문제 3.     3, 4       2, 5       0    
문제 4.     3          3          1    
문제 5.     5          5          1    
문제 6.     1, 2, 3, 4, 5    2          0.5  
문제 7.     1, 2       3, 4       0    
문제 8.     2, 4       3          0    
문제 9.     2, 3       3          0.5  
문제 9.     1, 5       1, 5       1    
문제 10.    1          1          1    
합계.                             5.5  

##### 주관식 문제 성적 (문항당 만점: 2점) #####
문제 11. list(p6_str)                                         2점
        p6_str[_:] + p6_str[:_]
문제 12. list(p6_str)                                         1점
        p6_str[2:] + p6_str[:2]
문제 13. .index(a)                                            1점

문제 14.

문제 15.

문제 16.

문제 17.

합계.                                  

##### 서술형 문제 성적 (문항당 만점: 3점) #####
문제 18.

문제 19.

문제 20-1.                                                    1점
def my_format_int(int_data, width = 0):    
    print('int_data : ',int_data)
    print('width :',width)

int_data = int(input('int_data : '))
width = int(input('width : '))

my_format_int(int_data,width)

문제 20-2.                                                    1점
def my_format_float(float_data, width = 0, precision = 6):
    print('float_data : ',float_data)
    print('width :',width)
    print("precision :",precision)
    
float_data = float(input('float_data : '))
width = float(input('width : '))
precision = float(input('precision : '))

my_format_float(float_data,width,precision)

합계.                                                         2점

'''

''' 객관식 문제 제출된 코드
# 문제 1:
# item을 문자열로 변환해서 반환해주는 my_str(item) 코드에서
# 주석 처리된 자리에 들어갈 코드로 알맞는 항목을 모두 고르시오

def my_str(item):
    if type(item) == str:
        return "'" + item + "'"
    else:
        return  # 주석 처리된 자리


# 1. str(item)
# 2. item
# 3. 'item'
# 4. string(item)
# 5. item.string()

# 정답: 1 3


# 문제 2:
# 리스트 my_list를 문자열로 변환해서 반환해주는 my_str(item) 코드에서
# index에 해당하는 항목을 출력하기 전에 지정된 문자열을 앞에 붙여서
# 출력하려고 할 때 주석 처리된 자리에 들어갈 적절한 코드를 모두 고르시오.

def my_marked_str_of_list(my_list, index):
    mark_char = '#'
    ret = '['
    for i in range(0, index):
        ret += my_str(my_list[i]) + ', '

    if index == len(my_list) - 1:
        return ret + mark_char + my_str(my_list[index]) + ']'
    else:
        # 주석 처리된 자리
        for i in range(index, len(my_list) - 1):
            ret += my_str(my_list[i]) + ', '
        return ret + my_str(my_list[-1]) + ']'


# 1. ret += mark_char
# 2. ret = ret + mark_char + my_str(my_list[index]) + ', '
# 3. ret += my_str(my_list[index]) + ', '
# 4. i = 0
# 5. i = index

# 정답: 4 5


# 문제 3:
# 리스트 p1_list에서 비어있는 튜플, 비어있는 리스트, 비어있는 문자열을
# 제거한 리스트를 p1_output에 저장하는 다음 코드에서
# 주석 처리된 자리에 들어갈 적절한 코드를 모두 고르시오.

p1_list = [(), 1, (), (), (1,), ('a',), ('a', 'b'), ((),), ('a', 'b'), '']
print("Problem 1. input =", p1_list)
print()

p1_output = []
i = 0
for item in p1_list:
    print(my_marked_str_of_list(p1_list, i))
    if item not in ((), [], ''):
        print(my_str(item), 'is not empty')
        # 주석처리된 자리
    else:
        print(my_str(item), 'is empty')
    print("p1_output =", p1_output)
    print()
    i += 1


# 1. p1_output.add(item)
# 2. p1_output.append(item)
# 3. p1_output.remove(item)
# 4. p1_output.pop(i)
# 5. p1_output.insert(0, item)

# 정답: 3 4


# 문제 4:
# 매개변수 x를 문자열로 변환했을 때, 문자열의 길이 만큼에 해당하는
# 공백 문자열을 반환하는 space_same_len(x) 함수에서
# 주석처리한 자리에 들어갈 적절한 코드를 고르시오

def space_same_len(x):
    return ' '  # 주석처리한 자리


# 1. * str(x)
# 2. ** len(str(x))
# 3. * len(str(x))
# 4. + len(str(x))
# 5. + str(x)

# 정답: 3


# 문제 5:
# 매개변수 x를 문자열로 변환했을 때, 문자열의 길이 만큼에 해당하는
# 문자열을 반환하는 space_same_len(x) 함수에서 문자열의 가운데 문자가
# ^ 이고, 나머지 문자는 공백으로 하기 위해서
# 주석처리한 자리에 들어갈 적절한 코드를 고르시오

def mark_middle(x):
    num_left_spaces = len(str(x)) // 2 - 1
    num_right_spaces = len(str(x)) // 2 + len(str(x)) % 2
    return ' '  # 주석처리된 자리


# 1. + '^' * num_right_spaces
# 2. + '^'
# 3. * len(str(x)) + '^' + ' '
# 4. + '^' + ' ' * num_right_spaces
# 5. * num_left_spaces + '^' + ' ' * num_right_spaces

# 정답: 5


# 문제 6:
# 리스트 my_list를 문자열로 반환한 것과 같은 길이의 문자열을 변환하는데
# 매개변수 index가 인덱스인 항목의 가운데 위치에 특별한 문자가 표시되고
# 나머지 문자들은 모두 공백이 되게 하는 mark_index_of_list 함수 코드에서
# 주석 처리된 자리에 들어갈 적절한 코드를 모두 고르시오.

def mark_index_of_list(my_list, index):
    space = ' '
    ret = space
    for item in my_list[:index]:
        ret += space_same_len(item)  # 주석처리된 자리
    return ret + mark_middle(my_list[index]) + space * 2


# 1. + space*1
# 2. + space*2
# 3. + space*3
# 4. + space*4
# 5. + space*5

# 정답: 1 2 3 4 5


# 문제 7:
# 리스트 p1_list에서 비어있는 튜플, 비어있는 리스트, 비어있는 문자열을
# 제거한 리스트를 p1_output에 저장하는 다음 코드에서
# 주석 처리된 자리에 들어갈 적절한 코드를 모두 고르시오.

p1_output = p1_list.copy()
print("\n" * 5 + str(p1_output) + '\n')
for i in range(len(p1_output) - 1, -1, -1):
    item = p1_output[i]
    if item not in ((), [], ''):
        pass
    else:
        print(mark_index_of_list(p1_output, i))
        print(my_str(item), 'is empty')
        # 주석처리된 자리
        print("\n" * 2)
        print(p1_output)
        print()

# 1. p1_output.append(item)
# 2. p1_output.insert(i, item)
# 3. p1_output.remove(item)
# 4. p1_output.pop(i)
# 5. p1_output.add(item)

# 정답: 1 2


# 문제 8:
# 리스트에서 가장 큰 항목을 가장 오른쪽으로 이동하는 다음 코드에서
# 주석처리된 자리에 들어갈 적절한 코드를 모두 고르시오

p2_list = [5, 6, 3, 9, 2, 12, 3, 8, 7]
index_end = 0  # 주석 처리된 자리
for i in range(0, index_end):
    if p2_list[i] > p2_list[i + 1]:
        p2_list[i], p2_list[i + 1] = p2_list[i + 1], p2_list[i]
    print(p2_list)

print()

# 1. + len(p2_list)
# 2. + 0
# 3. + len(p2_list) - 1
# 4. + 1
# 5. + len(p2_list) + 1

# 정답: 2 4


# 문제 9:
# 리스트에서 가장 큰 항목을 가장 오른쪽으로 반복적으로 이동해서
# 리스트의 모든 항목을 작은 값부터 큰 값까지 순서대로 배열하려고 할 때
# 주석처리된 자리에 들어갈 적절한 코드를 모두 고르시오


for j in range(0, len(p2_list) - 1):
    end_point = 0  # 주석 처리된 자리
    for i in range(0, end_point):
        if p2_list[i] > p2_list[i + 1]:
            p2_list[i], p2_list[i + 1] = p2_list[i + 1], p2_list[i]
    print(p2_list)

print()

# 1. + len(p2_list)
# 2. + j
# 3. + len(p2_list) - 1
# 4. + 0
# 5. + len(p2_list) + 1

# 정답: 2 3


# 문제 9:
# 리스트에서 가장 큰 항목을 가장 오른쪽으로 반복적으로 이동해서
# 리스트의 모든 항목을 작은 값부터 큰 값까지 순서대로 배열하려고 할 때
# 반복 중간중간에 정렬된 부분과 정렬되지 않은 부분을 분리해서 출력하기위해
# 주석처리된 자리에 들어갈 적절한 코드를 모두 고르시오

p3_list = [5, 6, 31, 9, 2, 12, 3, 8, 7]
for j in range(len(p3_list) - 1, 0, -1):
    for i in range(0, j):
        if p3_list[i] > p3_list[i + 1]:
            p3_list[i], p3_list[i + 1] = p3_list[i + 1], p3_list[i]
    # 주석 처리된 자리
print(p3_list)
print()

# 1. print(str(p3_list[:j])+',', p3_list[j:])
# 2. print(p3_list[0:j])
# 3. print(p3_list[j:])
# 4. print(p3_list[:])
# 5. print(p3_list[0:j], p3_list[j:-1])

# 정답: 1 5


# 문제 10:
# 문자열이 순서를 거꾸로 해도 똑같은지 확인하는 is_palindrome 함수에서
# 띄어쓰기는 처리하지 않으려고 할 때 주석처리된 자리에 알맞는 코드를 고르시오.

p4_tuple = (4, 5, 2, 3, 8, 1, 9, 0)
for i in range(len(p4_tuple), 0, -1):
    print(p4_tuple[0:i])


def is_palindrome(x):
    print(x)
    l = 0
    r = len(x) - 1
    while (l < r):
        while (x[l] != ' '):
            l += 1
        while (x[r] != ' '):
            r -= 1
        if x[l] != x[r]:
            return False
        else:
            _ = 0
            # 주석처리된 자리

    return True


p5_str = "a nut for a jar of tuna"
print(is_palindrome(p5_str))

# 1.
#   l += 1
#   r -= 1
# 2.
#   l += 1
# 3.
#   r += 1
# 4.
#   l -= 1
#   r -= 1
# 5.
#   l = r = 0

# 정답: 1


'''



# 주관식, 서술형 문제 성적 산출 코드

# 문제 11.
# p6_str을 i칸 왼쪽으로 회전시켜서 출력하시오

p6_str = "ABCDEFGHIJKLMNOPQURSTUVWXYZ"

for i in range(0, len(p6_str)):
    _ = i

# 정답 :list(p6_str)
#       p6_str[_:] + p6_str[:_]

# 문제 12.
# p7_dst_str을 p7_src_str에서 세칸 왼쪽으로 회전시켜서 구하시오

p7_src_str = "ABCDEFGHIJKLMNOPQURSTUVWXYZ"
p7_dst_str = p7_src_str  # 코드를 입력할 위치


# 정답 :list(p6_str)
#       p6_str[2:] + p6_str[:2]


# 문제 13
# a의 src_str에서 인덱스를 index 함수로 구한 뒤 dst_str의 해당 인덱스 문자열을
# 반환하는 ciper(a) 함수에서 주석처리된 부분에 들어갈 코드를 쓰시오.

def ciper(a):
    return p7_dst_str  # 주석 처리된 부분


print(p7_src_str.index('A'), ciper('A'))
print(p7_src_str.index('B'), ciper('B'))


# 정답: .index(a)


# 문제 14
# 입력받은 문자열에 대해서 모든 문자를 암호화하는 ciper_all함수에서
# 주석 처리된 부분에 적절한 코드를 쓰시오

def ciper_all(decoded_str):
    # 주석처리된 부분
    for a in decoded_str:
        if a in p7_src_str:
            encoded_str += ciper(a)
        else:
            encoded_str += a
    return encoded_str


p7_my_str = "ATTACK TONIGHT!"
print(ciper_all(p7_my_str))

# 정답:


# 문제 15

p7과
같이
p8_src_str에서
ciper(a), ciper_all(decoded_str)
을
구현하시오
p8_src_str = "ABCDEFGHIJKLMNOPQURSTUVWXYZabcdefghijklmnopqrstuvwxyz"
p8_dst_str = p8_src_str[3:] + p8_src_str[:3]


def ciper(a):
    _ = a


def ciper_all(decoded_str):
    _ = decoded_str


p8_my_str = "Veni, vidi, vici."
print(ciper_all(p8_my_str))


# 문제 16.
# my_string에서 모든 공백문자를 제거한 문자열을 반환하는
# remove_space(my_string)을 구현하시오

def remove_space(my_string):
    ret = ' '
    my_string = my_string.remove(ret)

    return my_string


# 문제 17.
# my_string에서 index로 부터 하나씩 양쪽으로 뻗어나가는 회문의
# 가장 긴 길이를 구하고, 회문 문자열, 회문의 길이를 반환하시오

def longest_odd_palindromic_from_root(my_string, index):
    i = 1
    ret = my_string
    return ret, i


# 문제 18.
# my_string에서 index와 index+1로 부터 하나씩 양쪽으로 뻗어나가는 회문의
# 가장 긴 길이를 구하고, 회문 문자열, 회문의 길이를 반환하시오

def longest_even_palindromic_from_root(my_string, index):
    i = 1
    ret = my_string
    return ret, i


# 문제 19.
# p9_my_str 내에서 가장 긴 회문을 찾아서 출력하시오

p9_my_str = "ATTACK"
print("longest palindromic string")


# 문제 20-1
# 정수 데이터와 필드폭을 받아서 해당 문자열을 출력하시오
def my_format_int(int_data, width=0):
    print('int_data : ', int_data)
    print('width :', width)


int_data = int(input('int_data : '))
width = int(input('width : '))

my_format_int(int_data, width)


# 문제 20-2
# 실수 데이터와 필드폭과 정밀도를 받아서 해당 문자열을 출력하시오
def my_format_float(float_data, width=0, precision=6):
    print('float_data : ', float_data)
    print('width :', width)
    print("precision :", precision)


float_data = float(input('float_data : '))
width = float(input('width : '))
precision = float(input('precision : '))

my_format_float(float_data, width, precision)