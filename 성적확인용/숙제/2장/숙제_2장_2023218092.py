# 학번: 2023218092
# 이름: 임정호

#2장
#2-1번 여러 자료형의 값을 화면에 출력하기
print('2-1')

print('Hello World')
print("/////////////////////////////////////")
print('')

month=3
day=14

print("오늘의 날짜는 ",month,"월 ",day,"일 입니다")
print("/////////////////////////////////////")
print('')
print("1+1=",1+1)
print("/////////////////////////////////////")
print('')

#2-2 영수증 계산하기 
#주어진 메뉴판에서 포테이토 피자 5판과 스테이크 피자 2판의 가격
#부가세 10%가 더해진 총 금액을 다음과 같은 형식으로 출력합니다.
#=====메뉴판====
#포테이토 피자  15,000
#스테이크 피자  25,000
print('2-2')

print('포테이토 피자 5판:',15000*5)
print('스테이크 피자 2판: ',25000*2)
print('총 가격: ',(15000*5+25000*2)*1.1)
print("/////////////////////////////////////")
print('')

#2-3 변수를 써서 영수증 계산하기
print('2-3')

price_potato_pizza=15000
price_steak_pizza=25000

price_potato_pizza_total=15000*5
price_steak_pizza_total=25000*2
price_total=(price_potato_pizza_total+price_steak_pizza_total)*1.1

print('포테이토 피자 5판: ',price_potato_pizza_total)
print('스테이크 피자 5판: ',price_steak_pizza_total)
print('총 가격: ',price_total)
print("/////////////////////////////////////")
print('')

#2-3 변수를 써서 2-2와 같이 영수증을 출력합니다.
print('2-3-1')

print('포테이토 피자 5판:',price_potato_pizza*5,' \n스테이크 피자 2판:',price_steak_pizza*2,'\n총 가격: ',price_total)
print("/////////////////////////////////////")
print('')

#2-4번 포테이토 피자의 가격을 30%할인 받았을때, 영수증의 포테이토 피자 5판의 괍과 전체 값을 변경하여 출력합니다.
print('2-3-2')

price_potato_pizza=price_potato_pizza*0.7
price_total=(price_potato_pizza_total+price_steak_pizza_total)*1.1

print('포테이토 피자 5판:',price_potato_pizza*5,' \n스테이크 피자 2판:',price_steak_pizza*2,'\n총 가격: ',price_total)
print("/////////////////////////////////////")
print('')
#2-4번 추가로 총 금액에서 20%할인 받은 경우에, 영수증의 총가격을 변경하여 출력
print('2-3-3')

price_total=price_total*0.8

print('포테이토 피자 5판:',price_potato_pizza*5,' 스테이크 피자 2판:',price_steak_pizza*2,'총 가격: ',price_total)
print("/////////////////////////////////////")
#2-4번 여러 자료형의 변수를 써서 영수증 출력하기
print('2-4')

name_potato_pizza='포테이토 피자'
name_steak_pizza= '스테이크 피자'
name_total='총 가격'
amount_potato_pizza=5
amount_steak_pizza=2

print(name_potato_pizza,' 판',amount_potato_pizza,': ',price_potato_pizza)
print(name_steak_pizza,' 판',amount_steak_pizza,': ',price_steak_pizza)
print(name_total,': ',price_total)
print("/////////////////////////////////////")
print('')

#2-5 변수 이름의 오류 찾기
print('2-5')
print("/////////////////////////////////////")
print('')

#2-5-1  변수 이름으로 파이썬에서 키워드로 지정된 단어를 썼을 때 
print('2-5-1')

true_1=1

print(true_1)
print("/////////////////////////////////////")
print('')

print('2-5-2')

name_steak_pizza="stake_pizza"

print(name_steak_pizza)
print("/////////////////////////////////////")
print('')

print('2-5-3')

order_num=251

print('너의 주문 번호는 ',order_num,'이다.')
print("/////////////////////////////////////")
print('')

print('2-5-4')

reciept="총: 10,000원"

print(reciept)
print("/////////////////////////////////////")
print('')

print('2-5-5')

price=10000
amount=2
tax=0.1
price_total_with_tax=price*amount+price*amount*tax

print(price_total_with_tax)
print("/////////////////////////////////////")
print('')

print('2-5-6')

price_with_tax=10000+1000*0.1

print(price_with_tax)
print("/////////////////////////////////////")
print('')

#2-6 변수 값을 다시 저장하기
print('2-6')

num=0
result=0
num=1
result=result+num

print(result)
print("/////////////////////////////////////")
print('')


#2-7 산술 연산자 사용

print('2-7')

result=0
num_left=6
num_right=6
result=num_left+num_right

print(result)

num_left=result
num_right=0.5
result=pow(num_left,num_right)

print(result)

num_left=result
num_right=5
result=num_left%num_right

print(result)

num_left=6
num_right=5
result=num_left/num_right

print(result)
num_left=6
num_right=5
result=num_left/num_right

print(result)

print("/////////////////////////////////////")
print('')

#2-8 복소수 연산 해보기

print('2-8')

x=1+1j
y=1+1j

print(x+y,x-y,x*y,x/y)
print("/////////////////////////////////////")
print('')

#2-9 비트 연산 해보기

print('2-9')

num_2s=64

print((num_2s >> 1) ,(num_2s >> 6) , (num_2s >> 10) , (num_2s << 24) , (num_2s << 25) , (num_2s << 26))

print("/////////////////////////////////////")
print('')
#2-10 키보드 입력

print('2-10')

print(input('단어를 입력하시오: '))
