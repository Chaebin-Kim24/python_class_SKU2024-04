### LAB 5-1
```python
even_list = [2, 4, 6, 8, 10]
print('even_list =', even_list)
#출력: even_list = [2, 4, 6, 8, 10]

even_list = list(range(2, 11, 2))
print('even_list =', even_list)
#출력: even_list = [2, 4, 6, 8, 10]

nations = ['Korea', 'China', 'India', 'Nepal']
print('nations =', nations)
#출력: nations = ['Korea', 'China', 'India', 'Nepal']

friends = ['길동', '철수', '은지', '지은', '영민']
print('friends =', friends)
#출력: friends = ['길동', '철수', '은지', '지은', '영민']

string = list('XYZ')
print('string =', string)
#출력: string = ['X', 'Y', 'Z']
```

### LAB 5-2
```python
prime_list = [2, 3, 5, 7]
print('prime_list의 첫 원소 :', prime_list[0])
# 출력: prime_list의 첫 원소 : 2

print('prime_list의 마지막 원소 :', prime_list[3])
# 출력: prime_list의 마지막 원소 : 7

print('prime_list의 마지막 원소 :', prime_list[-1])
# 출력: prime_list의 마지막 원소 : 7

nations = ['Korea', 'China', 'Russia', 'Malaysia']
print('nations의 첫 원소 :', nations[0])
# 출력: nations의 첫 원소 : Korea

print('nations의 마지막 원소 :', nations[-1])
# 출력: nations의 마지막 원소 : Malaysia

print('nations의 마지막 원소 :', nations[len(nations)-1])
# 출력: nations의 마지막 원소 : Malaysia
```

### LAB 5-3
```python
prime_list = [2, 3, 5, 7]
print('소수 목록 :', prime_list)
prime_list.append(11)
print('추가 후 소수 목록 :', prime_list)
# 출력:
# 소수 목록 : [2, 3, 5, 7]
# 추가 후 소수 목록 : [2, 3, 5, 7, 11]

print('삭제 전 소수 목록 :', prime_list)
prime_list.remove(3)
print('삭제 후 소수 목록 :', prime_list)
# 출력:
# 삭제 전 소수 목록 : [2, 3, 5, 7, 11]
# 삭제 후 소수 목록 : [2, 5, 7, 11]
```

### LAB 5-4
```python
prime_list = [2, 3, 5, 7]
print('1에서 10까지의 소수 :', prime_list)
print('최솟값 :', min(prime_list))
print('최댓값 :', max(prime_list))
print('합계 :', sum(prime_list))
print('평균 :', sum(prime_list)/len(prime_list))
# 출력:
# 1에서 10까지의 소수 : [2, 3, 5, 7]
# 최솟값 : 2
# 최댓값 : 7
# 합계 : 17
# 평균 : 4.25

nations = ['Korea', 'China', 'Russia', 'Malaysia']
print('국가 목록 :', nations)
print('사전에 가장 먼저 나오는 나라 :', min(nations))
print('사전에 가장 뒤에 나오는 나라 :', max(nations))
# 출력:
# 국가 목록 : ['Korea', 'China', 'Russia', 'Malaysia']
# 사전에 가장 먼저 나오는 나라 : China
# 사전에 가장 뒤에 나오는 나라 : Russia
```

### LAB 5-5
```python
# [1, 2, 3, [10, 20, 30]]
# [1, 2, 3, 10, 20, 30]

nlist = []
for i in range(1, 11):
    nlist.append(i)
print('nlist =', nlist)
# 출력: nlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nlist.insert(0, 0)
print('nlist =', nlist)
# 출력: nlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nlist.reverse()
print('nlist =', nlist)
# 출력: nlist = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

last = nlist.pop()
print('마지막 원소 =', last)
print('nlist =', nlist)
# 출력:
마지막 원소 = 0
nlist = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

### LAB 5-6
```python
n = int(input('반복할 정수를 입력하시오 : '))
print([1, 2, 3] * n)
# 출력:
# 반복할 정수를 입력하시오 : 3
# [1, 2, 3, 1, 2, 3, 1, 2, 3]

n = int(input('반복할 정수를 입력하시오 : '))
print([1, 2, 3] * n)
# 반복할 정수를 입력하시오 : 4
# [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
```

### LAB 5-7
```python
n_list = list(range(15))
print("n_list =", n_list)
# 출력: n_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

s_list1 = n_list[:5]
print("s_list1 =", s_list1)
# 출력: s_list1 = [0, 1, 2, 3, 4]

s_list2 = n_list[5:11]
print("s_list2 =", s_list2)
# 출력: s_list2 = [5, 6, 7, 8, 9, 10]

s_list3 = n_list[11:15]
print("s_list3 =", s_list3)
# 출력: s_list3 = [11, 12, 13, 14]

s_list4 = n_list[2:11:2]
print("s_list4 =", s_list4)
# 출력: s_list4 = [2, 4, 6, 8, 10]

s_list5 = n_list[10:5:-1]
print("s_list5 =", s_list5)
# 출력: s_list5 = [10, 9, 8, 7, 6]

s_list6 = n_list[10:1:-2]
print("s_list6 =", s_list6)
# 출력: s_list6 = [10, 8, 6, 4, 2]
```

