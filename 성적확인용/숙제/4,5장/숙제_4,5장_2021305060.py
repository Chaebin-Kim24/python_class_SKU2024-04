# 학번 2021305060
# 이름 이종희

#LAB 4-1
def my_greet():
    print('환영합니다.')

my_greet()
my_greet()

#LAB 4-2
def square(n):
    return n**2
print('3의 제곱은:',square(3))
print('4의 제곱은:',square(4))

#LAB 4-24
s=str(input('여러 단어로 이루어진 글을 입력하세요: '))
s=s.replace('.',' ')
s=s.replace(',',' ')
s=s.replace(':',' ')
s=s.split()
s=sorted(s)
print(s)

#LAB 4-25
s1='Kang Young Min'
s2=' Kang Young-Min'
s3='Park Dong Min'
s4=' Park Dong-Yun'

s1=s1.replace(' ','')
s2=s2.replace(' ','')
s3=s3.replace(' ','')
s4=s4.replace(' ','')
s2=s2.replace('-','')
s4=s4.replace('-','')
s1=s1.upper()
s2=s2.upper()
s3=s3.upper()
s4=s4.upper()

print('Kang Young Min(은)는',s1,'(으)로 수정됨')
print(' Kang Young-Min(은)는',s2,'(으)로 수정됨')
print('Park Dong Min(은)는',s3,'(으)로 수정됨')
print(' Park Dong Yun(은)는',s4,'(으)로 수정됨')
print(s1,':',s1.count('N'),'개의 N이 나타남')
print(s2,':',s2.count('N'),'개의 N이 나타남')
print(s3,':',s3.count('N'),'개의 N이 나타남')
print(s4,':',s4.count('N'),'개의 N이 나타남')

#LAB 4-26
city='Park(Java city), Kim(C city), Kang(Bython city), Lee(Bython city), Hong(Ruby city), Cho(Bython city), Koo(C city), Ryu(C++ city)'
print('주어진 문자열 :',city)
city=city.replace('Bython','Python')
print('수정된 문자열 :',city)
print('Bython 문자열은 모두 {}번 수정했습니다.'.format(city.count('Python')))

#LAB 4-27
def unit_fraction(frac):
    a=1
    while frac<1/a:
        a=a+1
    if abs(frac-1/a)>abs(frac-1/(a-1)):
        # 0.27-0.25 0.02   0.27-0.33333 0.63333
        print('가장 가까운 단위 분수는 1/{}이며, 이 값은 {}입니다.'.format(a-1,1/a-1))
    if abs(frac-1/a)<abs(frac-1/(a-1)):
        print('가장 가까운 단위 분수는 1/{}이며, 이 값은 {}입니다.'.format(a,1/(a)))
        
n=float(input('1보다 작고 0보다 큰 소수를 입력하세요:'))
unit_fraction(n)

#LAB 5-17
animal=['dog','cat','tiger','lion']
print(animal)
animal.append(animal[0])
animal.remove(animal[0])
print(animal)
for w_animal in animal:
    print('I love',w_animal)
    
#LAB 5-18
s_list=['abc','bcd','bcdefg','abba','cddc','opq']
s_list1=sorted(s_list) # ['abba','abc','bcd','bcdefg','cddc','opq']
short=len(s_list1[0])
short_word=s_list1[0]
for i in s_list1:
    if short>len(i):
        short_word=i
        short=len(short_word)
print('가장 길이가 짧은 문자열 :',short_word)

s_list2=s_list[::-1] # ['opq','cddc','bcdefg','bcd','abc','abba']
long=len(s_list2[0])
long_word=s_list2[0]
for j in s_list2:
    if long<len(i):
        long_word=i
        long=len(long_word)
print('가장 길이가 긴 문자열 :',long_word)

s_list.sort(key=len) # ['abc','bcd','opq','abba','cddc','bcdefh']
k=0
s_list3=[]
while len(s_list[k])==len(s_list[k+1]):
    k=k+1
print(k)
print('가장 길이가 짧은 문자열 :',end=' ')
for l in range(0,k+1):
    s_list3.append(s_list[l])
    if l!=k:
        print('\'{}\','.format(s_list[l]),end=' ')
    else:
        print('\'{}\''.format(s_list[l]))
        
#LAB 5-19
s1_list=['abc','bcd','abc','abba','cddc','opq','opq']
new_s1_list=[]
for s1_list_nums in range(0,len(s1_list)):
    if s1_list[s1_list_nums] not in new_s1_list:
        new_s1_list.append(s1_list[s1_list_nums])
print(s1_list)
print(new_s1_list)

#LAB 5-20
src='aaaabbb'
src_list=list(src)
new_src_list=[]
src_count=1
for src_num in range(1,len(src_list)):
    if src_list[src_num]==src_list[src_num-1]:
        src_count+=1
    else:
        new_src_list.append(src_list[src_num-1]+str(src_count))
        src_count=1
new_src_list.append(src_list[-1]+str(src_count))
print('src = \'{}\''.format(src))
print('output = \'{}\''.format(''.join(new_src_list)))

#LAB 5-21
src1='a12b3c6a2c3f1g1'
src1_list =[]
src1_num = 0
while src1_num < len(src1):
    src1_letter = src1[src1_num]
    src1_num += 1
    src1_count = ''
    while src1_num < len(src1) and src1[src1_num].isdigit():
        src1_count += src1[src1_num]
        src1_num += 1
    src1_list.append(src1_letter*int(src1_count))
print('src = \'{}\''.format(src1))
print('output = \'{}\''.format(''.join(src1_list)))

#LAB 5-22
def snake_matrix(n):
    snake_list=[]
    new_snake_list=[]
    for snake_num in range(1,n**2+1):
        snake_list.append(snake_num)
    for snake_ in range(0,n):
        new_snake_list.append(snake_list[snake_*n:snake_*n+n])
    for for_snake in range(n):
        if for_snake%2==0:
            for snake_num in new_snake_list[for_snake]:
                if snake_num<10:
                    print('',snake_num,end=' ')
                else:
                    print(snake_num,end=' ')
            print('')
        if for_snake%2!=0:
            for snake_num in (new_snake_list[for_snake])[::-1]:
                if snake_num<10:
                    print('',snake_num,end=' ')
                else:
                    print(snake_num,end=' ')
            print('')
n=int(input('n을 입력하시오 :'))
snake_matrix(n)

#LAB 5-23
from itertools import count


def how_many_persons(person_list):
    persons_num=0
    for how_many in person_list:
        if type(how_many)==str:
            persons_num+=1
    return persons_num

person1=['온달', 20, 1, 180.0, 100.0]
person2=['이사부', 25, 1, 170.0, 70.0]
person3=['평강', 22, 0, 169.0, 60.0]
person4=['혁거세', 40, 1, 150.0, 50.0]
#(1)
person_list=person1+person2+person4
n_person=how_many_persons(person_list)
print(str(n_person)+'명의 정보가 담겨 있습니다.')
print(person_list)
#(2)
def compute_average_age(person_list):
    age_list=person_list[1::5]
    person_average_age=sum(age_list)/len(age_list)
    return str(person_average_age)

person_list=person1+person2+person3+person4
average_age=compute_average_age(person_list)
print('평균 나이는 ' + str(average_age) +'세입니다.')
#(3)
def count_mals_females(person_list):
    gender_list=person_list[2::5]
    num_male=gender_list.count(1)
    num_female=gender_list.count(0)
    return num_male, num_female

person_list=person1+person2+person3+person4
n_male, n_female= count_mals_females(person_list)
print('리스트에는 남자가',n_male,'명, 여자가',n_female,'명입니다.')
#(4)
def display_persons(person_list):
    divide_persons=[]
    for num_of_person in range(0,len(person_list),5):
        divide_persons.append(person_list[num_of_person:num_of_person+4])
        print(divide_persons[0])
        divide_persons=[]
        
person_list=person1+person2+person3+person4
display_persons(person_list)
