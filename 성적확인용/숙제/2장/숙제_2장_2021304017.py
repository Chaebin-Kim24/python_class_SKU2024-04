# 학번 2021304017
# 이름 김연우

# 2-1-1
print("Hello World!")

# 2-1-2
from datetime import datetime
now = datetime.now()
formatted_date = now.strftime("Today is %m / %d .")
print(formatted_date)

# 2-1-3
print(f"1 plus 1 equals to {1+1}")

# 2-2
potato_pizza_price = 15000
steak_pizza_price = 25000
potato_pizza_quantity = 5
steak_pizza_quantity = 2
tax_rate = 0.10
potato_pizza_total = potato_pizza_price * potato_pizza_quantity
steak_pizza_total = steak_pizza_price * steak_pizza_quantity
total_price = potato_pizza_total + steak_pizza_total
total_price_with_tax = int(total_price * (1 + tax_rate))
print("Potato pizza 5:", potato_pizza_total)
print("Steak pizza 2:", steak_pizza_total)
print("Total:", total_price_with_tax)

# 2-3-2
price_potato_pizza_original = 15000
price_potato_pizza_discounted = price_potato_pizza_original * 0.7
price_steak_pizza = 25000
quantity_potato_pizza = 5
quantity_steak_pizza = 2
price_potato_pizza_total = price_potato_pizza_discounted * quantity_potato_pizza
price_steak_pizza_total = price_steak_pizza * quantity_steak_pizza
price_total = int((price_potato_pizza_total + price_steak_pizza_total) * (1 + 0.10))
print("Potato pizza 5:", price_potato_pizza_total)
print("Steak pizza 2:", price_steak_pizza_total)
print("Total:", price_total)

# 2-3-3
price_potato_pizza = 15000
price_steak_pizza = 25000
quantity_potato_pizza = 5
quantity_steak_pizza = 2
price_potato_pizza_total = price_potato_pizza * quantity_potato_pizza
price_steak_pizza_total = price_steak_pizza * quantity_steak_pizza
price_total = int((price_potato_pizza_total + price_steak_pizza_total) * (1 + 0.10))
price_potato_pizza = int(price_potato_pizza * (1 - 0.30))
price_potato_pizza_total = price_potato_pizza * quantity_potato_pizza
price_total = int((price_potato_pizza_total + price_steak_pizza_total) * (1 + 0.10))
price_total = int(price_total * (1 - 0.20))
print("Potato pizza 5:", price_potato_pizza_total)
print("Steak pizza 2:", price_steak_pizza_total)
print("Total:", price_total)

# 2-3-1
potato_pizza_price = 15000
steak_pizza_price = 25000
potato_pizza_quantity = 5
steak_pizza_quantity = 2
tax_rate = 0.10
potato_pizza_total = potato_pizza_price * potato_pizza_quantity
steak_pizza_total = steak_pizza_price * steak_pizza_quantity
total_price = potato_pizza_total + steak_pizza_total
total_price_with_tax = int(total_price * (1 + tax_rate))
print("Potato pizza 5:", potato_pizza_total)
print("Steak pizza 2:", steak_pizza_total)
print("Total:", total_price_with_tax)

# 2-4
price_potato_pizza = 15000
price_steak_pizza = 25000
quantity_potato_pizza = 5
quantity_steak_pizza = 2
price_potato_pizza_total = price_potato_pizza * quantity_potato_pizza
price_steak_pizza_total = price_steak_pizza * quantity_steak_pizza
price_total = int((price_potato_pizza_total + price_steak_pizza_total) * (1 + 0.10))
name_potato_pizza = "Potato pizza"
name_steak_pizza = "Steak pizza"
name_total = "Total"
amount_potato_pizza = 5
amount_steak_pizza = 2
print(name_potato_pizza, amount_potato_pizza, ":", price_potato_pizza_total)
print(name_steak_pizza, amount_steak_pizza, ":", price_steak_pizza_total)
print(name_total, ":", price_total)

# 2-5-2
name_steaky_pizza = "Steaky pizza"
print(name_steaky_pizza)

# 2-5-6
price_with_tax = int(10000 + 10000 * 0.10)
print(price_with_tax)

# 2-5-3
order_num = 251
print("Your order number is", order_num, ".")

# 2-5-4
pizza_recipt = "Total: 10,000 won"
print(pizza_recipt)

# 2-5-1
True_new = 1
print(True_new)

# 2-5-5
price = 10000
amount = 2
tax = 0.1
price_total_with_tax = price * amount + int(price * amount * tax)
print(price_total_with_tax)

# 2-6
num = 0
result = 0
num = 1
result = result + num
print(result)

# 2-7
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

# 2-8
import cmath
x = 1.0 + 1j
y = 1.0 + 1j
result1 = x + y
result2 = x - y
result3 = x * y
result4 = x / y
print(result1, result2, result3, result4)

# 2-9
num_2s = 64
print(num_2s >> 1, num_2s >> 6, num_2s >> 10, num_2s << 24, num_2s << 25, num_2s << 26)

# 2-10
input_str = input("please type any characters: ")
print("input string:", input_str)
