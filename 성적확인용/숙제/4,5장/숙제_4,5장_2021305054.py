# 학번 2021305054
# 이름 이승언

#4.1


def my_greet():
    print('안녕하세요.')
my_greet()
my_greet()


#4.2번
def yes(n):
    return n ** 2
    
print('3의 제곱은 : ',yes(3))
print('3의 제곱은 : ',yes(4))

#24번
def sentence():
    
    sent = input('여러 단어로 이루어진 글을 입력하세요: ')
    
    sent = sent.replace("-"," ").replace(":"," ").replace("."," ").replace(","," ")
    words = sent.split()
    
    sortedsent = sorted(words)
    print('정렬 결과 : ',sortedsent)
    
sentence()


#25번
def replacename():
    
    s1 = 'kang Young Min'
    s2 = ' kang Young-Min'
    s3 = 'park Dong Min'
    s4 = ' park Dong-Yun'


    s1 =s1.replace(" ","").replace("-","").upper()
    number1= s1.count("N")
    s2 =s2.replace(" ","").replace("-","").upper()
    number2= s2.count("N")
    s3 = s3.replace(" ","").replace("-","").upper()
    number3= s3.count("N")
    s4 = s4.replace(" ","").replace("-","").upper()
    number4= s4.count("N")


    print('kang Young Min(은)는',s1,'(으)로 수정됨')
    print(' kang Young-Min(은)는',s2,'(으)로 수정됨')
    print('park Dong Min(은)는',s3,'(으)로 수정됨')
    print(' park Dong-Yun(은)는',s4,'(으)로 수정됨')

    print(s1,":",number1,"개의 N이 나타남")
    print(s2,":",number2,"개의 N이 나타남")
    print(s3,":",number3,"개의 N이 나타남")
    print(s4,":",number4,"개의 N이 나타남")

replacename()


#4.26
def dele():
    
    s5 = "Park(Java city), Kim(C city), Kang(Bython city), Lee(Bython city), Hong(Ruby city), Cho(Bython city), Koo(C city), Ryu(C++ city)"
    print("주어진 문자열\n", s5)
    number5= s5.count("B")
    s5 = s5.replace("B", "P")
    
    print("수정된 문자열\n", s5)
    print("Bython 문자열은 모두",number5,"번 수정했습니다.")
dele()

#4.27

        
def unit(num):
    n = 1
    old_num = 1.0
    
    while True:
        old = abs(1/n - num)
        if (old <= old_num):
            old_num = old
        else:
            break
        
        n += 1
    
    return n - 1
        

n6 = float(input("1보다 적고 0보다 큰 소수를 입력하세요: "))

if n6 <= 0 or n6 > 1:
    print("입력값 오류")
else:
    nf = unit(n6)
    
    print("가장 가까운 단위 분수는 ",nf,"입니다. 그리고 이 값은",1/nf,"입니다.")
    

    
#5.17

animals = ['dog', 'cat', 'tiger', 'lion']    
print("animals =", animals)

animals[0], animals [1], animals[2], animals[3] = animals[1], animals[2], animals[3], animals[0]
print("animals =", animals)


animals_1 = ['dog', 'cat', 'tiger', 'lion']
love = ['i love', 'i love', 'i love', 'i love']
i = 0
for n in animals_1:
    print(love[i], animals_1[i])
    i = i + 1
    
 
#5.18




s1_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cbbc', 'opq']

min_s1_list = s1_list[0]
for i in range(1, len(s1_list)):
    if len(min_s1_list) > len(s1_list[i]):
        min_s1_list = s1_list[i]
print(min_s1_list)

max_s1_list = s1_list[0]
for i in range(1, len(s1_list)):
    if len(max_s1_list) < len(s1_list[i]):
        max_s1_list = s1_list[i]
print(max_s1_list)


s12_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cbbc', 'opq']

Min_s1_list = sorted(s12_list, key = len) 


for i in range(1, len(s12_list)):
    if len(Min_s1_list[0]) < len(s12_list[i-1]):
        Min_s1_list.remove(s12_list[i-1])
        
      
    
print(Min_s1_list)   
    




#5.19

s_list = ['abc', 'bcd', 'abc', 'abba', 'cbbc', 'opq', 'opq']
new_list = [0]
for n in s_list:
    if n not in new_list:
        new_list.append(n)
       
    
print(s_list)
print(new_list)


#5.20

src = input(str('a~g까지 문자를 입력하시오: '))

def string(s):
    
    com = ""
    last = s[0]
    count = 1
    for char in s[1:]:
        
        if char == last:
            count = count + 1
        else:
            
            com = com + last + str(count)
           
            last = char
            count = 1

   
    com = com + last + str(count)

    return com



com_src = string(src)

print("수정된 문자열:",{com_src})




#5.21

## 잘못된 메세지 
string = input(str('a~g까지 문자를 입력하시오: '))


def exp_string(s):
    
    result = ''
   
    i = 0
    while i < len(s):
        
        char = s[i]
        i += 1
       
        num = ''
        while i < len(s) and s[i].isdigit():
            num += s[i]
            i += 1
        
        result += char * int(num)
    
    return result


#5.22

print(exp_string(string))     




n = int(input("n을 입력하시오 : "))

result = []

current_num = 1

for i in range(n):
 
    row = list(range(current_num, current_num + n))

    if i % 2 == 1:
        row = row[::-1]  
    result.append(row)

    current_num += n


for row in result:
    print(' '.join(map(str, row)))



#5.23
    
person1 = ['온달', 20, 1, 180.0, 100]
person2 = ['이사부', 25, 1, 170.0, 700]        
person3 = ['평강', 22, 0, 169.0, 60]    
person4 = ['혁거세', 40, 1, 150.0, 50]

person_list = person1 + person3 + person4
print(person_list)

#1
def how_many_persons(n):
    x = len(n) / 5
    
    return x
n_persons = how_many_persons(person_list)
print(str(n_persons)+'명의 정보가 담겨있습니다.')

person_list = person1 + person2 + person3 + person4
#2
def comput_average_age(y):
    age = y[1:20:5]
    sum = int(age[0]) + int(age[1]) + int(age[2]) + int(age[3])
    sum = sum / 4
    return sum

average_age = comput_average_age(person_list)

print('평균나이는'+ str(average_age)+'세입니다.')

#3

person_list = person1 + person2 + person3 + person4


def count_males_females(z):
    male = z.count(1)
    female = z.count(0)
    
    return male, female
    
n_male, n_female = count_males_females(person_list)

print('리스트에는 남자가',n_male,'명, 여자가',n_female,'명입니다.')

#4

person_list = person1 + person2 + person3 + person4

def display_persons(b):
    ondal = b[0:5]
    leesaboo = b[5:10]
    pyunggang = b[10:15]
    hyukgusae = b[15:20]
    
   
    return ondal, leesaboo, pyunggang, hyukgusae

display_persons(person_list)

person5, person6, person7, person8 = display_persons(person_list)

print(person5)
print(person6)
print(person7)
print(person8)
