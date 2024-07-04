# 학번 2020305015
# 이름 김주영

# LAB 2-1
print('Hello World')
print('"Today is',3,'/',13,'"')
print('"1 plus 1 equals to',1+1,'"') 

# LAB 2-2
print('"""\n Potato pizza 5:',15000*5,'\n','Steak 2:',25000*2,'\n','Total:',(15000*5+25000*2)*(1+0.1),'\n','"""')

# LAB 2-3
# 1.
price_potato_pizza =15000
price_steak_pizza = 25000
price_potato_pizza_total = price_potato_pizza * 5
price_steak_pizza_total =price_steak_pizza * 2
price_total =(price_potato_pizza_total + price_steak_pizza_total) * (1 + 0.10)
print('"Potato pizza 5:',price_potato_pizza_total,'Steak 2:',price_steak_pizza_total,'Total:',price_total,'"\n')
# 2.
price_potato_pizza =price_potato_pizza =15000
price_steak_pizza = 25000
price_potato_pizza_total = price_potato_pizza * 5
price_steak_pizza_total =price_steak_pizza * 2
price_total =(price_potato_pizza_total + price_steak_pizza_total) * (1 + 0.10)
print('"Potato pizza 5:',price_potato_pizza_total,'Steak 2:',price_steak_pizza_total,'Total:',price_total,'"\n')
price_potato_pizza =price_potato_pizza * (1 - 0.30)
price_potato_pizza_total = price_potato_pizza * 5
price_total = (price_potato_pizza_total + price_steak_pizza_total) * (1 + 0.10)
print('"Potato pizza 5:',price_potato_pizza_total,'Steak 2:',price_steak_pizza_total,'Discount Total:',price_total,'"\n')
# 3.
price_potato_pizza =15000
price_steak_pizza = 25000
price_potato_pizza_total = price_potato_pizza * 5
price_steak_pizza_total =price_steak_pizza * 2
price_total =(price_potato_pizza_total + price_steak_pizza_total) * (1 + 0.10)
print('"Potato pizza 5:',price_potato_pizza_total,'Steak 2:',price_steak_pizza_total,'Total:',price_total,'"\n')
price_potato_pizza =price_potato_pizza * (1 - 0.30)
price_potato_pizza_total = price_potato_pizza * 5
price_total = (price_potato_pizza_total + price_steak_pizza_total) * (1 + 0.10)
print('"Potato pizza 5:',price_potato_pizza_total,'Steak 2:',price_steak_pizza_total,'Discount Total:',price_total,'"\n')
price_total = price_total * (1 - 0.20)
print('"Potato pizza 5:',price_potato_pizza_total,'Steak 2:',price_steak_pizza_total,'Discount Total 2:',price_total,'"\n')

# LAB 2-4
price_potato_pizza =price_potato_pizza =15000
price_steak_pizza = 25000
price_potato_pizza_total = price_potato_pizza * 5
price_steak_pizza_total =price_steak_pizza * 2
price_total =(price_potato_pizza_total + price_steak_pizza_total)
name_potato_pizza="Potato pizza"
name_steak_pizza="Steak pizza"
name_total= "Total"
amount_potato_pizza=5
amount_steak_pizza=2
print(name_potato_pizza,':',amount_potato_pizza,',',name_steak_pizza, ':',amount_steak_pizza,',',name_total,':',price_total)

# LAB 2-5
# 1.
true=1
print(true)
# 2.
name_steaky_pizza = "Steaky pizza"
print(name_steaky_pizza)
# 3.
order_num = 251
print('Your order number is ',order_num ,'.')
# 4.
reciept = "Total: 10,000 won"
print(reciept)

# 5.
price = 10000
amount = 2
tax = 0.1
price_total_with_tax = price * amount + (price * amount * tax)
print(price_total_with_tax)

# 6.
price_with_tax = 10000 + 10000 * 0.10
print(price_with_tax)

# LAB 2-6
num = 0
result = 0
num = 1
result = result + num
print(result)

# LAB 2-7
result = 0
num_left=6
num_right=6
result=num_left * num_right
num_left=result
num_right=0.5
result=num_left % num_right
num_left=6
num_right=5
result=num_left / num_right
print(result)

# LAB 2-8
x = complex(1,1)
y = complex(1.1)

print(x+y)
print(x-y)
print(x*y)
print(x/y)

# LAB 2-9
num_2s=64
print(num_2s >> 1)
print(num_2s >> 6)
print(num_2s >> 10)
print(num_2s << 24)
print(num_2s << 25)
print(num_2s << 26)

# LAB 2-10
print('값을 입력하세요:')
input_str=input()
print('input string:',input_str)
