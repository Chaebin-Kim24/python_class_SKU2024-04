# 3-20 
n = int(input('숫자를 입력하세요 : '))
for i in range(n):
    line = str()
    for j in range(1, n-i):
        line += ' '
    for j in range(n-i, n+1):
        line += '*'
    print(line)

# 3-21
n = int(input('숫자를 입력하세요 : '))
if n <= 1 or (n > 2 and n % 2 == 0):
    is_prime = False
else:
    is_prime = True
    
for i in range(3, n, 2):
    if n % i == 0:
        is_prime = False

if n % 10 == 0 or n % 10 == 1 or n % 10 == 3 or n % 10 == 6 or n % 10 == 7 or n % 10 == 8:
    eun_nun = '은'
else:
    eun_nun = '는'

string = str(n) + eun_nun + ' 소수'
    
if is_prime:
    print(string +  '입니다')
else:
    print(string + ' 아닙니다')

# 3-22
for n in range(2, 13):
    if n > 2 and n % 2 == 0:
        is_prime = False
    else:
        is_prime = True
    
    for i in range(3, n, 2):
        if n % i == 0:
            is_prime = False

    string = str(n) + " :"

    if is_prime:
        print(string, '소수')
    else:
        print(string, '합성수')

# 3-23
n = int(input('숫자를 입력하세요 : '))
while n <= 0:
    n = int(input('양의 정수를 입력하세요 : '))

sum_value = 0
for i in range(1, n + 1):
    sum_value += i ** 2

print('결과는 ' + str(sum_value) + '입니다.')

# 3-24
n = int(input('숫자를 입력하세요 : '))

sum_value = 0
for i in range(1, n + 1):
    sum_value += 1 / (i ** 2)

print('결과는 ' + str(sum_value) + '입니다.')

# 3-25
pos = 0
day = 1
night = False
while pos < 30:
    if not night:
        pos += 7
        print('day :', day, '\t' '달팽이의 위치 :', pos, '미터')
        night = True
    else:
        pos -= 5
        day += 1
        night = False

print('우물을 탈출하는 데 걸린 날은', str(day) + '일 입니다.')
