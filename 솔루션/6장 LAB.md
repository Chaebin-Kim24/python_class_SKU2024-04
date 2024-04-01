### LAB 6-1
```python
capital_dic = {'Korea':'Seoul', 'China':'Beijing', 'USA':'Washington DC'}
print(capital_dic['Korea'])
print(capital_dic['China'])
print(capital_dic['USA'])
# 출력:
# Seoul
# Beijing
# Washington DC

fruits_dic = {'apple':5000, 'banana':4000, 'grape':5300, 'melon':6500}
print('apple' '의 가격은', fruits_dic['apple'], '원입니다.')
print('banana' '의 가격은', fruits_dic['banana'], '원입니다.')
print('grape' '의 가격은', fruits_dic['grape'], '원입니다.')
print('melon' '의 가격은', fruits_dic['melon'], '원입니다.')
# 출력:
# apple의 가격은 5000 원입니다.
# banana의 가격은 4000 원입니다.
# grape의 가격은 5300 원입니다.
# melon의 가격은 6500 원입니다.
```

### LAB 6-2
```python
person = {'이름': '홍길동', '나이': 26, '몸무게': 82}
print(person)
# 출력: {'이름': '홍길동', '나이': 26, '몸무게': 82}

person['특기'] = '분신술'
print(person)
# 출력: {'이름': '홍길동', '나이': 26, '몸무게': 82, '특기': '분신술'}

person['아버지'] = '홍판서'
print(person)
# 출력: {'이름': '홍길동', '나이': 26, '몸무게': 82, '특기': '분신술', '아버지': '홍판서'}

del person['나이']
print(person)
# 출력: {'이름': '홍길동', '몸무게': 82, '특기': '분신술', '아버지': '홍판서'}
```

### LAB 6-3
```python
capital_dic = {'Korea':'Seoul', 'China':'Beijing', 'USA':'Washington DC'}
print('Korea' in capital_dic)
# 출력: True

print('China' in capital_dic)
# 출력: True

print('Indonesia' in capital_dic)
# 출력: False

print('Beijing' in capital_dic)
# 출력: False
```

### LAB 6-4
```python
fruits_dic = {'apple':6000, 'banana':3000, 'grape':5000, 'melon':7000}
print(fruits_dic)
# 출력: {'apple': 6000, 'banana': 3000, 'grape': 5000, 'melon': 7000}

print(fruits_dic.keys())
dict_keys(['apple', 'banana', 'grape', 'melon'])

print(fruits_dic.values())
dict_values([6000, 3000, 5000, 7000])

fruits_dic.pop('apple')
print(fruits_dic)
{'banana': 3000, 'grape': 5000, 'melon': 7000}

fruits_dic.clear()
print(fruits_dic)
{}
```

### LAB 6-5
```python
fruits_dic = {'apple':6000, 'melon':3000, 'banana':5000, 'orange':4000}
print(list(fruits_dic))
# 출력: ['apple', 'melon', 'banana', 'orange']

print(list(fruits_dic.values()))
# 출력: [6000, 3000, 5000, 4000]

print('fruits_dic 딕셔너리의 항목의 개수 :', len(fruits_dic))
# 출력: fruits_dic 딕셔너리의 항목의 개수 : 4

is_in = ''
if 'apple' not in fruits_dic:
    is_in = 'not '
print('apple is {}in fruits_dic.'.format(is_in))
# 출력: apple is in fruits_dic.

is_in = ''
if 'mango' not in fruits_dic:
    is_in = 'not '
print('mango is {}in fruits_dic.'.format(is_in))
# 출력: mango is not in fruits_dic.
```

### LAB 6-6
```python
the_day = 1919, 3, 1
year, month, day = the_day

print('{}년 {}월 {}일은 삼일절입니다.'.format(year, month, day))
# 출력: 1919년 3월 1일은 삼일절입니다.

c, b, a = tuple([10, 20, 30])
print('a =', a)
print('b =', b)
print('c =', c)
# 출력:
# a = 30
# b = 20
# c = 10
```

### LAB 6-7
```python
person = '홍길동', 2019001, 179
print('person =', person)
# 출력: person = ('홍길동', 2019001, 179)

# person[1] = 2019003
# TypeError: 'tuple' object does not support item assignment

person_list = list(person)
person_list[1] = 2020003

person = tuple(person_list)
print('학번 변동 후 person =', person)
# 출력: 학번 변동 후 person = ('홍길동', 2020003, 179)
```

### LAB 6-8
```python
def square(x, y):
    return x**2, y**2
x = 10
y = 20
x_sq, y_sq = square(x, y)
print('{} 제곱 = {}, {} 제곱 = {}'.format(x, x_sq, y, y_sq))
# 출력: 10 제곱 = 100, 20 제곱 = 400

print((10, 20, 30) + (40, 50, 60))
# 출력: (10, 20, 30, 40, 50, 60)

print('Hello ' * 3)
# 출력: Hello Hello Hello

print(('Hello ',) * 3)
# 출력: ('Hello ', 'Hello ', 'Hello ')
```

### LAB 6-9
```python
lst = ['apple', 'mango', 'banana']
s1 = set(lst)
print(lst)
print(s1)
# 출력:
# ['apple', 'mango', 'banana']
# {'mango', 'apple', 'banana'}

greet = 'Good afternoon'
s2 = set(greet)
print(greet)
print(s2)

# 출력:
# Good afternoon
# {'e', 'a', 'G', 'd', 'o', 't', 'r', 'n', 'f', ' '}
```

### LAB 6-10
```python
s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60, 70}
print(s1 | s2)
# 출력: {70, 40, 10, 50, 20, 60, 30}

print(s1 & s2)
# 출력: {40, 30}

print(s1 - s2)
# 출력: {10, 20}

print(s1 ^ s2)
# 출력: {50, 20, 70, 10, 60}

print(s1.issubset(s2))
# 출력: False

print(s1.issuperset(s2))
# 출력: False

print(s1.isdisjoint(s2))
# 출력: False
```

### LAB 6-11
```python
def product(set1, set2):
    tmp = ((),)
    result = ()
    for x in tmp:        
        for y in set1:
            result = result + ( x + (y,), )

    tmp = result
    result = ()
    for x in tmp:
        for y in set2:
            result = result + ( x + (y,), )

    return set(result)

A = {1, 2}
B = {'A', 'B', 'C'}

print('AXB =', product(A, B))
# 출력: AXB = {(2, 'C'), (2, 'A'), (2, 'B'), (1, 'C'), (1, 'A'), (1, 'B')}

print('BXA =', product(B, A))
# 출력: BXA = {('A', 2), ('C', 1), ('B', 1), ('A', 1), ('C', 2), ('B', 2)}

print('AXA =', product(A, A))
# 출력: AXA = {(1, 1), (1, 2), (2, 1), (2, 2)}

print('BXB =', product(B, B))
# 출력: BXB = {('C', 'C'), ('C', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'A'), ('C', 'A'), ('B', 'B'), ('A', 'A'), ('A', 'B')}
```

### LAB 6-12
```python

def exp(input_set, exponent=1):
    tmp = ((),)
    result = ((),)

    for _ in range(exponent):
        tmp = result
        result = ()
        for x in tmp:
            for y in input_set:
                result = result + ( x + (y,), )

    return set(result)

def tuple_sum(input_tuple):
    return sum(input_tuple)

set_1_to_6 = set(range(1,7))
set_1_to_6_exp_3 = exp(set_1_to_6, 3)

print('주사위를 세 번 던져 발생할 수 있는 사건은 {} 가지 경우가 있습니다.'.format(len(set_1_to_6_exp_3)))
# 출력: 주사위를 세 번 던져 발생할 수 있는 사건은 216 가지 경우가 있습니다.

case_greater_than_or_equal_10 = 0
for s in set_1_to_6_exp_3:
    if tuple_sum(s) >= 10:
        case_greater_than_or_equal_10 += 1

print('주사위를 세 번 던져 나온 눈의 합이 10 이상인 경우는 {} 가지 있니다.'.format(case_greater_than_or_equal_10))
# 출력: 주사위를 세 번 던져 나온 눈의 합이 10 이상인 경우는 135 가지 있니다.

def prob_over(x):
    case_over_x = 0
    for s in set_1_to_6_exp_3:
        if tuple_sum(s) >= x:
            case_over_x += 1
    return 100*case_over_x / len(set_1_to_6_exp_3)

for i in range(3, 19):
    print('눈의 합으로 {:2d} 이상을 얻을 확률 {:6.2f}%'.format(i, prob_over(i)))

# 출력:
# 눈의 합으로  3 이상을 얻을 확률 100.00%
# 눈의 합으로  4 이상을 얻을 확률  99.54%
# 눈의 합으로  5 이상을 얻을 확률  98.15%
# 눈의 합으로  6 이상을 얻을 확률  95.37%
# 눈의 합으로  7 이상을 얻을 확률  90.74%
# 눈의 합으로  8 이상을 얻을 확률  83.80%
# 눈의 합으로  9 이상을 얻을 확률  74.07%
# 눈의 합으로 10 이상을 얻을 확률  62.50%
# 눈의 합으로 11 이상을 얻을 확률  50.00%
# 눈의 합으로 12 이상을 얻을 확률  37.50%
# 눈의 합으로 13 이상을 얻을 확률  25.93%
# 눈의 합으로 14 이상을 얻을 확률  16.20%
# 눈의 합으로 15 이상을 얻을 확률   9.26%
# 눈의 합으로 16 이상을 얻을 확률   4.63%
# 눈의 합으로 17 이상을 얻을 확률   1.85%
# 눈의 합으로 18 이상을 얻을 확률   0.46%
```

