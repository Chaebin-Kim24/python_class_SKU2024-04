# 학번 2023218055
# 이름 사서연

#LAB 2-1
print('Hello World!')
month,day=3,13
print('Today is',month,'/',day,'.\n')
print('1 plus 1 equals to {1+1}')

#LAB 2-2
Potato_pizza,Steak_pizza=15000,25000
print('Potato pizza 5:',(Potato_pizza*5))
print('Steak pizza 2:',(Steak_pizza*2))
print('Total:',(Potato_pizza*5+Steak_pizza*2)*(1+0.10))

#LAB 2-3
price_potato_pizza,price_steak_pizza=15000,25000
price_potato_pizza_total=price_potato_pizza*5
price_steak_pizza_total=price_steak_pizza*2
price_total=(price_potato_pizza_total+price_steak_pizza_total)*(1+0.10)
print(price_total)

#LAB 2-3-1
print('Potato_pizza 5:',price_potato_pizza_total)
print('Steak pizza 5:',price_steak_pizza_total)
print('Total:',price_total)

#LAB 2-3-2
price_potato_pizza=price_potato_pizza*(1-0.30)
price_potato_pizza_total=price_potato_pizza*5
price_total=(price_potato_pizza_total+price_steak_pizza_total)*(1+0.10)
print(price_potato_pizza,price_steak_pizza,price_total)

#LAB 2-3-3
price_total=price_total*(1-0.20)
print('Potato pizza 5:',price_potato_pizza_total)
print('Steak pizza 2:',price_steak_pizza_total)
print('Total:',price_total)

#LAB 2-4
name_potato_pizza='Poato pizza'
name_steak_pizza='Steak pizza'
name_total='Total'
amount_potato_pizza,amount_steak_pizza=5,2
print(name_potato_pizza,' ',amount_potato_pizza,':',price_potato_pizza_total)
print(name_steak_pizza,' ',amount_steak_pizza,':',price_steak_pizza_total)
print(name_total,':',price_total)

#LAB 2-5-1
print('LAB 2-5')
true=1
print(true)

#LAB 2-5-2
print('LAB 2-5-2')
name_steaky_pizza='Steaky pizza'
print(name_steaky_pizza)

#LAB 2-5-3
abcdefghijklmnop=251
print('Your order number is ',abcdefghijklmnop,'.')
order_num=251
print('Your order number is',order_num,'.')

#LAB 2-5-4
pizza_delivery_reciept_string_for_this_pizza_order='Total: 10,000 won'
print('pizza_delivery_reciept_string_for_this_pizza_order')
reciept='Total: 10,000 won'
print(reciept)

#LAB 2-5-5
price=10000
amount=2
tax=0.1
price_total_without_tax=price*amount+(price*amount*tax)
print(price_total_without_tax)

#LAB 2-5-6
price_tax=10000+10000*0.10
print(price_tax)
price_with_tax=(10000+10000*0.10)
print(price_with_tax)

#LAB 2-6
num,result=0,0
num=1
result=result+num
print(result)

#LAB 2-7
result=0
num_left=6
num_right=6
result=num_left*num_right
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

#LAB 2-8
x=1.0+1j
y=1.0+1j
print(x+y,x-y,x*y,x/y)

#LAB 2-9
x=1.0+1j
y=1.0+1j
print(x+y,x-y,x*y,x/y)

#LAB 2-10
print(input('please type any characters:'))
