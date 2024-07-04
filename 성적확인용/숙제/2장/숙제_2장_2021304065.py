# 학번: 2021304065
# 이름: 이태희
# 1번
print('hello World\n')

print("Today is",3 ,"/",13,'\n')

print("1 plus 1 equals to ", 1 + 1)

# 2번
print("\n")

print("Potato pizza 5:",15000 * 5)

print("\nSteak pizza 2:",25000 * 2)

print("\nTotal:" ,(15000 * 5 + 25000 * 2) * (1 + 0.10))

# 3번
print("\n")

# 3-1
price_potato_pizza = 15000
price_steak_pizza = 25000
price_potato_pizza_total = price_potato_pizza * 5
price_steak_pizza_total = price_steak_pizza * 2
price_total = (price_potato_pizza_total + price_steak_pizza_total) * (1 + 0.10)

print("Potato pizza 5:",price_potato_pizza_total)
print("\nSteak pizza 2:",price_steak_pizza_total)
print("\nTotal:" ,price_total)

print("\n")

# 3-2
price_potato_pizza = price_potato_pizza * 0.7
price_potato_pizza_total = price_potato_pizza * 5 
price_total = (price_potato_pizza_total + price_steak_pizza_total)* 1.1

print("Potato pizza 5:",price_potato_pizza_total)
print("\nSteak pizza 2:",price_steak_pizza_total)
print("\nTotal:" ,price_total)

# 3-3

price_total=price_total * 0.8

print("\n")

print("Potato pizza 5:",price_potato_pizza_total)
print("\nSteak pizza 2:",price_steak_pizza_total)
print("\nTotal:" ,price_total)

# 4번 

name_potato_pizza = "Potato pizza"
name_steak_pizza = "Steak pizza"
name_total = "Total"
amount_potato_pizza = 5 
amount_steak_pizza = 2

print("\n")

print(name_potato_pizza,' :' , amount_potato_pizza,'\n', name_steak_pizza, ' :', amount_steak_pizza,'\n',name_total,' :',price_total)

# 5번
print("\n") 

# 5-1
True_ = 1
print(True_)

# 5-2
name_steaky_pizza = "Steaky pizza"
print("\n",name_steaky_pizza)

# 5-3
order_num = 251;
print("\nYour order number is", order_num);

# 5-4
reciept = "\nTotal: 10,000 won"
print(reciept)

# 5-5
price = 10000
amount= 2
tax = 0.1
price_total_with_tax = price * amount + (price * amount * tax)
print("\n",price_total_with_tax)

# 5-6
price_with_tax = (10000 + 10000 * 0.10)
print("\n", price_with_tax)

# 6번
num = 0
result = 0;
num = 1;
result = result + num;
print("\n",num)

# 7번
result = 0;
num_left = 6;
num_right = 6;

result = num_left * num_right
print("\n",result) 

num_left = result;
num_right = 0.5;

result = num_left ** num_right
print("\n", result)

num_left = result;
num_right = 5;

result = num_left % num_right
print("\n", result)

num_left = 6;
num_right = 5;

result = num_left // num_right
print("\n", result)

num_left = 6;
num_right = 5;

result = num_left / num_right
print("\n", result)

# 8번
x = 1.0 + 1j
y = 1.0 + 1j

print("\n") 
print(x+y)
print(x-y)
print(x*y)
print(x/y)

# 9번
num_2s = 64;

print("\n",num_2s>>1,"\n",num_2s>>6,"\n",num_2s>>10,"\n",num_2s<<1,"\n",num_2s<<6,"\n",num_2s<<10)

# 10번

input_str=input('\n')

print("input string:",input_str)
