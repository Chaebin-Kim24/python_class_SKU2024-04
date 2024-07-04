# 학번 2021304061
# 이름 이지민

#1번
print('Hello world!\n')
print("Today is", 3, "/", 13, ".")
print('1 plus 1 equals to',1+1)

#2번
print("Potato pizza 5:'",15000 * 5)
print("Steak pizza 2:",25000 * 2)
print("Total:", int((15000 * 5 + 25000 * 2) * (1 + 0.10)))
  
#3번

price_potato_pizza = 15000
price_steak_pizza = 25000
price_potato_pizza_total = price_potato_pizza * 5
price_steak_pizza_total = price_steak_pizza * 2
price_total = int((price_potato_pizza_total + price_steak_pizza_total) * (1 + 0.10))

print("Potato pizza 5:", price_potato_pizza_total)
print("Steak pizza 2:", price_steak_pizza_total)
print("Total:", price_total)


price_potato_pizza = int(price_potato_pizza * (1 - 0.30))
price_potato_pizza_total = price_potato_pizza * 5
price_total = int((price_potato_pizza_total + price_steak_pizza_total) * (1 + 0.10))

print("Potato pizza 5:", price_potato_pizza_total)
print("Steak pizza 2:", price_steak_pizza_total)
print("Total:",price_total)


price_total = int(price_total * (1 - 0.20))

print("Potato pizza 5:", price_potato_pizza_total)
print("Steak pizza 2:", price_steak_pizza_total)
print("Total:", price_total)

#4번

name_potato_pizza = "Potato pizza"
name_steak_pizza = "Steak pizza"
name_total = "Total"
amount_potato_pizza = 5
amount_steak_pizza = 2


price_potato_pizza = 15000  
price_steak_pizza = 25000  

price_potato_pizza_total = price_potato_pizza * amount_potato_pizza
price_steak_pizza_total = price_steak_pizza * amount_steak_pizza
price_total = int((price_potato_pizza_total + price_steak_pizza_total) * (1 + 0.10))


print(f"{name_potato_pizza} {amount_potato_pizza}: {price_potato_pizza_total}")
print(f"{name_steak_pizza} {amount_steak_pizza}: {price_steak_pizza_total}")
print(f"{name_total}: {price_total}")

#5번

true = 1
print(true)

# 2. 변수 이름에 오타가 있을 때
name_steaky_pizza = "Steaky pizza"
print(name_steaky_pizza)  

# 3. 변수 이름에 의미가 없을 때
order_num = 251
print("Your order number is {}.".format(order_num)) 

# 4. 변수 이름이 너무 길 때
receipt = "Total: 10,000 won"
print(receipt)  

# 5. 변수 이름이 변수 내용과 다른 의미를 나타낼 때
price = 10000
amount = 2
tax = 0.1
price_total_with_tax = price * amount + int(price * amount * tax)
print(price_total_with_tax)  

# 6. 변수 이름에 허용되지 않는 문자가 있을 때
price_with_tax = int(10000 + 10000 * 0.10)
print(price_with_tax)  
 
#6번 
num = 0
result = 0
num = 1
result = result + num
print(result)

#7번
result = 0
num_left = 6
num_right = 6

result = num_left * num_right
print(result)

num_left = result
num_right = 0.5

result = num_left ** num_right
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

#8번
x=1.0+1j
y=1.0 +1j
print(x + y)
print(x - y)
print(x * y)
print(x / y)

#9번
num_2s = 64
print(num_2s >> 1, num_2s >> 6, num_2s >> 10, num_2s << 1, num_2s << 6, num_2s << 10)

#10번
input_str2 = input()
print("input string:", input_str2)
