# 학번: 2021304054
# 이름: 윤종서


# lab2_1
print("Hello World!")
print("Today is ", 3, 13)
print("1 plus 1 equals to ", 1 + 1);


# lab2_2
print("Potato pizza 5:", 15000 * 5)
print("Steak pizza 2:", 25000 * 2)
print('Total:', (15000 * 5 + 25000 * 2) * (1 + 0.10))


# lab2_3
price_potato_pizza = 15000
price_steak_pizza = 25000
price_potato_pizza_total = price_potato_pizza * 5
price_steak_pizza_total = price_steak_pizza * 2
price_total = ((price_potato_pizza_total + price_steak_pizza_total) * (1 + 0.10))
print("Potato pizza 5:", price_potato_pizza_total)
print("Steak pizza 2:", price_steak_pizza_total)
print('Total:', price_total)

# lab2_3_1
price_potato_pizza = 15000
price_steak_pizza = 25000
price_potato_pizza_total = price_potato_pizza * 5
price_steak_pizza_total = price_steak_pizza * 2
price_total = ((price_potato_pizza_total + price_steak_pizza_total) * (1 + 0.10))
print("Potato pizza 5:", price_potato_pizza_total)
print("Steak pizza 2:", price_steak_pizza_total)
print('Total:', price_total)

# lab2_3_2
price_potato_pizza = 15000
price_steak_pizza = 25000
price_potato_pizza = (price_potato_pizza * (1 - 0.30))
price_potato_pizza_total = price_potato_pizza * 5
price_steak_pizza_total = price_steak_pizza * 2
price_total = ((price_potato_pizza_total + price_steak_pizza_total) * (1 + 0.10))
print("Potato pizza 5:", price_potato_pizza_total)
print("Steak pizza 2:", price_steak_pizza_total)
print('Total:', price_total)

# lab2_3_3
price_potato_pizza = 15000
price_steak_pizza = 25000
price_potato_pizza = (price_potato_pizza * (1 - 0.30))
price_potato_pizza_total = price_potato_pizza * 5
price_steak_pizza_total = price_steak_pizza * 2
price_total = ((price_potato_pizza_total + price_steak_pizza_total) * (1 + 0.10))
price_total = (price_total * (1 - 0.20))
print("Potato pizza 5:", price_potato_pizza_total)
print("Steak pizza 2:", price_steak_pizza_total)
print('Total:', price_total)


# lab2_4
name_potato_pizza = 'Potato pizza' 
name_steak_pizza = 'Steak pizza'
name_total = 'Total'

amount_potato_pizza = 5
amount_steak_pizza = 2

price_potato_pizza = 15000
price_steak_pizza = 25000
price_potato_pizza = (price_potato_pizza * (1 - 0.30))
price_potato_pizza_total = price_potato_pizza * 5
price_steak_pizza_total = price_steak_pizza * 2
price_total = ((price_potato_pizza_total + price_steak_pizza_total) * (1 + 0.10))
price_total = (price_total * (1 - 0.20))
print(name_potato_pizza, amount_potato_pizza,':', price_potato_pizza_total)
print(name_steak_pizza, amount_steak_pizza,':', price_steak_pizza_total)
print(name_total, price_total)


# lab2_5_1
apple = 1
print(apple)

# lab2_5_2
name_steaky_pizza = 'Steaky pizza'
print(name_steaky_pizza)

# lab2_5_3
order_num = 251
print("Your order number is ", order_num)

# lab2_5_4
reciept = "Total: 10,000 won"
print(reciept)

# lab2_5_5
price = 10000
amount = 2
tax = 0.1 
price_total_with_tax = price * amount + (price * amount * tax)
print(price_total_with_tax)

# lab2_5_6
price_with_tax = (int)(10000 + 10000 * 0.10)
print(price_with_tax)


# lab2_6
num = 0 
result = 0
num = 1
result = result + num
print(result)


# lab2_7
result = 0
num_left = 6
num_right = 6
result = num_left * num_right
print(result)

num_left = result
num_right = 0.5
result = pow(num_left, num_right)
print(result)

num_left = result
num_right = 5
result = num_left % num_right
print(result)

num_left = 6
num_right = 5
result = num_left // num_right
print(result)

num_left = 6
num_right = 5
result = num_left / num_right
print(result)


# lab2_8
x = 1.0 + 1j
y = 1.0 + 1j
print(x + y)
print(x - y)
print(x * y)
print(x / y)


# lab2_9
num_2s = 64
print(num_2s >> 1)
print(num_2s >> 6)
print(num_2s >> 10)


# lab2_10
input_str2 = input()
print('input string :', input_str2)
