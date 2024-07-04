# 학번 2023218090
# 이름 임상환

#2-1

print('Hello world!')
print('Today is ', 3,'/',19)
print('1 plus 1 equals to ', 1+1,'\n')

#2-2

print('Potato pizza 5: ', 15000*5)
print('Steak pizza 2: ', 25000*2)
print('Total: ', (15000*5+25000*2)*(1+0.1), '\n')

#2-3

price_potato_pizza = 15000
price_steak_pizza = 25000
price_potato_pizza_total = price_potato_pizza * 5
price_steak_pizza_total = price_steak_pizza * 2
price_total = ((price_potato_pizza_total + price_steak_pizza_total) * (1 + 0.10))

print("Potato pizza 5: ", price_potato_pizza_total, "\nSteak pizza 2: ", price_steak_pizza_total, "\nTotal: ", price_total)

price_potato_pizza = (price_potato_pizza * (1 - 0.30))
price_potato_pizza_total = price_potato_pizza * 5
price_total = ((price_potato_pizza_total + price_steak_pizza_total) * (1 + 0.10))
print( "Potato pizza 5: ", price_potato_pizza_total, "\nSteak pizza 2: ", price_steak_pizza_total, "\nTotal: ", price_total)

price_total =(price_total * (1 - 0.20));
print("Potato pizza 5: ", price_potato_pizza_total, "\nSteak pizza 2: ", price_steak_pizza_total, "\nTotal: ", price_total)
#2-4

name_potato_pizza = "Potato pizza"
name_steak_pizza = "Steak pizza",
name_total = "Total";
amount_potato_pizza = 5
amount_steak_pizza = 2
print(name_potato_pizza, " ", amount_potato_pizza, ": ", price_potato_pizza_total, "\n", name_steak_pizza, " ", amount_steak_pizza, ": ", price_potato_pizza_total, "\n", name_total, ": ", price_total, "\n"); 

#2-5

true = 1
print(true, '\n')

name_steaky_pizza = 'Steaky pizza'
print(name_steaky_pizza, '\n')

order_number = 251
print('your order number is ', order_number,'.', '\n')

reciept = 'Total: 10,000 won'
print(reciept, '\n')

price = 10000
amount = 2
tax = 0.1
price_total_with_tax = price * amount + (price * amount * tax)
print(price_total_with_tax, '\n')

price_with_tax= 10000+(10000*0.1)
print(price_with_tax, '\n')

#2-6

num=0
result=0
num=1
result=result+num
print(result, '\n')

#2-7

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
num_right= 5
result=num_left%num_right
print(result)

num_left=6
num_right=5
result=num_left//num_right
print(result)

num_left=6
num_right=5
result=num_left/num_right
print(result, '\n')

#2-8

x=1.0+1j
y=1.0+1j
print(x+y,x-y,x*y,x/y,'\n')

#2-9

num_2s = 64
print(num_2s>>1, ' ',num_2s>>6, ' ',num_2s>>10, ' ', num_2s>>24, ' ',num_2s>>25, ' ',num_2s>>26, '\n')

#2-10

input_str=input()
print('input string: ', input_str)
