# 학번 2023218074
# 이름 이서연

#4-1
def my_greet():
    print('환영합니다.')
my_greet()
my_greet()

#4-2

def square(n):
    return n**2
print('3의 제곱은 :',square(3))
print('4의 제곱은 :',square(4))

l=input('여러 단어로 이루어진 글을 입력하세요: ').split(' ')
print(sorted(l))

#4-25

s1='Kang Young Min'
s2=' Kang Young-Min'
s3='Park Dong Min'
s4=' Park Dong-Min'

s1_1=s1.replace(' ','')
s2_1=s2.replace('-','')
s2_1=s2_1.replace(' ','')
s3_1=s3.replace(' ','')
s4_1=s4.replace('-','')
s4_1=s4_1.replace(' ','')
s1_1_1=s1_1.upper()
s2_1_1=s2_1.upper()
s3_1_1=s3_1.upper()
s4_1_1=s4_1.upper()

print('Kang Young Min(은)는 ',s1_1_1+'(으)로 수정됨',)
print(' Kang Young-Min(은)는 ',s2_1_1+'(으)로 수정됨')
print('Park Dong Min(은)는 ',s3_1_1+'(으)로 수정됨')
print(' Park Dong-Min(은)는 ',s4_1_1+'(으)로 수정됨')

#4-26
lan=['Park(Java city)','kim(C city)','Kang(Bython city)','lee(Bythoncity)','Hong(Ruby city)','cho(Bython city)','Koo(C city','Ryu(C++ city)']
lan_1=str(lan).replace('[','').replace(']','').replace("'",'')
print('주어진 문자열 :\n',lan_1,'\n')
l=len(lan)
c=0
lan_1=[]
for i in range(l):
    if '(Bython city)' in lan[i]:
        k=lan[i].replace('(Bython city)','(python city)')
        lan_1.append(k)
        c+=1
    else:
        k=lan[i]
        lan_1.append(k)
lan_1=str(lan_1).replace('[','').replace(']','').replace("'",'')
print('변경후 문자열 :\n',lan_1)
print('Bython 문자열은 모두 ',c,'번 수정했습니다.')

#4-27
x=float(input('1보다 작고 0보다 큰 소수를 입력하시오: '))
i=0
k=1

while i<1:
    k+=1
    if x<1/k and x>1/(k+1):
        if (1/k)-x > x-(1/k+1):
            z=k+1
            i=2
        else:
            z=k
            i=2
    else:
        i==0
print('가장 가까운 단위 분수는 1/',z,'이며','이 값은',1/z,'입니다.')

#5-17-1
animals=['dog','cat','tiger','lion']
print('animals = ',animals)
print(animals[1],animals[2],animals[3],animals[0])
#5-17-2
for i in range(4):
    print('I love ',animals[i]+'.')
#5-18-1
s_list=['abc','bcd','bcdefg','abba','opq']
s=s_list[0]

for k in s_list[1:]:
    if len(k) < len(s):
        s = k
    elif len(k) == len(s) and k < s:
        s = k
print('가장 길이가 짧은 문자열 : ',s)
#5-18-2
s_list=['abc','bcd','bcdefg','abba','opq']
s=s_list[0]

for k in s_list[1:]:
    if len(k) > len(s):
        s = k
    elif len(k) == len(s) and k > s:
        s = k
print('가장 길이가 긴 문자열 :',s )

#5-18-3
s_list=['abc','bcd','bcdefg','abba','opq']
s=s_list[0]
a=len(s_list)
y=[]
q=s_list
for k in s_list[1:]:
    if len(k) < len(s):
        s = k
    elif len(k) == len(s) and k < s:
        s = k
z=len(s)
for i in range(a):
    if len(q[i])==z:
        y.append(q[i])
y=str(y).replace('[','').replace(']','')
print('가장 길이가 짧은 문자열 : ',y)
#5-19
s_list=['abc','bcd','abc','abba','cddc','opq','opq']
new_s_list=[]
new_s_list.append(s_list[0])
x=len(s_list) #x=7

print('s_list = ',s_list)

for i in range(1,x):
    for j in range(i):
        if new_s_list[j-1]==s_list[i]:
            break
        elif new_s_list[j]!=s_list[i]:
            s=s_list[i]
            new_s_list.append(s)
            break

print('new_s_list =',new_s_list )

#5-20
s1=input('src = ')
k=[]
if not s1 :
    compressed=''
else:
    compressed=''
    count=1
    for i in range(1,len(s1)):
        if s1[i]==s1[i-1]:
            count+=1
        else:
            compressed+=s1[i-1]+str(count)
            count=1
    compressed+=s1[-1]+str(count)
k.append(compressed)
k=str(k)[1:-1]
print('output = ',k)
#5-21
src=input(('src = '))
x=len(src)
output=[]

for i in range(0,x,2):
    if src[i+1]==1:
        z=src[i]
        output.append(z)
    else:
        a=src[i]
        b=int(src[i+1])
        z=a*b
        output.append(z)
output=list(output)
print("".join(output))

#5-22
n=int(input('n을 입력하시오 : '))

num=[]
s=[]
for i in range(1,n**2+1):
    num.append(i)

for i in range(n):
    if i==0:
        x = num[n * i:n * (i + 1)]
        x= str(x).replace('[','').replace(']',"").replace(',','')
        print(x.rjust(3))
    elif i%2==1:
        x=num[n*i:n*(i+1)]
        x.sort(reverse=True)
        x = str(x).replace('[', '').replace(']', "").replace(',', '')
        print(x.rjust(3))
    elif i%2==0:
        x = num[n * i:n * (i + 1)]
        x = str(x).replace('[', '').replace(']', "").replace(',', '')
        print(x.rjust(3))

#5-23-1

person1=['온달',20,1,180.0,100.0]
person2=['이사부',25,1,170.0,70.0]
person3=['평강',22,0,169.0,60.0]
person4=['혁거세',40,1,150.0,50.0]

person_list=person1+person3+person4
def how_many_persons(person_list):
    x=len(person_list)
    return int(x/5)
n_persons=how_many_persons(person_list)
print(str(n_persons)+'명의 정보가 담겨 있습니다.')

#5-23-2
person_list=person1+person2+person3+person4
x=len(person_list)/5
age=0
x=int(x)
def compute_average_age(person_list):
    pl_age=0
    for i in range(x):
        age=person_list[1+(5*i)]
        age=float(age)
        pl_age=pl_age+age
    return float(pl_age)/4
average_age=compute_average_age(person_list)
print('평군 나이는 '+str(average_age)+'세입니다.')

#5-23-3

def count_males_females(person_list):
    female=0
    male=0
    for i in range(x):
        n=person_list[2+(5*i)]
    if n==1:
        male+=1
    elif n==0:
        female+=1
    return male,female
n_male,n_female=count_males_females(person_list)

#5-23-4
print('리스트에는 남자가',n_male,'명, 여자가',n_female,'명입니다.')

def display_preson(person_list):
    for i in range(4):
        if i==0:
            x=person_list[i:5]
            print(x)
        else:
            x=person_list[5*i:5*(i+1)]
            print(x)
display_preson(person_list)
