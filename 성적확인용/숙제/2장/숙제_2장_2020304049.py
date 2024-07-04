# 학번: 2020304049
# 이름: 윤치경
#
# 파이썬프로그래밍
# 2020304049 윤치경
#
# 2장 변수와 연산자


# LAB 2-1 : 여러 자료형의 값을 화면에 출력하기
print("Hello World!")
print("Today is ", 3, " / ", 14, " .", sep='')
print("1 plus 1 equals to ", 1 + 1, sep='')


# LAB 2-2 : 영수증 계산하기
print("Potato pizza 5: ", 15000 * 5, sep='')
print("Steak pizza 2: ", 25000 * 2, sep='')
print("Total: ", int((15000 * 5 + 25000 * 2) * (1 + 0.10)), sep='')


# LAB 2-3 : 변수를 써서 영수증 계산하기
price_potato_pizza, price_steak_pizza = 15000, 25000
price_potato_pizza_total = price_potato_pizza * 5
price_steak_pizza_total = price_steak_pizza * 2
price_total = int((price_potato_pizza_total + price_steak_pizza_total) * (1 + 0.10))

# 2-3-1 : 정의한 변수를 써서 LAB 2-2에서와 같이 화면에 영수증을 출력합니다.
print("Potato pizza 5: ", price_potato_pizza_total, sep='')
print("Steak pizza 2: ", price_steak_pizza_total, sep='')
print("Total: ", price_total)

# 2-3-2 : 포테이토 피자의 가격을 30% 할인받았을 때, 영수증의 Potato pizza 5 값과 Total 값을 변경하여 출력합니다.
price_potato_pizza = int(price_potato_pizza * (1 - 0.30))
price_potato_pizza_total = price_potato_pizza * 5
price_total = int((price_potato_pizza_total + price_steak_pizza_total) * (1 + 0.10))

print("Potato pizza 5: ", price_potato_pizza_total, sep='')
print("Steak pizza 2: ", price_steak_pizza_total, sep='')
print("Total: ", price_total, sep='')

# 2-3-3 : 추가로 총 금액에서 20% 할인 혜택을 받은 경우에, 영수증의 Total 값을 변경하여 출력합니다.
price_total = (int)(price_total * (1 - 0.20))

print("Potato pizza 5: ", price_potato_pizza_total, sep='')
print("Steak pizza 2: ", price_steak_pizza_total, sep='')
print("Total: ", price_total, sep='')


# LAB 2-4 : 여러 자료형의 변수를 써서 영수증 출력하기
name_potato_pizza = "Potato pizza"
name_steak_pizza = "Steak pizza"
name_total = "Total"
amount_potato_pizza = 5
amount_steak_pizza = 2

print(name_potato_pizza, " ", amount_potato_pizza, ": ", price_potato_pizza_total, sep='')
print(name_steak_pizza, " ", amount_steak_pizza, ": ", price_steak_pizza_total, sep='')
print(name_total, ": ", price_total, sep='')


# LAB 2-5 : 변수 이름의 오류 찾기
# 2-5-1 : 변수 이름으로 파이썬에서 키워드로 지정된 단어를 썼을 때
# True = 1
true = 1
print(true)

# 2-5-2 : 변수 이름에 오타가 있을 때
'''
name_steaky_pizza = "Steaky pizza"
print(Name_steaky_pizza)
'''
name_steaky_pizza = "Steaky pizza"
print(name_steaky_pizza)

# 2-5-3 : 변수 이름에 의미가 없을 때
'''
abcdefghijklmnop = 251
print("Your order number is ", abcdefghijklmnop)
'''
order_num = 251
print("Your order number is ", order_num, sep='')

# 2-5-4 : 변수 이름이 너무 길 때
'''
pizza_delivery_reciept_string_for_this_pizza_order = "Total: 10,000 won"
print(pizza_delivery_reciept_string_for_this_pizza_order)
'''
reciept = "Total: 10,000 won"
print(reciept)

# 2-5-5 : 변수 이름이 변수 내용과 다른 의미를 나타낼 때
'''
price = 10000
amount = 2
tax = 0.1
price_total_without_tax = price * amount + (int) (price * amount * tax)
print(price_total_without_tax)
'''
price = 10000
amount = 2
tax = 0.1
price_total_with_tax = price * amount + (int)(price * amount * tax)
print(price_total_with_tax)


# LAB 2-6 : 변수 값을 다시 저장하기
num, result = 0, 0
num = 1
result = result + num
print(num)


# LAB 2-7 : 산술연산자 써보기
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


# LAB 2-8 : 복소수 연산 해보기
x = 1.0 + 1j
y = 1.0 + 1j
print(x + y, x - y, x * y, x / y)


# LAB 2-9 : 비트 연산 해보기
num_2s = 64
print(num_2s >> 1, num_2s >> 6, num_2s >> 10, num_2s << 24, num_2s << 25, num_2s << 26)


# LAB 2-10 : 키보드 입력
input_str2 = input()
print("input string:", input_str2)
