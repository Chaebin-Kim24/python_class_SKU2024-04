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
