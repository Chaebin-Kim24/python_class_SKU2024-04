print("\nLAB 2-1")
# LAB 2-1 : 여러 자료형의 값을 화면에 출력하기
#
# Hello World!를 화면에 출력합니다.
print("Hello World!")
# 오늘 날짜를 "Today is {month} / {day} ." 형식으로 화면에 출력합니다.
print("Today is", 3, "/", 13, ".")
# 계산 결과를 "1 plus 1 equals to {1+1} " 형식으로 화면에 출력합니다.
print("1 plus 1 equals to", 1+1)
#

print("\nLAB 2-2")
# LAB 2-2 : 영수증 계산하기
# 주어진 메뉴판에서 포테이토 피자 5판과 스테이크 피자 2판의 가격,
# 부가세 10%가 더해진 총 금액을 다음과 같은 형식으로 출력합니다.  
# """
# Potato pizza 5: #potato_pizza_price
# Steak pizza 2: #stake_pizza_price
# Total: #total_price
# """ 
# =====메뉴판=====
# 포테이토 피자      15,000
# 스테이크 피자      25,000
print("Potato pizza 5:", 15000 * 5)
print("Steak pizza 2:", 25000 * 2)
print("Total:", (int)((15000 * 5 + 25000 * 2) * (1 + 0.10)))
#

print("\nLAB 2-3")
# LAB 2-3 : 변수를 써서 영수증 계산하기 (LAB 2-2와 이어집니다.)
# 포테이토 피자와 스테이크 피자 가격을 변수 price_potato_pizza, price_steak_pizza에 저장하고,
# 포테이토 피자 5판, 스테이크 피자 2판의 가격을 
# 변수 price_potato_pizza_total, price_steak_pizza_total에 저장합니다. 
# 총 금액에 부가서 10%를 더해서 변수 price_total에 저장합니다.
price_potato_pizza, price_steak_pizza = 15000, 25000
price_potato_pizza_total, price_steak_pizza_total = price_potato_pizza * 5, price_steak_pizza * 2
price_total = (int)((price_potato_pizza_total + price_steak_pizza_total) * (1 + 0.10))

print("\nLAB 2-3-1")
# 1. 정의한 변수를 써서 LAB 2-2에서와 같이 화면에 영수증을 출력합니다.
print("Potato pizza 5:", price_potato_pizza_total)
print("Steak pizza 2:", price_steak_pizza_total)
print("Total:", price_total)

print("\nLAB 2-3-2")
# 2. 포테이토 피자의 가격을 30% 할인받았을 때, 영수증의 Potato pizza 5 값과 Total 값을 변경하여 출력합니다.
price_potato_pizza = (int)(price_potato_pizza * (1 - 0.30))
price_potato_pizza_total = price_potato_pizza * 5
price_total = (int)((price_potato_pizza_total + price_steak_pizza_total) * (1 + 0.10))

print("Potato pizza 5:", price_potato_pizza_total)
print("Steak pizza 2:", price_steak_pizza_total)
print("Total:", price_total)

print("\nLAB 2-3-3")
# 3. 추가로 총 금액에서 20% 할인 혜택을 받은 경우에, 영수증의 Total 값을 변경하여 출력합니다.
price_total = (int)(price_total * (1 - 0.20))
print("Potato pizza 5:", price_potato_pizza_total)
print("Steak pizza 2:", price_steak_pizza_total)
print("Total:", price_total)

print("\nLAB 2-4")
# LAB 2-4 : 여러 자료형의 변수를 써서 영수증 출력하기 (LAB 2-3와 이어집니다.)
# 포테이토 피자의 영수증에 출력되는 영문명 "Potato pizza"를 변수 name_potato_pizza에 저장합니다.
# 스테이크 피자의 영수증에 출력되는 영문명 "Steak pizza"를 변수 name_steak_pizza에 저장합니다. 
# 총 금액이 영수증에 출력되는 영문명 "Total"을 변수 name_total에 저장합니다.
# 포테이토 피자 주문 수량을 변수 amount_potato_pizza에 저장합니다. 
# 스테이크 피자 주문 수량을 변수 amount_steak_pizza에 저장합니다. 
# 생성한 변수를 이용해서 영수증을 출력합니다.  

name_potato_pizza, name_steak_pizza, name_total = "Potato pizza", "Steak pizza", "Total"
amount_potato_pizza, amount_steak_pizza = 5, 2
print(name_potato_pizza, str(amount_potato_pizza) + ":", price_potato_pizza_total)
print(name_steak_pizza, str(amount_steak_pizza) + ":", price_steak_pizza_total)
print(name_total + ":", price_total)

print("\nLAB 2-5")
# LAB 2-5 : 변수 이름의 오류 찾기
# 다양한 종류의 오류를 찾고 고쳐봅니다. 

print("\nLAB 2-5-1")
# 1. 변수 이름으로 파이썬에서 키워드로 지정된 단어를 썼을 때
# 다음 주석처리된 코드가 오류 없이 동작하게 변수 이름을 바꿔보세요
# True = 1
# print(True)
true = 1
print(true)

print("\nLAB 2-5-2")
# 2. 변수 이름에 오타가 있을 때
# 다음 주석처리된 코드가 오류 없이 동작하게 변수 이름을 바꿔보세요
# name_steaky_pizza = "Steaky pizza"
# print(Name_steaky_pizza)
name_steaky_pizza = "Steaky pizza"
print(name_steaky_pizza)

print("\nLAB 2-5-3")
# 3. 변수 이름에 의미가 없을 때
# 다음 주석처리된 코드에서 변수 이름을 변수 내용과 관련있게 지어서 바꿔보세요
# abcdefghijklmnop = 251
# print("Your order number is", abcdefghijklmnop, ".")
order_num = 251
print("Your order number is", order_num, ".")

print("\nLAB 2-5-4")
# 4. 변수 이름이 너무 길 때
# 다음 주석처리된 코드에서 변수 이름을 짧게 바꿔보세요
# pizza_delivery_receipt_string_for_this_pizza_order = "Total: 10,000 won"
# print(pizza_delivery_receipt_string_for_this_pizza_order)
receipt = "Total: 10,000 won"
print(receipt)

print("\nLAB 2-5-5")
# 5. 변수 이름이 변수 내용과 다른 의미를 나타낼 때
# 다음 주석처리된 코드에서 변수 이름을 변수 내용과 의미가 맞게 바꿔보세요
# price = 10000
# amount = 2
# tax = 0.1
# price_total_without_tax = price * amount + (int) (price * amount * tax)
# print(price_total_without_tax)
price = 10000
amount = 2
tax = 0.1
price_total_with_tax = price * amount + (int)(price * amount * tax)
print(price_total_with_tax)

print("\nLAB 2-5-6")
# 6. 변수 이름에 허용되지 않는 문자가 있을 때
# 다음 주석처리된 코드에서 변수 이름을 허용되는 문자만 사용해서 바꿔보세요
# price_+_tax = 10000 + 10000 * 0.10
# print(price_+_tax)
price_with_tax = (int)(10000 + 10000 * 0.10)
print(price_with_tax)

print("\nLAB 2-6")
# LAB 2-6 : 변수 값을 다시 저장하기
# 변수 num, result에 각각 0을 저장합니다.
# num에 1을 저장합니다.
# result + num의 결과를 result에 저장하고 출력합니다.
num, result = 0, 0
num = 1
result = result + num
print(result)

print("\nLAB 2-7")
# LAB 2-7 : 산술연산자 써보기 (LAB 2-6에서 이어집니다)
# result에 0을 저장합니다.
# 변수 num_left에 6을 저장합니다.
# 변수 num_right에 6을 저장합니다.
# num_left * num_right의 결과를 result에 저장하고 출력합니다.
# num_left에 result를 저장합니다.
# num_right에 0.5을 저장합니다.
# num_left ** num_right의 결과를 result에 저장하고 출력합니다.
# num_left에 result를 저장합니다.
# num_right에 5를 저장합니다.
# num_left % num_right의 결과를 result에 저장하고 출력합니다.
# num_left에 6을 저장합니다.
# num_right에 5를 저장합니다.
# num_left // num_right의 결과를 result에 저장하고 출력합니다.
# num_left에 6을 저장합니다.
# num_right에 5를 저장합니다.
# num_left / num_right의 결과를 result에 저장하고 출력합니다.
result = 0
num_left = 6
num_right = 6
print(result := num_left * num_right)
num_left = result
num_right = 0.5
print(result := num_left ** num_right)
num_left = result
num_right = 5
print(result := num_left % num_right)
num_left = 6
num_right = 5
print(result := num_left // num_right)
num_left = 6
num_right = 5
print(result := num_left / num_right)

print("\nLAB 2-8")
# LAB 2-8 : 복소수 연산 해보기
# 복소수 연산 (1 + 1i) + (1 + 1i), (1 + 1i) - (1 + 1i), (1 + 1i) * (1 + 1i), (1 + 1i) / (1 + 1i) 결과를 출력하시오
x = 1 + 1j
y = 1 + 1j
print(x + y, x - y, x * y, x / y)

print("\nLAB 2-9")
# LAB 2-9 : 비트 연산 해보기
# 변수 num_2s에 64를 저장합니다.
# num_2s >> 1, num_2s >> 6, num_2s >> 10, num_2s << 1, num_2s << 6, num_2s << 10을 출력합니다.
num_2s = 64
print(num_2s >> 1, num_2s >> 6, num_2s >> 10, num_2s << 24, num_2s << 25, num_2s << 26)

print("\nLAB 2-10")
# LAB 2-10 : 키보드 입력
# 변수 input_str에 키보드 입력을 받아서 저장하고, 앞에 " input string: "를 붙여서 출력합니다.
input_str = input()
print(" input string:", input_str)
