# 학번 2023218092
# 이름 임정호

#1
n=int(input('n을 입력하시오 : '))
a=[]
b=[]
c=[]
d=[]
p=1
z=n
for i in range(n):
    if i%2==0:
        for k in range(z):
            a.append(p)
            p+=1
        print(*a)
        a.clear()
    elif i%2==1:
        u=(p-1)*2
        for k in range(z):
            b.append(u-k)
            p+=1
        print(*b)
        b.clear()

#5
x=int(input('주민등록번호 첫 6숫자 형식 입력'))


year=x//10000
month=(x%10000)//100
day=x%100
if x>25:
    print(1900+year,'년',month,'월',day,'일')
else:
    print(2000+year,'년',month,'월',day,'일')






