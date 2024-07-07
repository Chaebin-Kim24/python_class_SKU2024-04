
'''
        파이썬 프로그래밍(EN1004-04) / 프로그래밍언어기초및실습(EE1201-04)
        중간고사                          학번:
                                          이름:
'''


# 문제 1:
# item을 문자열로 변환해서 반환해주는 my_str(item) 코드에서
# 주석 처리된 자리에 들어갈 코드로 알맞는 항목을 모두 고르시오

def my_str(item):
    if type(item) == str:
        return "'" + item + "'"
    else:
        return # 주석 처리된 자리

# 1. str(item)
# 2. item
# 3. 'item'
# 4. string(item)
# 5. item.string()


print("문제 1.")


# 보기 1. 
def my_str_1(item):
    if type(item) == str:
        return "'" + item + "'"
    else:
        return str(item)
print("보기 1:", my_str_1([]), type(my_str_1([])))
# 출력:
# 보기 1: [] <class 'str'>        (정답)


# 보기 2. 
def my_str_2(item):
    if type(item) == str:
        return "'" + item + "'"
    else:
        return item
print("보기 2:", my_str_2([]), type(my_str_2([])))
# 출력:
# 보기 2: [] <class 'list'>       (오답)


# 보기 3. 
def my_str_3(item):
    if type(item) == str:
        return "'" + item + "'"
    else:
        return 'item'
print("보기 3:", my_str_3([]), type(my_str_3([])))
# 출력:
# 보기 3: item <class 'str'>      (오답)


# 보기 4. 
def my_str_4(item):
    if type(item) == str:
        return "'" + item + "'"
    else:
        return string(item)
# print("보기 4:", my_str_4([]), type(my_str_4([])))  #string 이름 없음 에러 
# 출력:
# 에러 발생                       (오답)


# 보기 5. 
def my_str_5(item):
    if type(item) == str:
        return "'" + item + "'"
    else:
        return item.string()
# print("보기 5:", my_str_5([]), type(my_str_5([])))  #string 속성 없음 에러 
# 출력:
# 에러 발생                       (오답)


# 정답: 1
my_str = my_str_1



# 문제 2:
# 리스트 my_list를 문자열로 변환해서 반환해주는 my_str(item) 코드에서
# index에 해당하는 항목을 출력하기 전에 지정된 문자열을 앞에 붙여서
# 출력하려고 할 때 주석 처리된 자리에 들어갈 적절한 코드를 모두 고르시오.   
print("문제 2.")

def my_marked_str_of_list(my_list, index):
    mark_char = '#'
    ret = '['
    for i in range(0, index):
        ret += my_str(my_list[i]) + ', '

    if index == len(my_list) - 1:
        return ret + mark_char + my_str(my_list[index]) + ']' 
    else:
        # 주석 처리된 자리
        for i in range(index, len(my_list)-1):
            ret += my_str(my_list[i]) + ', '
        return ret + my_str(my_list[-1]) + ']'

# 1. ret += mark_char
# 2. ret = ret + mark_char + my_str(my_list[index]) + ', '
# 3. ret += my_str(my_list[index]) + ', '
# 4. i = 0
# 5. i = index 


# 보기 1. 
def my_marked_str_of_list_1(my_list, index):
    mark_char = '#'
    ret = '['
    for i in range(0, index):
        ret += my_str(my_list[i]) + ', '

    if index == len(my_list) - 1:
        return ret + mark_char + my_str(my_list[index]) + ']' 
    else:
        ret += mark_char
        for i in range(index, len(my_list)-1):
            ret += my_str(my_list[i]) + ', '
        return ret + my_str(my_list[-1]) + ']'

print("보기 1:", my_marked_str_of_list_1([0,1,2,3,4,5], 2))
# 출력:
# 보기 1: [0, 1, #2, 3, 4, 5]       (정답)


# 보기 2. 
def my_marked_str_of_list_2(my_list, index):
    mark_char = '#'
    ret = '['
    for i in range(0, index):
        ret += my_str(my_list[i]) + ', '

    if index == len(my_list) - 1:
        return ret + mark_char + my_str(my_list[index]) + ']' 
    else:
        ret = ret + mark_char + my_str(my_list[index]) + ', '
        for i in range(index, len(my_list)-1):
            ret += my_str(my_list[i]) + ', '
        return ret + my_str(my_list[-1]) + ']'

print("보기 2:", my_marked_str_of_list_2([0,1,2,3,4,5], 2))
# 출력:
# 보기 2: [0, 1, #2, 2, 3, 4, 5]       (오답)



# 보기 3. 
def my_marked_str_of_list_3(my_list, index):
    mark_char = '#'
    ret = '['
    for i in range(0, index):
        ret += my_str(my_list[i]) + ', '

    if index == len(my_list) - 1:
        return ret + mark_char + my_str(my_list[index]) + ']' 
    else:
        ret += my_str(my_list[index]) + ', '
        for i in range(index, len(my_list)-1):
            ret += my_str(my_list[i]) + ', '
        return ret + my_str(my_list[-1]) + ']'

print("보기 3:", my_marked_str_of_list_3([0,1,2,3,4,5], 2))
# 출력:
# 보기 3: [0, 1, 2, 2, 3, 4, 5]       (오답)



# 보기 4. 
def my_marked_str_of_list_4(my_list, index):
    mark_char = '#'
    ret = '['
    for i in range(0, index):
        ret += my_str(my_list[i]) + ', '

    if index == len(my_list) - 1:
        return ret + mark_char + my_str(my_list[index]) + ']' 
    else:
        i = 0
        for i in range(index, len(my_list)-1):
            ret += my_str(my_list[i]) + ', '
        return ret + my_str(my_list[-1]) + ']'

print("보기 4:", my_marked_str_of_list_4([0,1,2,3,4,5], 2))
# 출력:
# 보기 4: [0, 1, 2, 3, 4, 5]       (오답)



# 보기 5. 
def my_marked_str_of_list_5(my_list, index):
    mark_char = '#'
    ret = '['
    for i in range(0, index):
        ret += my_str(my_list[i]) + ', '

    if index == len(my_list) - 1:
        return ret + mark_char + my_str(my_list[index]) + ']' 
    else:
        i = 0
        for i in range(index, len(my_list)-1):
            ret += my_str(my_list[i]) + ', '
        return ret + my_str(my_list[-1]) + ']'

print("보기 5:", my_marked_str_of_list_5([0,1,2,3,4,5], 2))
# 출력:
# 보기 5: [0, 1, 2, 3, 4, 5]       (오답)


# 정답: 1
my_marked_str_of_list = my_marked_str_of_list_1





# 문제 3:
# 리스트 p1_list에서 비어있는 튜플, 비어있는 리스트, 비어있는 문자열을
# 제거한 리스트를 p1_output에 저장하는 다음 코드에서
# 주석 처리된 자리에 들어갈 적절한 코드를 모두 고르시오.    
print("문제 3.")

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
    print("p1_output =",p1_output)
    print()
    i += 1

# 보기 
# 1. p1_output.add(item)
# 2. p1_output.append(item)    
# 3. p1_output.remove(item)
# 4. p1_output.pop(i)    
# 5. p1_output.insert(0, item)    


# 보기 1.
print("보기 1:")
p1_output = []
i = 0
for item in p1_list:
    print(my_marked_str_of_list(p1_list, i))
    if item not in ((), [], ''):
        print(my_str(item), 'is not empty')
        # p1_output.add(item)   # 에러: 리스트에 add가 없음 
    else:
        print(my_str(item), 'is empty')
    print("p1_output =",p1_output)
    print()
    i += 1

# 출력:
# 에러: 리스트에 add가 없음      (오답)


# 보기 2.
print("보기 2:")
p1_output = []
i = 0
for item in p1_list:
    print(my_marked_str_of_list(p1_list, i))
    if item not in ((), [], ''):
        print(my_str(item), 'is not empty')
        p1_output.append(item)    
    else:
        print(my_str(item), 'is empty')
    print("p1_output =",p1_output)
    print()
    i += 1

# 출력:
# 보기 2:
# [#(), 1, (), (), (1,), ('a',), ('a', 'b'), ((),), ('a', 'b'), '']
# () is empty
# p1_output = []
#
# [(), #1, (), (), (1,), ('a',), ('a', 'b'), ((),), ('a', 'b'), '']
# 1 is not empty
# p1_output = [1]
#
# [(), 1, #(), (), (1,), ('a',), ('a', 'b'), ((),), ('a', 'b'), '']
# () is empty
# p1_output = [1]
#
# [(), 1, (), #(), (1,), ('a',), ('a', 'b'), ((),), ('a', 'b'), '']
# () is empty
# p1_output = [1]
#
# [(), 1, (), (), #(1,), ('a',), ('a', 'b'), ((),), ('a', 'b'), '']
# (1,) is not empty
# p1_output = [1, (1,)]
# 
# [(), 1, (), (), (1,), #('a',), ('a', 'b'), ((),), ('a', 'b'), '']
# ('a',) is not empty
# p1_output = [1, (1,), ('a',)]
#
# [(), 1, (), (), (1,), ('a',), #('a', 'b'), ((),), ('a', 'b'), '']
# ('a', 'b') is not empty
# p1_output = [1, (1,), ('a',), ('a', 'b')]
# 
# [(), 1, (), (), (1,), ('a',), ('a', 'b'), #((),), ('a', 'b'), '']
# ((),) is not empty
# p1_output = [1, (1,), ('a',), ('a', 'b'), ((),)]
#
# [(), 1, (), (), (1,), ('a',), ('a', 'b'), ((),), #('a', 'b'), '']
# ('a', 'b') is not empty
# p1_output = [1, (1,), ('a',), ('a', 'b'), ((),), ('a', 'b')]
# 
# [(), 1, (), (), (1,), ('a',), ('a', 'b'), ((),), ('a', 'b'), #'']
# '' is empty
# p1_output = [1, (1,), ('a',), ('a', 'b'), ((),), ('a', 'b')]      (정답)



# 보기 3.
print("보기 3:")
p1_output = []
i = 0
for item in p1_list:
    print(my_marked_str_of_list(p1_list, i))
    if item not in ((), [], ''):
        print(my_str(item), 'is not empty')
        # p1_output.remove(item)    # 에러: item이 리스트에 없음 
    else:
        print(my_str(item), 'is empty')
    print("p1_output =",p1_output)
    print()
    i += 1

# 출력:
# 에러: item이 리스트에 없음         (오답)



# 보기 4.
print("보기 4:")
p1_output = []
i = 0
for item in p1_list:
    print(my_marked_str_of_list(p1_list, i))
    if item not in ((), [], ''):
        print(my_str(item), 'is not empty')
        # p1_output.pop(i)    # 에러: 비어있는 리스트에서의 pop 
    else:
        print(my_str(item), 'is empty')
    print("p1_output =",p1_output)
    print()
    i += 1

# 출력:
# 에러: 비어있는 리스트에서의 pop       (오답)



# 보기 5.
print("보기 5:")
p1_output = []
i = 0
for item in p1_list:
    print(my_marked_str_of_list(p1_list, i))
    if item not in ((), [], ''):
        print(my_str(item), 'is not empty')
        p1_output.insert(0, item)    
    else:
        print(my_str(item), 'is empty')
    print("p1_output =",p1_output)
    print()
    i += 1

# 출력:
# 보기 5:
# [#(), 1, (), (), (1,), ('a',), ('a', 'b'), ((),), ('a', 'b'), '']
# () is empty
# p1_output = []
#
# [(), #1, (), (), (1,), ('a',), ('a', 'b'), ((),), ('a', 'b'), '']
# 1 is not empty
# p1_output = [1]
#
# [(), 1, #(), (), (1,), ('a',), ('a', 'b'), ((),), ('a', 'b'), '']
# () is empty
# p1_output = [1]
#
# [(), 1, (), #(), (1,), ('a',), ('a', 'b'), ((),), ('a', 'b'), '']
# () is empty
# p1_output = [1]
#
# [(), 1, (), (), #(1,), ('a',), ('a', 'b'), ((),), ('a', 'b'), '']
# (1,) is not empty
# p1_output = [(1,), 1]
#
# [(), 1, (), (), (1,), #('a',), ('a', 'b'), ((),), ('a', 'b'), '']
# ('a',) is not empty
# p1_output = [('a',), (1,), 1]
#
# [(), 1, (), (), (1,), ('a',), #('a', 'b'), ((),), ('a', 'b'), '']
# ('a', 'b') is not empty
# p1_output = [('a', 'b'), ('a',), (1,), 1]
# 
# [(), 1, (), (), (1,), ('a',), ('a', 'b'), #((),), ('a', 'b'), '']
# ((),) is not empty
# p1_output = [((),), ('a', 'b'), ('a',), (1,), 1]
#
# [(), 1, (), (), (1,), ('a',), ('a', 'b'), ((),), #('a', 'b'), '']
# ('a', 'b') is not empty
# p1_output = [('a', 'b'), ((),), ('a', 'b'), ('a',), (1,), 1]
#
# [(), 1, (), (), (1,), ('a',), ('a', 'b'), ((),), ('a', 'b'), #'']
# '' is empty
# p1_output = [('a', 'b'), ((),), ('a', 'b'), ('a',), (1,), 1]      (정답)



# 정답: 2, 5


    
    
# 문제 4:
# 매개변수 x를 문자열로 변환했을 때, 문자열의 길이 만큼에 해당하는
# 공백 문자열을 반환하는 space_same_len(x) 함수에서 
# 주석처리한 자리에 들어갈 적절한 코드를 고르시오

def space_same_len(x):
    return ' ' # 주석처리한 자리

# 1. * str(x)
# 2. ** len(str(x))
# 3. * len(str(x))
# 4. + len(str(x))
# 5. + str(x)


print("문제 4.")

# 보기 1.
def space_same_len_1(x):
    return ' ' * str(x)

# print("보기 1:" + space_same_len_1("space") + "space")  # 에러

# 출력.
# 에러: 문자열과 문자열을 곱할 수 없음     (오답)


# 보기 2.
def space_same_len_2(x):
    return ' ' ** len(str(x))

# print("보기 2:" + space_same_len_2("space") + "space")  # 에

# 출력.
# 에러: 문자열과 숫자를 거듭제곱할 수 없음     (오답)


# 보기 3.
def space_same_len_3(x):
    return ' ' * len(str(x))

print("보기 3:" + space_same_len_3("space") + "space")

# 출력.
# 보기 3:     space       (정답)


# 보기 4.
def space_same_len_4(x):
    return ' ' + len(str(x))

# print("보기 4:" + space_same_len_4("space") + "space")      # 에러 

# 출력.
# 에러: 숫자를 문자열에 이어붙일 수 없음        (오답)


# 보기 5.
def space_same_len_5(x):
    return ' ' + str(x)

print("보기 5:" + space_same_len_5("space") + "space")

# 출력.
# 보기 5: spacespace      (오답)



# 정답: 3
space_same_len = space_same_len_3




# 문제 5:
# 매개변수 x를 문자열로 변환했을 때, 문자열의 길이 만큼에 해당하는
# 문자열을 반환하는 space_same_len(x) 함수에서 문자열의 가운데 문자가
# ^ 이고, 나머지 문자는 공백으로 하기 위해서
# 주석처리한 자리에 들어갈 적절한 코드를 고르시오

def mark_middle(x):
    num_left_spaces = len(str(x)) // 2 - 1
    num_right_spaces = len(str(x)) // 2 + len(str(x)) % 2
    return ' ' # 주석처리된 자리

# 1. + '^' * num_right_spaces
# 2. + '^'
# 3. * len(str(x)) + '^' + ' '
# 4. + '^' + ' ' * num_right_spaces
# 5. * num_left_spaces + '^' + ' ' * num_right_spaces

print()
print("문제 5.")

# 보기 1.
def mark_middle_1(x):
    num_left_spaces = len(str(x)) // 2 - 1
    num_right_spaces = len(str(x)) // 2 + len(str(x)) % 2
    return ' '  + '^' * num_right_spaces
print("보기 1:" + mark_middle_1("long_spaces") + "space")

# 출력:
# 보기 1: ^^^^^^space     (오답)


# 보기 2.
def mark_middle_2(x):
    num_left_spaces = len(str(x)) // 2 - 1
    num_right_spaces = len(str(x)) // 2 + len(str(x)) % 2
    return ' '  + '^'
print("보기 2:" + mark_middle_2("long_spaces") + "space")

# 출력:
# 보기 2: ^space      (오답)


# 보기 3.
def mark_middle_3(x):
    num_left_spaces = len(str(x)) // 2 - 1
    num_right_spaces = len(str(x)) // 2 + len(str(x)) % 2
    return ' ' * len(str(x)) + '^' + ' '
print("보기 3:" + mark_middle_3("long_spaces") + "space")

# 출력:
# 보기 3:           ^ space       (오답)


# 보기 4.
def mark_middle_4(x):
    num_left_spaces = len(str(x)) // 2 - 1
    num_right_spaces = len(str(x)) // 2 + len(str(x)) % 2
    return ' ' + '^' + ' ' * num_right_spaces

print("보기 4:" + mark_middle_4("long_spaces") + "space")

# 출력:
# 보기 4: ^      space        (오답)


# 보기 5.
def mark_middle_5(x):
    num_left_spaces = len(str(x)) // 2 - 1
    num_right_spaces = len(str(x)) // 2 + len(str(x)) % 2
    return ' ' * num_left_spaces + '^' + ' ' * num_right_spaces

print("보기 5:" + mark_middle_5("long_spaces") + "space")

# 출력:
# 보기 5:    ^      space     (정답)



# 정답: 5
mark_middle = mark_middle_5





# 문제 6:
# 리스트 my_list를 문자열로 반환한 것과 같은 길이의 문자열을 변환하는데
# 매개변수 index가 인덱스인 항목의 가운데 위치에 특별한 문자가 표시되고
# 나머지 문자들은 모두 공백이 되게 하는 mark_index_of_list 함수 코드에서
# 주석 처리된 자리에 들어갈 적절한 코드를 모두 고르시오.   

def mark_index_of_list(my_list, index):
    space = ' '
    ret = space
    for item in my_list[:index]:
        ret += space_same_len(item) # 주석처리된 자리
    return ret + mark_middle(my_list[index]) + space*2

# 1. + space*1
# 2. + space*2
# 3. + space*3
# 4. + space*4
# 5. + space*5


print()
print("문제 6")


# 보기 1.
def mark_index_of_list_1(my_list, index):
    space = ' '
    ret = space
    for item in my_list[:index]:
        ret += space_same_len(item) + space*1
    return ret + mark_middle(my_list[index]) + space*2

print("보기 1.")
print([1, 2, 3])
print(mark_index_of_list_1([1, 2, 3], 2))

# 출력:
# 보기 1.
# [1, 2, 3]
#      ^        (오답)



# 보기 2.
def mark_index_of_list_2(my_list, index):
    space = ' '
    ret = space
    for item in my_list[:index]:
        ret += space_same_len(item) + space*2
    return ret + mark_middle(my_list[index]) + space*2

print("보기 2.")
print([1, 2, 3])
print(mark_index_of_list_2([1, 2, 3], 2))

# 출력:
# 보기 2.
# [1, 2, 3]
#        ^      (정답)


# 보기 3.
def mark_index_of_list_3(my_list, index):
    space = ' '
    ret = space
    for item in my_list[:index]:
        ret += space_same_len(item) + space*3
    return ret + mark_middle(my_list[index]) + space*2

print("보기 3.")
print([1, 2, 3])
print(mark_index_of_list_3([1, 2, 3], 2))

# 출력:
# 보기 3.
# [1, 2, 3]
#          ^        (오답)



# 보기 4.
def mark_index_of_list_4(my_list, index):
    space = ' '
    ret = space
    for item in my_list[:index]:
        ret += space_same_len(item) + space*4
    return ret + mark_middle(my_list[index]) + space*2

print("보기 4.")
print([1, 2, 3])
print(mark_index_of_list_4([1, 2, 3], 2))

# 출력:
# 보기 4.
# [1, 2, 3]
#            ^          (오답)



# 보기 5.
def mark_index_of_list_5(my_list, index):
    space = ' '
    ret = space
    for item in my_list[:index]:
        ret += space_same_len(item) + space*5
    return ret + mark_middle(my_list[index]) + space*2

print("보기 5.")
print([1, 2, 3])
print(mark_index_of_list_5([1, 2, 3], 2))

# 출력:
# 보기 5.
# [1, 2, 3]
#              ^        (오답)




# 정답: 2
mark_index_of_list = mark_index_of_list_2        




# 문제 7:
# 리스트 p1_list에서 비어있는 튜플, 비어있는 리스트, 비어있는 문자열을
# 제거한 리스트를 p1_output에 저장하는 다음 코드에서
# 주석 처리된 자리에 들어갈 적절한 코드를 모두 고르시오.    

p1_output = p1_list.copy()
print("\n"*5 + str(p1_output) + '\n')
for i in range(len(p1_output)-1, -1, -1):
    item = p1_output[i]
    if item not in ((), [], ''):
        pass
    else:
        print(mark_index_of_list(p1_output,i))
        print(my_str(item), 'is empty')
        # 주석처리된 자리
        print("\n"*2)
        print(p1_output)
        print()
    
# 1. p1_output.append(item)
# 2. p1_output.insert(i, item)
# 3. p1_output.remove(item)        
# 4. p1_output.pop(i)
# 5. p1_output.add(item)

print()
print("문제 7")


# 보기 1.
print("보기 1:")

p1_output = p1_list.copy()
print("\n"*5 + str(p1_output) + '\n')
for i in range(len(p1_output)-1, -1, -1):
    item = p1_output[i]
    if item not in ((), [], ''):
        pass
    else:
        print(mark_index_of_list(p1_output,i))
        print(my_str(item), 'is empty')
        p1_output.append(item)
        print("\n"*2)
        print(p1_output)
        print()

# 출력:
# 보기 1:
# 
# 
# 
# 
# 
# [(), 1, (), (), (1,), ('a',), ('a', 'b'), ((),), ('a', 'b'), '']
# 
#                                                              ^  
# '' is empty
# 
# 
# 
# [(), 1, (), (), (1,), ('a',), ('a', 'b'), ((),), ('a', 'b'), '', '']
# 
#             ^   
# () is empty
# 
# 
# 
# [(), 1, (), (), (1,), ('a',), ('a', 'b'), ((),), ('a', 'b'), '', '', ()]
# 
#         ^   
# () is empty
# 
# 
# 
# [(), 1, (), (), (1,), ('a',), ('a', 'b'), ((),), ('a', 'b'), '', '', (), ()]
# 
#  ^   
# () is empty
# 
# 
# 
# [(), 1, (), (), (1,), ('a',), ('a', 'b'), ((),), ('a', 'b'), '', '', (), (), ()]
# (오답)


# 보기 2.
print("보기 2:")

p1_output = p1_list.copy()
print("\n"*5 + str(p1_output) + '\n')
for i in range(len(p1_output)-1, -1, -1):
    item = p1_output[i]
    if item not in ((), [], ''):
        pass
    else:
        print(mark_index_of_list(p1_output,i))
        print(my_str(item), 'is empty')
        p1_output.insert(i, item)
        print("\n"*2)
        print(p1_output)
        print()

# 출력:
# 보기 2:
# 
# 
# 
# 
# 
# [(), 1, (), (), (1,), ('a',), ('a', 'b'), ((),), ('a', 'b'), '']
# 
#                                                              ^  
# '' is empty
# 
# 
# 
# [(), 1, (), (), (1,), ('a',), ('a', 'b'), ((),), ('a', 'b'), '', '']
# 
#             ^   
# () is empty
# 
# 
# 
# [(), 1, (), (), (), (1,), ('a',), ('a', 'b'), ((),), ('a', 'b'), '', '']
# 
#         ^   
# () is empty
# 
# 
# 
# [(), 1, (), (), (), (), (1,), ('a',), ('a', 'b'), ((),), ('a', 'b'), '', '']
# 
#  ^   
# () is empty
# 
# 
# 
# [(), (), 1, (), (), (), (), (1,), ('a',), ('a', 'b'), ((),), ('a', 'b'), '', '']
# (오답)



# 보기 3.
print("보기 3:")

p1_output = p1_list.copy()
print("\n"*5 + str(p1_output) + '\n')
for i in range(len(p1_output)-1, -1, -1):
    item = p1_output[i]
    if item not in ((), [], ''):
        pass
    else:
        print(mark_index_of_list(p1_output,i))
        print(my_str(item), 'is empty')
        p1_output.remove(item)        
        print("\n"*2)
        print(p1_output)
        print()

# 출력:
# 보기 3:
#
#
#
#
#
# [(), 1, (), (), (1,), ('a',), ('a', 'b'), ((),), ('a', 'b'), '']
# 
#                                                              ^  
# '' is empty
# 
# 
# 
# [(), 1, (), (), (1,), ('a',), ('a', 'b'), ((),), ('a', 'b')]
# 
#             ^   
# () is empty
# 
# 
# 
# [1, (), (), (1,), ('a',), ('a', 'b'), ((),), ('a', 'b')]
# 
#         ^   
# () is empty
# 
# 
# 
# [1, (), (1,), ('a',), ('a', 'b'), ((),), ('a', 'b')]
# 
#     ^   
# () is empty
# 
# 
# 
# [1, (1,), ('a',), ('a', 'b'), ((),), ('a', 'b')]
# (정답) 



# 보기 4.
print("보기 4:")

p1_output = p1_list.copy()
print("\n"*5 + str(p1_output) + '\n')
for i in range(len(p1_output)-1, -1, -1):
    item = p1_output[i]
    if item not in ((), [], ''):
        pass
    else:
        print(mark_index_of_list(p1_output,i))
        print(my_str(item), 'is empty')
        p1_output.pop(i)
        print("\n"*2)
        print(p1_output)
        print()

# 출력:
# 보기 4:
# 
# 
# 
# 
# 
# [(), 1, (), (), (1,), ('a',), ('a', 'b'), ((),), ('a', 'b'), '']
#
#                                                             ^  
# '' is empty
# 
# 
# 
# [(), 1, (), (), (1,), ('a',), ('a', 'b'), ((),), ('a', 'b')]
# 
#             ^   
# () is empty
# 
# 
# 
# [(), 1, (), (1,), ('a',), ('a', 'b'), ((),), ('a', 'b')]
# 
#         ^   
# () is empty
# 
# 
# 
# [(), 1, (1,), ('a',), ('a', 'b'), ((),), ('a', 'b')]
# 
#  ^   
# () is empty
# 
# 
# 
# [1, (1,), ('a',), ('a', 'b'), ((),), ('a', 'b')]



# 보기 5.
print("보기 5:")

p1_output = p1_list.copy()
print("\n"*5 + str(p1_output) + '\n')
for i in range(len(p1_output)-1, -1, -1):
    item = p1_output[i]
    if item not in ((), [], ''):
        pass
    else:
        print(mark_index_of_list(p1_output,i))
        print(my_str(item), 'is empty')
        # p1_output.add(item)       # 에
        print("\n"*2)
        print(p1_output)
        print()

# 출력:
# 보기 5:
# 에러: 리스트는 add 속성이 없음
# (오답)


# 정답: 3, 4





# 문제 8: 
# 리스트에서 가장 큰 항목을 가장 오른쪽으로 이동하는 다음 코드에서
# 주석처리된 자리에 들어갈 적절한 코드를 모두 고르시오       

p2_list = [5, 6, 3, 9, 2, 12, 3, 8, 7]
index_end = 0 # 주석 처리된 자리
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

print()
print("문제 8.")


# 보기 1.
print("보기 1:")
p2_list = [5, 6, 3, 9, 2, 12, 3, 8, 7]
index_end = 0  # + len(p2_list)  # 에러 
for i in range(0, index_end):
    if p2_list[i] > p2_list[i+1]:
        p2_list[i], p2_list[i+1] = p2_list[i+1], p2_list[i]
    print(p2_list)

print()

# 출력:
# 보기 1:
# [5, 6, 3, 9, 2, 12, 3, 8, 7]
# [5, 3, 6, 9, 2, 12, 3, 8, 7]
# [5, 3, 6, 9, 2, 12, 3, 8, 7]
# [5, 3, 6, 2, 9, 12, 3, 8, 7]
# [5, 3, 6, 2, 9, 12, 3, 8, 7]
# [5, 3, 6, 2, 9, 3, 12, 8, 7]
# [5, 3, 6, 2, 9, 3, 8, 12, 7]
# [5, 3, 6, 2, 9, 3, 8, 7, 12]
# 인덱스 에러
# (오답)


# 보기 2.
print("보기 2:")
p2_list = [5, 6, 3, 9, 2, 12, 3, 8, 7]
index_end = 0 + 0
for i in range(0, index_end):
    if p2_list[i] > p2_list[i+1]:
        p2_list[i], p2_list[i+1] = p2_list[i+1], p2_list[i]
    print(p2_list)

print()

# 출력:
# 보기 2:
# (오답)


# 보기 3.
print("보기 3:")
p2_list = [5, 6, 3, 9, 2, 12, 3, 8, 7]
index_end = 0 + len(p2_list) - 1
for i in range(0, index_end):
    if p2_list[i] > p2_list[i+1]:
        p2_list[i], p2_list[i+1] = p2_list[i+1], p2_list[i]
    print(p2_list)

print()

# 출력:
# 보기 3:
# [5, 6, 3, 9, 2, 12, 3, 8, 7]
# [5, 3, 6, 9, 2, 12, 3, 8, 7]
# [5, 3, 6, 9, 2, 12, 3, 8, 7]
# [5, 3, 6, 2, 9, 12, 3, 8, 7]
# [5, 3, 6, 2, 9, 12, 3, 8, 7]
# [5, 3, 6, 2, 9, 3, 12, 8, 7]
# [5, 3, 6, 2, 9, 3, 8, 12, 7]
# [5, 3, 6, 2, 9, 3, 8, 7, 12]
# (정답) 


# 보기 4.
print("보기 4:")
p2_list = [5, 6, 3, 9, 2, 12, 3, 8, 7]
index_end = 0 + 1
for i in range(0, index_end):
    if p2_list[i] > p2_list[i+1]:
        p2_list[i], p2_list[i+1] = p2_list[i+1], p2_list[i]
    print(p2_list)

print()

# 출력:
# 보기 4:
# [5, 6, 3, 9, 2, 12, 3, 8, 7]
# (오답) 


# 보기 5.
print("보기 5:")
p2_list = [5, 6, 3, 9, 2, 12, 3, 8, 7]
index_end = 0 # + len(p2_list) + 1  # 에
for i in range(0, index_end):
    if p2_list[i] > p2_list[i+1]:
        p2_list[i], p2_list[i+1] = p2_list[i+1], p2_list[i]
    print(p2_list)

print()

# 출력:
# 보기 5:
# [5, 6, 3, 9, 2, 12, 3, 8, 7]
# [5, 3, 6, 9, 2, 12, 3, 8, 7]
# [5, 3, 6, 9, 2, 12, 3, 8, 7]
# [5, 3, 6, 2, 9, 12, 3, 8, 7]
# [5, 3, 6, 2, 9, 12, 3, 8, 7]
# [5, 3, 6, 2, 9, 3, 12, 8, 7]
# [5, 3, 6, 2, 9, 3, 8, 12, 7]
# [5, 3, 6, 2, 9, 3, 8, 7, 12]
# 인덱스 에러 
# (오답) 

# 정답: 3


 
 

# 문제 9: 
# 리스트에서 가장 큰 항목을 가장 오른쪽으로 반복적으로 이동해서 
# 리스트의 모든 항목을 작은 값부터 큰 값까지 순서대로 배열하려고 할 때    
# 주석처리된 자리에 들어갈 적절한 코드를 모두 고르시오       
   

for j in range(0, len(p2_list) - 1):
    end_point = 0 # 주석 처리된 자리
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


print()
print("문제 9")


p2_list_orig = p2_list.copy()

# 보기 1.
print("보기 1:")
p2_list = p2_list_orig.copy()
for j in range(0, len(p2_list) - 1):
    end_point = 0 # + len(p2_list)  # 에러 
    for i in range(0, end_point):
        if p2_list[i] > p2_list[i+1]:
            p2_list[i], p2_list[i+1] = p2_list[i+1], p2_list[i]
    print(p2_list)

print()

# 출력:
# 보기 1:
# 인덱스 에러 



# 보기 2.
print("보기 2:")
p2_list = p2_list_orig.copy()
for j in range(0, len(p2_list) - 1):
    end_point = 0 + j 
    for i in range(0, end_point):
        if p2_list[i] > p2_list[i+1]:
            p2_list[i], p2_list[i+1] = p2_list[i+1], p2_list[i]
    print(p2_list)

print()

# 출력:
# 보기 2:
# [5, 6, 3, 9, 2, 12, 3, 8, 7]
# [5, 6, 3, 9, 2, 12, 3, 8, 7]
# [5, 3, 6, 9, 2, 12, 3, 8, 7]
# [3, 5, 6, 9, 2, 12, 3, 8, 7]
# [3, 5, 6, 2, 9, 12, 3, 8, 7]
# [3, 5, 2, 6, 9, 12, 3, 8, 7]
# [3, 2, 5, 6, 9, 3, 12, 8, 7]
# [2, 3, 5, 6, 3, 9, 8, 12, 7]



# 보기 3.
print("보기 3:")
p2_list = p2_list_orig.copy()
for j in range(0, len(p2_list) - 1):
    end_point = 0 + len(p2_list) - 1 
    for i in range(0, end_point):
        if p2_list[i] > p2_list[i+1]:
            p2_list[i], p2_list[i+1] = p2_list[i+1], p2_list[i]
    print(p2_list)

print()

# 출력:
# 보기 3:
# [5, 3, 6, 2, 9, 3, 8, 7, 12]
# [3, 5, 2, 6, 3, 8, 7, 9, 12]
# [3, 2, 5, 3, 6, 7, 8, 9, 12]
# [2, 3, 3, 5, 6, 7, 8, 9, 12]
# [2, 3, 3, 5, 6, 7, 8, 9, 12]
# [2, 3, 3, 5, 6, 7, 8, 9, 12]
# [2, 3, 3, 5, 6, 7, 8, 9, 12]
# [2, 3, 3, 5, 6, 7, 8, 9, 12]




# 보기 4.
print("보기 4:")
p2_list = p2_list_orig.copy()
for j in range(0, len(p2_list) - 1):
    end_point = 0 + 0
    for i in range(0, end_point):
        if p2_list[i] > p2_list[i+1]:
            p2_list[i], p2_list[i+1] = p2_list[i+1], p2_list[i]
    print(p2_list)

print()

# 출력:
# 보기 4:
# [5, 6, 3, 9, 2, 12, 3, 8, 7]
# [5, 6, 3, 9, 2, 12, 3, 8, 7]
# [5, 6, 3, 9, 2, 12, 3, 8, 7]
# [5, 6, 3, 9, 2, 12, 3, 8, 7]
# [5, 6, 3, 9, 2, 12, 3, 8, 7]
# [5, 6, 3, 9, 2, 12, 3, 8, 7]
# [5, 6, 3, 9, 2, 12, 3, 8, 7]
# [5, 6, 3, 9, 2, 12, 3, 8, 7]



# 보기 5.
print("보기 5:")
p2_list = p2_list_orig.copy()
for j in range(0, len(p2_list) - 1):
    end_point = 0 # + len(p2_list) + 1  # 에
    for i in range(0, end_point):
        if p2_list[i] > p2_list[i+1]:
            p2_list[i], p2_list[i+1] = p2_list[i+1], p2_list[i]
    print(p2_list)

print()

# 출력:
# 보기 5:
# 인덱스 에러 



# 정답: 3
 





# 문제 9: 
# 리스트에서 가장 큰 항목을 가장 오른쪽으로 반복적으로 이동해서 
# 리스트의 모든 항목을 작은 값부터 큰 값까지 순서대로 배열하려고 할 때
# 반복 중간중간에 정렬된 부분과 정렬되지 않은 부분을 분리해서 출력하기위해
# 주석처리된 자리에 들어갈 적절한 코드를 모두 고르시오       

p3_list = [5, 6, 31, 9, 2, 12, 3, 8, 7]
for j in range(len(p3_list) - 1, 0, -1):
    for i in range(0, j):
        if p3_list[i] > p3_list[i+1]:
            p3_list[i], p3_list[i+1] = p3_list[i+1], p3_list[i]
    # 주석 처리된 자리
print(p3_list)
print()

# 1. print(str(p3_list[:j])+',', p3_list[j:])
# 2. print(p3_list[0:j])
# 3. print(p3_list[j:])
# 4. print(p3_list[:])
# 5. print(p3_list[0:j], p3_list[j:-1])



print("문제 9.")

# 보기 1:
print("보기 1:")

p3_list = [5, 6, 31, 9, 2, 12, 3, 8, 7]
for j in range(len(p3_list) - 1, 0, -1):
    for i in range(0, j):
        if p3_list[i] > p3_list[i+1]:
            p3_list[i], p3_list[i+1] = p3_list[i+1], p3_list[i]
    print(str(p3_list[:j])+',', p3_list[j:])
print(p3_list)
print()

# 출력:
# 보기 1:
# [5, 6, 9, 2, 12, 3, 8, 7], [31]
# [5, 6, 2, 9, 3, 8, 7], [12, 31]
# [5, 2, 6, 3, 8, 7], [9, 12, 31]
# [2, 5, 3, 6, 7], [8, 9, 12, 31]
# [2, 3, 5, 6], [7, 8, 9, 12, 31]
# [2, 3, 5], [6, 7, 8, 9, 12, 31]
# [2, 3], [5, 6, 7, 8, 9, 12, 31]
# [2], [3, 5, 6, 7, 8, 9, 12, 31]
# [2, 3, 5, 6, 7, 8, 9, 12, 31]



# 보기 2:
print("보기 2:")

p3_list = [5, 6, 31, 9, 2, 12, 3, 8, 7]
for j in range(len(p3_list) - 1, 0, -1):
    for i in range(0, j):
        if p3_list[i] > p3_list[i+1]:
            p3_list[i], p3_list[i+1] = p3_list[i+1], p3_list[i]
    print(p3_list[0:j])
print(p3_list)
print()

# 출력:
# 보기 2:
# [5, 6, 9, 2, 12, 3, 8, 7]
# [5, 6, 2, 9, 3, 8, 7]
# [5, 2, 6, 3, 8, 7]
# [2, 5, 3, 6, 7]
# [2, 3, 5, 6]
# [2, 3, 5]
# [2, 3]
# [2]
# [2, 3, 5, 6, 7, 8, 9, 12, 31]




# 보기 3:
print("보기 3:")

p3_list = [5, 6, 31, 9, 2, 12, 3, 8, 7]
for j in range(len(p3_list) - 1, 0, -1):
    for i in range(0, j):
        if p3_list[i] > p3_list[i+1]:
            p3_list[i], p3_list[i+1] = p3_list[i+1], p3_list[i]
    print(p3_list[j:])
print(p3_list)
print()

# 보기 3:
# [31]
# [12, 31]
# [9, 12, 31]
# [8, 9, 12, 31]
# [7, 8, 9, 12, 31]
# [6, 7, 8, 9, 12, 31]
# [5, 6, 7, 8, 9, 12, 31]
# [3, 5, 6, 7, 8, 9, 12, 31]
# [2, 3, 5, 6, 7, 8, 9, 12, 31]



# 보기 4:
print("보기 4:")

p3_list = [5, 6, 31, 9, 2, 12, 3, 8, 7]
for j in range(len(p3_list) - 1, 0, -1):
    for i in range(0, j):
        if p3_list[i] > p3_list[i+1]:
            p3_list[i], p3_list[i+1] = p3_list[i+1], p3_list[i]
    print(p3_list[:])
print(p3_list)
print()

# 보기 4:
# [5, 6, 9, 2, 12, 3, 8, 7, 31]
# [5, 6, 2, 9, 3, 8, 7, 12, 31]
# [5, 2, 6, 3, 8, 7, 9, 12, 31]
# [2, 5, 3, 6, 7, 8, 9, 12, 31]
# [2, 3, 5, 6, 7, 8, 9, 12, 31]
# [2, 3, 5, 6, 7, 8, 9, 12, 31]
# [2, 3, 5, 6, 7, 8, 9, 12, 31]
# [2, 3, 5, 6, 7, 8, 9, 12, 31]
# [2, 3, 5, 6, 7, 8, 9, 12, 31]




print("보기 5:")

p3_list = [5, 6, 31, 9, 2, 12, 3, 8, 7]
for j in range(len(p3_list) - 1, 0, -1):
    for i in range(0, j):
        if p3_list[i] > p3_list[i+1]:
            p3_list[i], p3_list[i+1] = p3_list[i+1], p3_list[i]
    print(p3_list[0:j], p3_list[j:-1])
print(p3_list)
print()

# 보기 5:
# [5, 6, 9, 2, 12, 3, 8, 7] []
# [5, 6, 2, 9, 3, 8, 7] [12]
# [5, 2, 6, 3, 8, 7] [9, 12]
# [2, 5, 3, 6, 7] [8, 9, 12]
# [2, 3, 5, 6] [7, 8, 9, 12]
# [2, 3, 5] [6, 7, 8, 9, 12]
# [2, 3] [5, 6, 7, 8, 9, 12]
# [2] [3, 5, 6, 7, 8, 9, 12]
# [2, 3, 5, 6, 7, 8, 9, 12, 31]


# 정답: 1, 5





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
        # 문제 오류: !=이 아니고, ==임 
        while(x[l] == ' '):
            l += 1
        # 문제 오류: !=이 아니고, ==임 
        while(x[r] == ' '):
            r -= 1
        if x[l] != x[r]:
            return False
        else:
            _ = 0
            # 주석처리된 자리
        
    return True

p5_str = "a nut for a jar of tuna"
# print(is_palindrome(p5_str))      # 무한 루프 

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


print()
print("문제 10.")

# 보기 1. 
print("보기 1.")

def is_palindrome_1(x):
    print(x)
    l = 0
    r = len(x) - 1
    while (l < r):
        print(x)
        print(' ' * l + '|' + ' ' * (r - l - 1) + '|')
        while(x[l] == ' '):
            l += 1
        while(x[r] == ' '):
            r -= 1
            
        if(l < r):
            print(' ' * l + '^' + ' ' * (r - l - 1) + '^')
        elif(l == r):
            print(' ' * l + '^')
            return True
        else:
            print(' ' * l + '^' + ' ' * (r - l - 1) + '^')
            return True
        
        if x[l] != x[r]:
            print('x[l] =', x[l], ', x[r] =', x[r])
            return False
        else:
            _ = 0
            l += 1
            r -= 1
    return True

p5_str = "a nut for a jar of tuna"
print(is_palindrome_1(p5_str))

# 출력:
# 보기 1.
# a nut for a jar of tuna
# a nut for a jar of tuna
# |                     |
# ^                     ^
# a nut for a jar of tuna
#  |                   |
#   ^                  ^
# a nut for a jar of tuna
#    |                |
#    ^                ^
# a nut for a jar of tuna
#     |              |
#     ^              ^
# a nut for a jar of tuna
#      |            |
#       ^          ^
# a nut for a jar of tuna
#        |        |
#        ^        ^
# a nut for a jar of tuna
#         |      |
#         ^     ^
# a nut for a jar of tuna
#          |   |
#           ^  ^
# a nut for a jar of tuna
#            ||
#             ^
# True
# (정답)



# 보기 2. 
print("보기 2.")

def is_palindrome_2(x):
    print(x)
    l = 0
    r = len(x) - 1
    while (l < r):
        print(x)
        print(' ' * l + '|' + ' ' * (r - l - 1) + '|')
        while(x[l] == ' '):
            l += 1
        while(x[r] == ' '):
            r -= 1
            
        if(l < r):
            print(' ' * l + '^' + ' ' * (r - l - 1) + '^')
        elif(l == r):
            print(' ' * l + '^')
            return True
        else:
            print(' ' * l + '^' + ' ' * (r - l - 1) + '^')
            return True
        
        if x[l] != x[r]:
            print('x[l] =', x[l], ', x[r] =', x[r])
            return False
        else:
            _ = 0
            l += 1
    return True

p5_str = "a nut for a jar of tuna"
print(is_palindrome_2(p5_str))

# 출력:
# 보기 2.
# a nut for a jar of tuna
# a nut for a jar of tuna
# |                     |
# ^                     ^
# a nut for a jar of tuna
#  |                    |
#   ^                   ^
# x[l] = n , x[r] = a
# False
# (오답)


# 보기 3. 
print("보기 3.")

def is_palindrome_3(x):
    print(x)
    l = 0
    r = len(x) - 1
    while (l < r):
        print(x)
        print(' ' * l + '|' + ' ' * (r - l - 1) + '|')
        while(x[l] == ' '):
            l += 1
        while(x[r] == ' '):
            r -= 1
            
        if(l < r):
            print(' ' * l + '^' + ' ' * (r - l - 1) + '^')
        elif(l == r):
            print(' ' * l + '^')
            return True
        else:
            print(' ' * l + '^' + ' ' * (r - l - 1) + '^')
            return True
        
        if x[l] != x[r]:
            print('x[l] =', x[l], ', x[r] =', x[r])
            return False
        else:
            _ = 0
            r += 1
    return True

p5_str = "a nut for a jar of tuna"
# print(is_palindrome_3(p5_str))    # 에러 

# 출력:
# 보기 3.
# a nut for a jar of tuna
# a nut for a jar of tuna
# |                     |
# ^                     ^
# a nut for a jar of tuna
# |                      |
# 인덱스 에러
# (오답)


# 보기 4. 
print("보기 4.")

def is_palindrome_4(x):
    print(x)
    l = 0
    r = len(x) - 1
    while (l < r):
        print(x)
        print(' ' * l + '|' + ' ' * (r - l - 1) + '|')
        while(x[l] == ' '):
            l += 1
        while(x[r] == ' '):
            r -= 1
            
        if(l < r):
            print(' ' * l + '^' + ' ' * (r - l - 1) + '^')
        elif(l == r):
            print(' ' * l + '^')
            return True
        else:
            print(' ' * l + '^' + ' ' * (r - l - 1) + '^')
            return True
        
        if x[l] != x[r]:
            print('x[l] =', x[l], ', x[r] =', x[r])
            return False
        else:
            _ = 0
            l -= 1
            r -= 1
    return True

p5_str = "a nut for a jar of tuna"
print(is_palindrome_4(p5_str))    

# 출력:
# 보기 4.
# a nut for a jar of tuna
# a nut for a jar of tuna
# |                     |
# ^                     ^
# a nut for a jar of tuna
# |                     |
# ^                     ^
# x[l] = a , x[r] = n
# False
# (오답)


# 보기 5. 
print("보기 5.")

def is_palindrome_5(x):
    print(x)
    l = 0
    r = len(x) - 1
    while (l < r):
        print(x)
        print(' ' * l + '|' + ' ' * (r - l - 1) + '|')
        while(x[l] == ' '):
            l += 1
        while(x[r] == ' '):
            r -= 1
            
        if(l < r):
            print(' ' * l + '^' + ' ' * (r - l - 1) + '^')
        elif(l == r):
            print(' ' * l + '^')
            return True
        else:
            print(' ' * l + '^' + ' ' * (r - l - 1) + '^')
            return True
        
        if x[l] != x[r]:
            print('x[l] =', x[l], ', x[r] =', x[r])
            return False
        else:
            _ = 0
            l = r = 0
    return True

p5_str = "a nut for a jar of tuna"
print(is_palindrome_5(p5_str))    

# 출력:
# 보기 5.
# a nut for a jar of tuna
# a nut for a jar of tuna
# |                     |
# ^                     ^
# True
# (오답)


# 정답: 1




# 문제 11.
# p6_str을 i칸 왼쪽으로 회전시켜서 출력하시오

p6_str = "ABCDEFGHIJKLMNOPQURSTUVWXYZ"

for i in range(0, len(p6_str)):
    _ = i
    #코드를 입력할 위치


print()
print("문제 11.")

# 답안 1.

print("답안 1:")
for i in range(0, len(p6_str)):
    _ = i
    print(p6_str[i:] + p6_str[:i])

# 출력:
# ABCDEFGHIJKLMNOPQURSTUVWXYZ
# BCDEFGHIJKLMNOPQURSTUVWXYZA
# CDEFGHIJKLMNOPQURSTUVWXYZAB
# DEFGHIJKLMNOPQURSTUVWXYZABC
# EFGHIJKLMNOPQURSTUVWXYZABCD
# FGHIJKLMNOPQURSTUVWXYZABCDE
# GHIJKLMNOPQURSTUVWXYZABCDEF
# HIJKLMNOPQURSTUVWXYZABCDEFG
# IJKLMNOPQURSTUVWXYZABCDEFGH
# JKLMNOPQURSTUVWXYZABCDEFGHI
# KLMNOPQURSTUVWXYZABCDEFGHIJ
# LMNOPQURSTUVWXYZABCDEFGHIJK
# MNOPQURSTUVWXYZABCDEFGHIJKL
# NOPQURSTUVWXYZABCDEFGHIJKLM
# OPQURSTUVWXYZABCDEFGHIJKLMN
# PQURSTUVWXYZABCDEFGHIJKLMNO
# QURSTUVWXYZABCDEFGHIJKLMNOP
# URSTUVWXYZABCDEFGHIJKLMNOPQ
# RSTUVWXYZABCDEFGHIJKLMNOPQU
# STUVWXYZABCDEFGHIJKLMNOPQUR
# TUVWXYZABCDEFGHIJKLMNOPQURS
# UVWXYZABCDEFGHIJKLMNOPQURST
# VWXYZABCDEFGHIJKLMNOPQURSTU
# WXYZABCDEFGHIJKLMNOPQURSTUV
# XYZABCDEFGHIJKLMNOPQURSTUVW
# YZABCDEFGHIJKLMNOPQURSTUVWX
# ZABCDEFGHIJKLMNOPQURSTUVWXY




# 문제 12.
# p7_dst_str을 p7_src_str에서 세칸 왼쪽으로 회전시켜서 구하시오
    
p7_src_str = "ABCDEFGHIJKLMNOPQURSTUVWXYZ"
p7_dst_str = p7_src_str # 코드를 입력할 위치

print()
print("문제 12.")

# 답안 1.
print("답안 1:")
p7_src_str = "ABCDEFGHIJKLMNOPQURSTUVWXYZ"
p7_dst_str = p7_src_str[3:] + p7_src_str[:3]

print(p7_dst_str)

# 출력:
# 답안 1:
# DEFGHIJKLMNOPQURSTUVWXYZABC




# 문제 13
# a의 src_str에서 인덱스를 index 함수로 구한 뒤 dst_str의 해당 인덱스 문자열을
# 반환하는 ciper(a) 함수에서 주석처리된 부분에 들어갈 코드를 쓰시오.

def ciper(a):
    return p7_dst_str # 주석 처리된 부분

print(p7_src_str.index('A'), ciper('A'))
print(p7_src_str.index('B'), ciper('B'))


print("문제 13.")
# 답안 1.
print("답안 1:")

def ciper_1(a):
    return p7_dst_str[p7_src_str.index(a)]

print(p7_src_str.index('A'), ciper_1('A'))
print(p7_src_str.index('B'), ciper_1('B'))

# 출력:
# 답안 1:
# 0 D
# 1 E

ciper = ciper_1




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
# print(ciper_all(p7_my_str))       # 에러 

print("문제 14")
# 답안 1.
print("답안 1:")

def ciper_all_1(decoded_str):
    encoded_str = ''
    for a in decoded_str:
        if a in p7_src_str:
            encoded_str += ciper(a)
        else:
            encoded_str += a
    return encoded_str

p7_my_str = "ATTACK TONIGHT!"
print(ciper_all_1(p7_my_str))

# 출력:
# 답안 1:
# DWWDFN WUQLJKW!

ciper_all = ciper_all_1



# 문제 15

#p7과 같이 p8_src_str에서 ciper(a), ciper_all(decoded_str)을 구현하시오
#p8_src_str = "ABCDEFGHIJKLMNOPQURSTUVWXYZabcdefghijklmnopqrstuvwxyz"
#p8_dst_str = p8_src_str[3:] + p8_src_str[:3]

def ciper(a):
    _ = a

def ciper_all(decoded_str):
    _ = decoded_str

p8_my_str = "Veni, vidi, vici."
print(ciper_all(p8_my_str))


print("문제 15.")
# 답안 1
print("답안 1:")

p8_src_str = "ABCDEFGHIJKLMNOPQURSTUVWXYZabcdefghijklmnopqrstuvwxyz"
p8_dst_str = p8_src_str[3:] + p8_src_str[:3]

def ciper(a):
    return p8_dst_str[p8_src_str.index(a)] if a in p8_src_str else a
    
def ciper_all(decoded_str):
    return ''.join(ciper(a) for a in decoded_str)

p8_my_str = "Veni, vidi, vici."
print(ciper_all(p8_my_str))

# 출력:
# Yhql, ylgl, ylfl.



# 문제 16. 
# my_string에서 모든 공백문자를 제거한 문자열을 반환하는 
# remove_space(my_string)을 구현하시오

def remove_space(my_string):
    ret = ''
    return ret


print("문제 16.")

# 답안 1.
print("답안 1.")

def remove_space(my_string):
    ret = ''.join(x for x in my_string if x != ' ')
    return ret

print(remove_space("a nut for a jar of tuna"))
# 출력:
# anutforajaroftuna



# 문제 17. 
# my_string에서 index로 부터 하나씩 양쪽으로 뻗어나가는 회문의 
# 가장 긴 길이를 구하고, 회문 문자열, 회문의 길이를 반환하시오 

def longest_odd_palindromic_from_root(my_string, index):
    i = 1    
    ret = my_string
    return ret, i


print("문제 17.")
# 답안 1:
print("답안 1:")

def longest_odd_palindromic_from_root_1(my_string, index):
    i = 1
    i_max = min(index + 1, len(my_string) - index)
    while i < i_max:
        if my_string[index - i] == my_string[index + i]:
            i = i + 1
        else:
            break
    ret = my_string[index - i + 1 : index + i]    
    return ret, 2 * i - 1

print(longest_odd_palindromic_from_root_1("anutforajaroftuna", 8)) 
print(longest_odd_palindromic_from_root_1("anutforajaroftuna", 7)) 

# 출력:
# 답안 1:
# ('anutforajaroftuna', 17)
# ('a', 1)

longest_odd_palindromic_from_root = longest_odd_palindromic_from_root_1


# 문제 18. 
# my_string에서 index와 index+1로 부터 하나씩 양쪽으로 뻗어나가는 회문의 
# 가장 긴 길이를 구하고, 회문 문자열, 회문의 길이를 반환하시오 

def longest_even_palindromic_from_root(my_string, index):
    i = 1
    ret = my_string
    return ret, i


print("문제 18.")
# 답안 1.
print("답안 1:")

def longest_even_palindromic_from_root_1(my_string, index):
    i = 0
    i_max = min(index + 1, len(my_string) - index - 1)
    while i < i_max:
        if my_string[index - i] == my_string[index + 1 + i]:
            i = i + 1
        else:
            break
    ret = my_string[index - i + 1 : index + 1 + i]    
    return ret, 2 * i

print(longest_even_palindromic_from_root_1("abcdeffedcba", 5)) 
print(longest_even_palindromic_from_root_1("abcdeffedcba", 6)) 

# 출력:
# 답안 1:
# ('abcdeffedcba', 12)
# ('', 0)

longest_even_palindromic_from_root = longest_even_palindromic_from_root_1


# 문제 19. 
# p9_my_str 내에서 가장 긴 회문을 찾아서 출력하시오

p9_my_str = "ATTACK"
print("longest palindromic string")


print("문제 19.")
# 답안 1.
print("답안 1:")

i = 0
res = ''
for index in range(len(p9_my_str)):
    res_odd, i_odd = longest_odd_palindromic_from_root(p9_my_str, index)
    if i < i_odd:
        res, i = res_odd, i_odd
    res_even, i_even = longest_even_palindromic_from_root(p9_my_str, index)
    if i < i_even:
        res, i = res_even, i_even
print(res, i)    

# 출력:
# 답안 1:
# ATTA 4




# 문제 20-1
# 정수 데이터와 필드폭을 받아서 해당 문자열을 출력하시오
def my_format_int(int_data, width = 0):
    ret = ''
    return ret

print("문제 20-1.")
# 답안 1.
print("답안 1:")
def my_format_int(int_data, width = 0):
    str_data = str(int_data)
    ret = str_data if len(str_data) >= width \
                   else ' ' * (width-len(str_data)) + str_data
    return ret

print(my_format_int(12345, 10))
# 출력:
# 답안 1:
#      12345




# 문제 20-2
# 실수 데이터와 필드폭과 정밀도를 받아서 해당 문자열을 출력하시오
def my_format_float(float_data, width = 0, precision = 6):
    ret = ''
    return ret
    

print("문제 20-2.")
# 답안 1.
print("답안 1:")
def my_format_float(float_data, width = 0, precision = 6):
    str_data = str(float_data)
    left, right = str_data.split('.')
    if len(right) < precision:
        right = right + '0' * (precision - len(right))
    elif len(right) > precision:
        right = right[:precision]
    else:
        right = right
    str_data = left + '.' + right
    ret = str_data if len(str_data) >= width \
                   else ' ' * (width-len(str_data)) + str_data
    return ret

print(my_format_float(123.45, 10, 3))
# 출력:
# 답안 1:
#    123.450


