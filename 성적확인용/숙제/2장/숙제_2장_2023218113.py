# 학번: 2023218113
# 이름: 주현우

#LAB 2-1
print('Hello world!')

month=3
day=20
print('today is',month,day)

print('1 plus 1 equals to', 1 + 1)

#LAB 2-2 
potato_pizza_price = 15000
steak_pizza_price = 25000
print('Potato pizza 5:', 15000* 5)
print('Steak pizza 2:', 25000 * 2)
print('Total:',15000* 5+25000 * 2)

#LAB 2-3-1
price_potato_pizza = 15000
price_steak_pizza = 25000
price_potato_pizza_total = price_potato_pizza * 5
price_steak_pizza_total = price_steak_pizza * 2

price_total = (price_potato_pizza_total + price_steak_pizza_total) * (1.10)

print('Potato pizza 5:', price_potato_pizza_total)
print('Steak pizza 2:', price_steak_pizza_total)
print('Total:' ,price_total)

#LAB 2-3-2
price_potato_pizza = 15000 * (1 - 0.30)  
price_potato_pizza_total = price_potato_pizza * 5  
price_steak_pizza_total = 25000 * 2 
price_total = (price_potato_pizza_total + price_steak_pizza_total) * (1 + 0.10)  


print('Potato pizza 5:', price_potato_pizza_total)
print('Steak pizza 2:', price_steak_pizza_total)
print('Total:' ,price_total)

#LAB 2-3-3
price_potato_pizza = 15000 * (1 - 0.30)  
price_steak_pizza = 25000  
price_potato_pizza_total = price_potato_pizza * 5 
price_steak_pizza_total = price_steak_pizza * 2

price_total = price_potato_pizza_total + price_steak_pizza_total  
price_total = price_total * (1 - 0.20) 

print(price_total)

#LAB 2-4
name_potato_pizza = "Potato pizza"
name_steak_pizza = "Steak pizza"
name_total = "Total"

amount_potato_pizza = 5
amount_steak_pizza = 2

price_potato_pizza = 15000
price_steak_pizza = 25000

price_potato_pizza_total = price_potato_pizza * amount_potato_pizza
price_steak_pizza_total = price_steak_pizza * amount_steak_pizza

price_total = (price_potato_pizza_total + price_steak_pizza_total) * 1.10

print(name_potato_pizza, amount_potato_pizza, ":", price_potato_pizza_total)
print(name_steak_pizza, amount_steak_pizza, ":", price_steak_pizza_total)
print(name_total, ":", price_total)

#LAB 2-5-1
  cat = 1;
  print(cat) 

#LAB 2-5-2 
name_steaky_pizza = "Steaky pizza"
print(name_steaky_pizza)

#LAB 2-5-3
order_number = 251
print('Your order number is', order_number)

#LAB 2-5-4
receipt = "Total: 10,000 won"
print(receipt)

#LAB 2-5-5 
price = 10000
amount = 2
tax_rate = 0.1
price_total_with_tax = price * amount + (price * quantity * tax_rate)
print(price_total_with_tax)

#LAB 2-5-6
price_with_tax = int(10000 + 10000 * 0.10)
print(price_with_tax)

#LAB 2-6
num = 0
result = 0
num = 1
result = result + num
print(result)

#LAB 2-7

#LAB 2-8
x = 1 + 1j
y = 1 + 1j
print(x + y, x - y, x * y, x / y)

#LAB 2-9
num_2s = 64
print(num_2s >> 1, num_2s >> 6, num_2s >> 10, num_2s << 1, num_2s << 6, num_2s << 10)

#LAB 2-10
input_str = input("Enter a string: ")
print(" input string:", input_str)
