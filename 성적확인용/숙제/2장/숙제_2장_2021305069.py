# 학번: 2021305069
# 이름: 장수연

#LAB 2-1
print('Hello World!')

print('Today is', 3, '/', 14, '.')

print('1 plus 1 equals to', 1+1)

#LAB 2-2
print('potato pizza 5:', 15000*5)

print('steak pizza 2:', 25000*2)

print('potato pizza 5 steak pizza 2 total:', (15000*5 + 25000*2)*(1+0.10))

#LAB 2-3
price_potato_pizza = 15000
price_steak_pizza = 25000

price_potato_pizza_total = price_potato_pizza*5
price_steak_pizza_total = price_steak_pizza*2

price_total = (price_potato_pizza_total+price_steak_pizza_total)*(1+0.10)

#LAB 2-3-1
print('potato pizza 5 steak pizza 2 total:', price_total)

#LAB 2-3-2
price_potato_pizza = price_potato_pizza*(1-0.30)
price_potato_pizza_total = price_potato_pizza*5
price_total = (price_potato_pizza_total+price_steak_pizza_total)*(1+0.10)
print('potato pizza 5 steak pizza 2 total:', price_total)

#LAB 2-3-3
price_total = price_total*(1-0.20)
print('potato pizza 5 steak pizza 2 total:', price_total)

#LAB 2-4
name_potato_pizza = 'potato pizza'
name_steak_pizza = 'steak pizza'
name_total = 'total'
amount_potato_pizza = 5
amount_steak_pizza = 2
print(name_potato_pizza, amount_potato_pizza, name_steak_pizza, amount_steak_pizza, name_total,':',price_total)

#LAB 2-5-1
true = 1
print(true)

#LAB 2-5-2
name_steaky_pizza = 'Steaky pizza'
print(name_steaky_pizza)

#LAB 2-5-3
order_num = 251
print('Your order number is', order_num)

#LAB 2-5-4
reciept = 'Total: 10,000won'
print(reciept)

#LAB 2-5-5
price = 10000
amount = 2
tax = 0.1
price_total_with_tax = price*amount + price*amount*tax
print(price_total_with_tax)

#LAB 2-5-6
price_with_tax = 10000+10000*0.10
print(price_with_tax)

#LAB 2-6
num, result = 0, 0
num = 1
result = result + num
print(result)

#LAB 2-7
result = 0
num_left = 6
num_right = 6
result = num_left*num_right
print(result)
num_left = result
num_right = 0.5
result = num_left**num_right
print(result)
num_left = result
num_right = 5
result = num_left%num_right
print(result)
num_left = 6
num_right = 5
result = num_left//num_right
print(result)
num_letf = 6
num_right = 5
result = num_left/num_right
print(result)

#LAB 2-8
a = 1+1j
print(a+a, a-a, a*a, a/a)

#LAB 2-9
num_2s = 64
print(num_2s>>1, num_2s>>6, num_2s>>10, num_2s<<1, num_2s<<6, num_2s<<10)

#LAB 2-10
input_str = input('입력:')
print('input string:',input_str)
