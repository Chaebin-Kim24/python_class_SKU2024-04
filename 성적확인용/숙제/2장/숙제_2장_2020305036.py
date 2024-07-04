# 학번 2020305036
# 이름 원종인

#LAB 2-1
print('LAB 2-1')
print('Hello World')
print('Todaty is 3 / 15')
print('1 plus 1 equals to', 1+1)

#LAB 2-2
print('LAB 2-2')
print('Potato pizza 5 :',15000 * 5,'\nSteak pizza 2 :',25000*2,'\nTotal', (int)((15000*5+25000*2)*1.1))

#LAB 2-3
print('LAB 2-3-1')
price_potato_pizza = 15000
price_steak_pizza = 25000
price_potato_pizza_total = price_potato_pizza * 5
price_steak_pizza_total = price_steak_pizza * 2
price_total = (int)((price_potato_pizza_total + price_steak_pizza_total) * 1.1)
print('Potato pizza 5 :',price_potato_pizza_total,'\nSteak pizza 2 :',price_steak_pizza_total,'\nTotal', price_total)

print('LAB 2-3-2')
price_potato_pizza_total = (int)(price_potato_pizza_total * 0.7)
price_total = (int)((price_potato_pizza_total + price_steak_pizza_total) * 1.1)
print('Potato pizza 5 :',price_potato_pizza_total,'\nSteak pizza 2 :',price_steak_pizza_total,'\nTotal', price_total)

print('LAB 2-3-3')
price_total = (int)(price_total * 0.8)
print('Potato pizza 5 :',price_potato_pizza_total,'\nSteak pizza 2 :',price_steak_pizza_total,'\nTotal', price_total)

#LAB 2-4
print('LAB 2-4')
name_potato_pizza = 'Potato pizza'
name_steak_pizza = 'Steak pizza'
name_total = 'Total'
amount_potato_pizza = 5
amount_steak_pizza = 2
print(name_potato_pizza, amount_potato_pizza,':',price_potato_pizza_total)
print(name_steak_pizza, amount_steak_pizza,':',price_steak_pizza_total)
print(name_total, price_total)

#LAB 2-5
print('LAB 2-5-1')
true = 1;
print(true)
print()

print('LAB 2-5-2')
name_steaky_pizza = 'steaky pizza'
print(name_steaky_pizza)
print()

print('LAB 2-5-3')
order_number = 251
print('your order number is',order_number)
print()

print('LAB 2-5-4')
reciept = "Total: 10,000 won"
print(reciept)
print()

print('LAB 2-5-5')
price = 10000;
amount = 2;
tax = 0.1;
price_total_with_tax = price * amount + (int) (price * amount * tax);
print(price_total_with_tax)
print()

print('LAB 2-5-6')
price_with_tax = 10000 + 10000 * 0.10;
print(price_with_tax)
print()

#lab 2-6
print('LAB 2-6')
num, result = 0, 0
num = 1
result += num
print(result)
print()

#lab 2-7
print('LAB 2-7')
result = 0
num_left = 6
num_right = 6
result = num_left * num_right
print(result)
print()

num_left = result
num_right = 0.5
result = num_left ** num_right
print(result)
print()

num_left = result
num_right = 5
result = num_left % num_right
print(result)
print()

num_left = 6
num_right = 5
result = num_left // num_right
print(result )
 
num_left = 6
num_right = 5
result = num_left / num_right
print (result)

#LAB 2-8
print('LAB 2-8')
print((1 + 1j) + (1 + 1j), (1 + 1j) - (1 + 1j), (1 + 1j) * (1 + 1j), (1 + 1j) / (1 + 1j))

#LAB 2-9
print('LAB 2-9')
num_2s = 64
print(num_2s >> 1, num_2s>>6, num_2s>>10, num_2s <<1, num_2s<<6, num_2s<<10)

#LAB 2-10
print('LAB 2-10')
input_str = 'input string: ' + input('문자열 입력 : ')
print(input_str)
