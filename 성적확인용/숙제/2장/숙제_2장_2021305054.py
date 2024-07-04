# 학번 2021305054
# 이름 이승언

#LAB 2-1
print("Hello World\n")
print("Today is ",3, 16,"\n")
print("1 plus 1 equals to ",1+1,"\n")

#LAB 2-2
print("potato pizza: 15,000\nstake pizza: 25,000\n")

potato_pizza = 15000
stake_pizza = 25000

print("price is ",(potato_pizza*5 + stake_pizza*2)*(1.0+0.1))

#LAB 2-3
print("\npotato pizza 5: 75,000\nstake pizza 2: 50,000\ntotal: 125,000")

#포테이토 피자의 가격이 30% 할인된 가격일 때
salepotato = (potato_pizza*5)*(1.0-0.3)
print("\npotato pizza 5: ",salepotato)
print("\nstake pizza 2: ",stake_pizza*2)
print("\ntotal: ",salepotato + stake_pizza*2 )

#LAB 2-4 여러 자료형 사용하기
name_potato_pizza = "potato pizza"
name_stake_pizza = "stake pizza"
name_total = "Total"

price_potato_pizza = 15000
price_stake_pizza = 25000

amount_potato_pizza = 5
amount_stake_pizza = 2
price_total = ((price_potato_pizza*amount_potato_pizza) + (price_stake_pizza * amount_stake_pizza))*(1.0+0.1)

print("\n",name_potato_pizza, amount_potato_pizza,":",price_potato_pizza,"\n",name_stake_pizza, amount_stake_pizza,": ",price_stake_pizza,"\n",name_total,": ",price_total )

#LAB 2-5
##1
true = 1
print(true,"\n")
##2
name_steaky_pizza = "Steaky pizza"
print(name_steaky_pizza,"\n")
##3
order_num = 251
print("Your number is ",order_num)
##4
reciept = "Total: 10,000 won"
print(reciept,"\n")
##5
price = 10000
amount = 2
tax = 0.1
price_total_with_tax = price * amount + int(price*amount*tax)
print(price_total_with_tax,"\n")
##6
price_tax = int(10000+10000*0.10)
print(price_tax,"\n")

#LAB 2-6
num = 0.0
result = 0.0
num = 1

result = result + num
print(num,"\n")

#LAB 2-7
result = 0
num_left = 6.0
num_right = 6.0
result = num_right*num_left
print(result,"\n")

num_left = result
num_right = 0.5
result = pow(num_left,num_right)
print(result,"\n")

num_left = result
num_right = 5
result = int(num_left) % int(num_right)
print(result,"\n")

num_left = 6
num_right = 5
result = (int)(num_left) / (int)(num_right)
print(result,"\n")

num_left = 6
num_right = 5
result = num_left / num_right
print(result,"\n")

#LAB 2-8
#(1+1i) + (1+1i)
c1 = (1 + 1j)
c1_sol = c1 + c1
print(c1_sol,"\n")

#(1+1i) - (1+1i)
c2_sol = c1 - c1
print(c2_sol,"\n")

#(1+1i) * (1+1i)
c3_sol = c1 * c1
print(c3_sol,"\n")

#(1+1i)/(1+1i)
c4_sol = c1 / c1
print(c4_sol,"\n")

#LAB 2-9
num_2s = 64
print(num_2s >> 1, num_2s >> 6, num_2s >> 10, num_2s << 24, num_2s << 25, num_2s << 26);

#LAB 2-10
input_str2 = input()
print("input string: ",input_str2)
