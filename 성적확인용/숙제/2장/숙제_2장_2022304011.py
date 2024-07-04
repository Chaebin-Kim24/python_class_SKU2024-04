# 학번: 2022304011
# 이름: 김수연

#LAB 2-1
print('heloo world')

print('오늘의 날짜는',3,'월',20,'일 입니다')

print('1+1=',1+1)

#LAB 2-2
print('포테이토 피자 5판:',15000*5)
print('스테이크 피자 2판:',25000*2)
print('총 가격:',(75000+50000)*1.1)

#LAB 2-3-1
price_potato_pizza_total=15000*5
print('포테이토 피자 5판:',price_potato_pizza_total)
price_steak_pizza_total=25000*2
print('스테이크 피자 2판:',price_steak_pizza_total)
price_total=(price_potato_pizza_total+price_steak_pizza_total)*1.1
print('총 가격:',price_total)

#LAB 2-3-2
print('포테이토 피자 5판:',price_potato_pizza_total,'/n스테이크 피자 2판;',price_steak_pizza_total,'/n총 가격:',price_total)

#LAB 2-3-3
price_potato_pizza=15000
price_seak_pizza=25000
price_potato_pizza=price_potato_pizza*0.7
price_steak_pizza=25000
price_total=(price_potato_pizza_total+price_steak_pizza_total)*1.1
price_total=(price_potato_pizza_total+price_steak_pizza_total)*1.1
print('포테이토 피자 5판:',price_potato_pizza*5,'/n스테이크 피자2판',price_steak_pizza*2,'/n총 가격:',price_total)
price_total=price_total*0.8
print('포테이토 피자 5판:',price_potato_pizza*5,' 스테이크 피자 2판:',price_steak_pizza*2,'총 가격:',price_total)

#LAB 2-4
name_potato_pizza='포테이토 피자'
name_total='총 가격'
name_steak_pizza='스테이크 피자'
amount_steak_pizza=5
amount_potato_pizza=2
print(name_potato_pizza,'판',amount_potato_pizza,':',price_potato_pizza)

print(name_steak_pizza,' 판',amount_steak_pizza,': ',price_steak_pizza)

print(name_total,': ',price_total)

#LAB 2-5-1
true_1=1
print(true_1)

#LAB 2-5-2
name_steak_pizza="stake_pizza"
print(name_steak_pizza)

#LAB 2-5-3
order_num=251
print('너의 주문 번호는 ',order_num,'이다.')

#LAB 2-5-4
reciept="총: 10,000원"
print(reciept)

#LAB 2-5-5
price=10000
amount=2
tax=0.1
price_total_with_tax=price*amount+price*amount*tax
print(price_total_with_tax)

#LAB 2-5-6
price_with_tax=10000+1000*0.1
print(price_with_tax)

#LAB 2-6
num=0
result=0
num=1
result=result+num
print(result)

#LAB 2-7
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
result=num_left/num_right
print(result)

num_left=6
num_right=5
result=num_left/num_right
print(result)

#LAB 2-8
x=1+1j
y=1+1j
print(x+y,x-y,x*y,x/y)

#LAB 2-9
num_2s=64
print((num_2s >> 1) ,(num_2s >> 6) , (num_2s >> 10) , (num_2s << 24) , (num_2s << 25) , (num_2s << 26))
