
'''
        ���̽� ���α׷���(EN1004-04) / ���α׷��־����ʹ׽ǽ�(EE1201-04)
        �߰����                          �й�:
                                          �̸�:
'''


# ���� 1:
# item�� ���ڿ��� ��ȯ�ؼ� ��ȯ���ִ� my_str(item) �ڵ忡��
# �ּ� ó���� �ڸ��� �� �ڵ�� �˸´� �׸��� ��� ���ÿ�

def my_str(item):
    if type(item) == str:
        return "'" + item + "'"
    else:
        return # �ּ� ó���� �ڸ�

# 1. str(item)
# 2. item
# 3. 'item'
# 4. string(item)
# 5. item.string()
    
# ����: 



# ���� 2:
# ����Ʈ my_list�� ���ڿ��� ��ȯ�ؼ� ��ȯ���ִ� my_str(item) �ڵ忡��
# index�� �ش��ϴ� �׸��� ����ϱ� ���� ������ ���ڿ��� �տ� �ٿ���
# ����Ϸ��� �� �� �ּ� ó���� �ڸ��� �� ������ �ڵ带 ��� ���ÿ�.   

def my_marked_str_of_list(my_list, index):
    mark_char = '#'
    ret = '['
    for i in range(0, index):
        ret += my_str(my_list[i]) + ', '

    if index == len(my_list) - 1:
        return ret + mark_char + my_str(my_list[index]) + ']' 
    else:
        # �ּ� ó���� �ڸ�
        for i in range(index, len(my_list)-1):
            ret += my_str(my_list[i]) + ', '
        return ret + my_str(my_list[-1]) + ']'

# 1. ret += mark_char
# 2. ret = ret + mark_char + my_str(my_list[index]) + ', '
# 3. ret += my_str(my_list[index]) + ', '
# 4. i = 0
# 5. i = index 

# ����: 


# ���� 3:
# ����Ʈ p1_list���� ����ִ� Ʃ��, ����ִ� ����Ʈ, ����ִ� ���ڿ���
# ������ ����Ʈ�� p1_output�� �����ϴ� ���� �ڵ忡��
# �ּ� ó���� �ڸ��� �� ������ �ڵ带 ��� ���ÿ�.    
    
p1_list = [(), 1, (), (), (1,), ('a',), ('a', 'b'), ((),), ('a', 'b'), '']
print("Problem 1. input =", p1_list)
print()

p1_output = []
i = 0
for item in p1_list:
    print(my_marked_str_of_list(p1_list, i))
    if item not in ((), [], ''):
        print(my_str(item), 'is not empty')
        # �ּ�ó���� �ڸ�
    else:
        print(my_str(item), 'is empty')
    print("p1_output =",p1_output)
    print()
    i += 1
    
# 1. p1_output.add(item)
# 2. p1_output.append(item)    
# 3. p1_output.remove(item)
# 4. p1_output.pop(i)    
# 5. p1_output.insert(0, item)    

# ����:

    
    
# ���� 4:
# �Ű����� x�� ���ڿ��� ��ȯ���� ��, ���ڿ��� ���� ��ŭ�� �ش��ϴ�
# ���� ���ڿ��� ��ȯ�ϴ� space_same_len(x) �Լ����� 
# �ּ�ó���� �ڸ��� �� ������ �ڵ带 ���ÿ�

def space_same_len(x):
    return ' ' # �ּ�ó���� �ڸ�

# 1. * str(x)
# 2. ** len(str(x))
# 3. * len(str(x))
# 4. + len(str(x))
# 5. + str(x)

# ����: 




# ���� 5:
# �Ű����� x�� ���ڿ��� ��ȯ���� ��, ���ڿ��� ���� ��ŭ�� �ش��ϴ�
# ���ڿ��� ��ȯ�ϴ� space_same_len(x) �Լ����� ���ڿ��� ��� ���ڰ�
# ^ �̰�, ������ ���ڴ� �������� �ϱ� ���ؼ�
# �ּ�ó���� �ڸ��� �� ������ �ڵ带 ���ÿ�

def mark_middle(x):
    num_left_spaces = len(str(x)) // 2 - 1
    num_right_spaces = len(str(x)) // 2 + len(str(x)) % 2
    return ' ' # �ּ�ó���� �ڸ�

# 1. + '^' * num_right_spaces
# 2. + '^'
# 3. * len(str(x)) + '^' + ' '
# 4. + '^' + ' ' * num_right_spaces
# 5. * num_left_spaces + '^' + ' ' * num_right_spaces

# ����:






# ���� 6:
# ����Ʈ my_list�� ���ڿ��� ��ȯ�� �Ͱ� ���� ������ ���ڿ��� ��ȯ�ϴµ�
# �Ű����� index�� �ε����� �׸��� ��� ��ġ�� Ư���� ���ڰ� ǥ�õǰ�
# ������ ���ڵ��� ��� ������ �ǰ� �ϴ� mark_index_of_list �Լ� �ڵ忡��
# �ּ� ó���� �ڸ��� �� ������ �ڵ带 ��� ���ÿ�.   

def mark_index_of_list(my_list, index):
    space = ' '
    ret = space
    for item in my_list[:index]:
        ret += space_same_len(item) # �ּ�ó���� �ڸ�
    return ret + mark_middle(my_list[index]) + space*2

# 1. + space*1
# 2. + space*2
# 3. + space*3
# 4. + space*4
# 5. + space*5

# ����:
        




# ���� 7:
# ����Ʈ p1_list���� ����ִ� Ʃ��, ����ִ� ����Ʈ, ����ִ� ���ڿ���
# ������ ����Ʈ�� p1_output�� �����ϴ� ���� �ڵ忡��
# �ּ� ó���� �ڸ��� �� ������ �ڵ带 ��� ���ÿ�.    

p1_output = p1_list.copy()
print("\n"*5 + str(p1_output) + '\n')
for i in range(len(p1_output)-1, -1, -1):
    item = p1_output[i]
    if item not in ((), [], ''):
        pass
    else:
        print(mark_index_of_list(p1_output,i))
        print(my_str(item), 'is empty')
        # �ּ�ó���� �ڸ�
        print("\n"*2)
        print(p1_output)
        print()
    
# 1. p1_output.append(item)
# 2. p1_output.insert(i, item)
# 3. p1_output.remove(item)        
# 4. p1_output.pop(i)
# 5. p1_output.add(item)

# ����:




# ���� 8: 
# ����Ʈ���� ���� ū �׸��� ���� ���������� �̵��ϴ� ���� �ڵ忡��
# �ּ�ó���� �ڸ��� �� ������ �ڵ带 ��� ���ÿ�       

p2_list = [5, 6, 3, 9, 2, 12, 3, 8, 7]
index_end = 0 # �ּ� ó���� �ڸ�
for i in range(0, index_end):
    if p2_list[i] > p2_list[i+1]:
        p2_list[i], p2_list[i+1] = p2_list[i+1], p2_list[i]
    print(p2_list)

print()
    
# 1. + len(p2_list)
# 2. + 0
# 3. + len(p2_list) - 1
# 4. + 1
# 5. + len(p2_list) + 1 

# ����:
 
 

# ���� 9: 
# ����Ʈ���� ���� ū �׸��� ���� ���������� �ݺ������� �̵��ؼ� 
# ����Ʈ�� ��� �׸��� ���� ������ ū ������ ������� �迭�Ϸ��� �� ��    
# �ּ�ó���� �ڸ��� �� ������ �ڵ带 ��� ���ÿ�       
   

for j in range(0, len(p2_list) - 1):
    end_point = 0 # �ּ� ó���� �ڸ�
    for i in range(0, end_point):
        if p2_list[i] > p2_list[i+1]:
            p2_list[i], p2_list[i+1] = p2_list[i+1], p2_list[i]
    print(p2_list)

print()
        

# 1. + len(p2_list)
# 2. + j
# 3. + len(p2_list) - 1
# 4. + 0
# 5. + len(p2_list) + 1 

# ����:
 




# ���� 9: 
# ����Ʈ���� ���� ū �׸��� ���� ���������� �ݺ������� �̵��ؼ� 
# ����Ʈ�� ��� �׸��� ���� ������ ū ������ ������� �迭�Ϸ��� �� ��
# �ݺ� �߰��߰��� ���ĵ� �κа� ���ĵ��� ���� �κ��� �и��ؼ� ����ϱ�����
# �ּ�ó���� �ڸ��� �� ������ �ڵ带 ��� ���ÿ�       

p3_list = [5, 6, 31, 9, 2, 12, 3, 8, 7]
for j in range(len(p3_list) - 1, 0, -1):
    for i in range(0, j):
        if p3_list[i] > p3_list[i+1]:
            p3_list[i], p3_list[i+1] = p3_list[i+1], p3_list[i]
    # �ּ� ó���� �ڸ�
print(p3_list)
print()

# 1. print(str(p3_list[:j])+',', p3_list[j:])
# 2. print(p3_list[0:j])
# 3. print(p3_list[j:])
# 4. print(p3_list[:])
# 5. print(p3_list[0:j], p3_list[j:-1])

# ����:





# ���� 10: 
# ���ڿ��� ������ �Ųٷ� �ص� �Ȱ����� Ȯ���ϴ� is_palindrome �Լ�����
# ����� ó������ �������� �� �� �ּ�ó���� �ڸ��� �˸´� �ڵ带 ���ÿ�.

p4_tuple = (4, 5, 2, 3, 8, 1, 9, 0)
for i in range(len(p4_tuple), 0, -1):
    print(p4_tuple[0:i])

def is_palindrome(x):
    print(x)
    l = 0
    r = len(x) - 1
    while (l < r):
        while(x[l] != ' '):
            l += 1
        while(x[r] != ' '):
            r -= 1
        if x[l] != x[r]:
            return False
        else:
            _ = 0
            # �ּ�ó���� �ڸ�
        
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




# ���� 11.
# p6_str�� iĭ �������� ȸ�����Ѽ� ����Ͻÿ�

p6_str = "ABCDEFGHIJKLMNOPQURSTUVWXYZ"

for i in range(0, len(p6_str)):
    _ = i
    #�ڵ带 �Է��� ��ġ



# ���� 12.
# p7_dst_str�� p7_src_str���� ��ĭ �������� ȸ�����Ѽ� ���Ͻÿ�
    
p7_src_str = "ABCDEFGHIJKLMNOPQURSTUVWXYZ"
p7_dst_str = p7_src_str # �ڵ带 �Է��� ��ġ

# ����:



# ���� 13
# a�� src_str���� �ε����� index �Լ��� ���� �� dst_str�� �ش� �ε��� ���ڿ���
# ��ȯ�ϴ� ciper(a) �Լ����� �ּ�ó���� �κп� �� �ڵ带 ���ÿ�.

def ciper(a):
    return p7_dst_str # �ּ� ó���� �κ�

print(p7_src_str.index('A'), ciper('A'))
print(p7_src_str.index('B'), ciper('B'))

# ����: 



# ���� 14
# �Է¹��� ���ڿ��� ���ؼ� ��� ���ڸ� ��ȣȭ�ϴ� ciper_all�Լ�����
# �ּ� ó���� �κп� ������ �ڵ带 ���ÿ�

def ciper_all(decoded_str):
    # �ּ�ó���� �κ�
    for a in decoded_str:
        if a in p7_src_str:
            encoded_str += ciper(a)
        else:
            encoded_str += a
    return encoded_str

p7_my_str = "ATTACK TONIGHT!"
print(ciper_all(p7_my_str))

# ����: 



# ���� 15

p7�� ���� p8_src_str���� ciper(a), ciper_all(decoded_str)�� �����Ͻÿ�
p8_src_str = "ABCDEFGHIJKLMNOPQURSTUVWXYZabcdefghijklmnopqrstuvwxyz"
p8_dst_str = p8_src_str[3:] + p8_src_str[:3]

def ciper(a):
    _ = a

def ciper_all(decoded_str):
    _ = decoded_str

p8_my_str = "Veni, vidi, vici."
print(ciper_all(p8_my_str))



# ���� 16. 
# my_string���� ��� ���鹮�ڸ� ������ ���ڿ��� ��ȯ�ϴ� 
# remove_space(my_string)�� �����Ͻÿ�

def remove_space(my_string):
    ret = ''
    return ret



# ���� 17. 
# my_string���� index�� ���� �ϳ��� �������� ������� ȸ���� 
# ���� �� ���̸� ���ϰ�, ȸ�� ���ڿ�, ȸ���� ���̸� ��ȯ�Ͻÿ� 

def longest_odd_palindromic_from_root(my_string, index):
    i = 1    
    ret = my_string
    return ret, i



# ���� 18. 
# my_string���� index�� index+1�� ���� �ϳ��� �������� ������� ȸ���� 
# ���� �� ���̸� ���ϰ�, ȸ�� ���ڿ�, ȸ���� ���̸� ��ȯ�Ͻÿ� 

def longest_even_palindromic_from_root(my_string, index):
    i = 1
    ret = my_string
    return ret, i



# ���� 19. 
# p9_my_str ������ ���� �� ȸ���� ã�Ƽ� ����Ͻÿ�

p9_my_str = "ATTACK"
print("longest palindromic string")
   

# ���� 20-1
# ���� �����Ϳ� �ʵ����� �޾Ƽ� �ش� ���ڿ��� ����Ͻÿ�
def my_format_int(int_data, width = 0):
    ret = ''
    return ret

# ���� 20-2
# �Ǽ� �����Ϳ� �ʵ����� ���е��� �޾Ƽ� �ش� ���ڿ��� ����Ͻÿ�
def my_format_float(float_data, width = 0, precision = 6):
    ret = ''
    return ret
    