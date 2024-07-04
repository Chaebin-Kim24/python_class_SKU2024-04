# 학번 2023218002
# 이름 고서연

# LAB 2-1
print('Hello World!')
print('Today is', 3, '/', 19,  '.')
print('1 plus 1 equals to', 1+1)

# LAB 2-2
print('Potato pizza 5:', 15000*5)
print('Steak pizza 2:', 25000*2)

# LAB 2-3-1
price_potato_pizza, price_steak_pizza = 15000,25000
price_potato_pizza_total=price_potato_pizza*5
print(price_potato_pizza_total)
price_steak_pizza_total=price_steak_pizza*2
print(price_steak_pizza_total)
print_total=(price_potato_pizza_total+price_steak_pizza_total)*(1.1)
print(print_total)

# LAB 2-3-2
price_potato_pizza=price_potato_pizza*(1-0.30)
print(price_potato_pizza)
price_potato_pizza_total=price_potato_pizza*5
print(price_potato_pizza_total)
price_total=(price_potato_pizza_total+price_steak_pizza_total)*(1+0.10)
print(price_total)
print('Potato pizza 5:', price_potato_pizza_total,'\n', 'Steak pizza 2:', price_steak_pizza_total, '\n', 'Total:', price_total)

# LAB 2-3-3
price_total=price_total*(1-0.20)
print('Potato pizza 5:',price_potato_pizza_total,'\n','Steak pizza 2:',price_steak_pizza_total,'\n','Total:',price_total)

# LAB 2-4
name_potato_pizza='Potato pizza'
name_steak_pizza='Steak pizza'
name_total='Total'
amount_potato_pizza,amount_steak_pizza=5,2
print(name_potato_pizza,' ',amount_potato_pizza,':',price_potato_pizza_total,'\n',name_steak_pizza,' ',amount_steak_pizza,':',price_steak_pizza_total,'\n',name_total,':',price_total)

# LAB 2-5
print('LAB 2-5-1')
print(True)
print('LAB 2-5-2')
name_steaky_pizza='Steaky pizza'
print(name_steaky_pizza)
print('LAB 2-5-3')
order_num=251
print('Your order number is',order_num,'.')
print('LAB 2-5-4')
reciept='Total: 10,000 won'
print(reciept)
print('LAB 2-5-5')
price,amount,tax=10000,2,0.1
price_total_with_tax=price*amount+(price*amount*tax)
print(price_total_with_tax)
print('LAB 2-5-6')
price_with_tax=(10000+10000*0.10)
print(price_with_tax)

#LAB 2-6
print('LAB 2-6')
num,result=0,0
num=1
result=result+num
print(num)

#LAB 2-7
print('LAB 2-7')
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
print('LAB 2-8')
x=1.0+1j
y=1.0+1j
print(x+y,x-y,x*y,x/y)

#LAB 2-9
print('LAB 2-9')
num_2s=64
print(num_2s>>1,' ',num_2s>>6,' ',num_2s>>10,' ',num_2s<<24,' ',num_2s<<25,' ',num_2s<<26)

#LAB 2-10
print('LAB 2-10')
print(input('이름을 입력하세요 : '))

