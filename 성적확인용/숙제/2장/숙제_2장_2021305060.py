# 학번: 2021305060
# 이름: 이종희

print('Hello World!')
#LAB 2-1

print('Potato pizza 5:',15000*5,'Steak pizza 2:',25000*2,'Total:',15000*5+25000*2)
#LAB 2-2

price_potato_pizza,price_steak_pizza=15000,25000
price_potato_pizza_total=price_potato_pizza*5
price_steak_pizza_total=price_steak_pizza*2
price_total=(price_potato_pizza_total+price_steak_pizza_total)*(1+0.1)
#LAB 2-3

print('Potato pizza 5:',price_potato_pizza_total,'Steak pizza 2:',price_steak_pizza_total,'Total:',price_total)
#LAB 2-3-1

price_potato_pizza=price_potato_pizza*(1-0.3)
price_potato_pizza_total=price_potato_pizza*5
price_total=(price_potato_pizza_total+price_steak_pizza_total)*(1+0.1)
print('Potato pizza 5:',price_potato_pizza_total,'Steak pizza 2:',price_steak_pizza_total,'Total:',price_total)
#LAB 2-3-2

price_total=price_total*(1-0.2)
print('Potato pizza 5:',price_potato_pizza_total,'Steak pizza 2:',price_steak_pizza_total,'Total:',price_total)
#LAB 2-3-3

name_potato_pizza,name_steak_pizza="Potato Pizza","Steak pizza"
total="Total"
amount_potato_pizza,amount_steak_pizza=5,2
print(name_potato_pizza,amount_potato_pizza,':',price_potato_pizza_total,name_steak_pizza,amount_steak_pizza,':',price_steak_pizza_total,total,':',price_total)
#LAB 2-4

true=1
print(true)
#LAB 2-5-1

name_steaky_pizza="Steaky Pizza"
print(name_steaky_pizza)
#LAB 2-5-2

abcdefghijklmnop=251
order_num=abcdefghijklmnop
print('Your number is',order_num)
#LAB 2-5-3

pizza_delivery_reciept_string_for_this_pizza_order="Total: 10,000 won"
reciept=pizza_delivery_reciept_string_for_this_pizza_order
print(reciept)
#LAB 2-5-4

price=10000
amount=2
tax=0.1
price_total_with_tax=price*amount-price*amount*tax
print(price_total_with_tax)
#LAB 2-5-5

price_with_tax=10000+10000*0.1
print(price_with_tax)
#LAB 2-5-6

num,result=0,0
num=1
result=result+num
print(result)
#LAB 2-6

result=0
num_left=6
num_right=6
result=num_left*num_right
print(result)
num_left=result
num_right=0.5
result=num_left**num_right
print(result)
num_left=result
num_right=5
result=num_left%num_right
print(result)
num_left=6
num_right=5
result=num_left/num_right
print(result)
#LAB 2-7

print((1+1j)+(1+1j),(1+1j)-(1+1j),(1+1j)*(1+1j),(1+1j)/(1+1j))
#LAB 2-8

num_2s=64
print(num_2s>>1,num_2s>>6,num_2s>>10,num_2s<<1,num_2s<<6,num_2s<<10)
#LAB 2-9

input_str=input()
print("input string: ",input_str)
