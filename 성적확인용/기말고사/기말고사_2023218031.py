# 학번 2023218031
# 이름 김태연

#1
n = int(input('n을 입력하시오 : '))
stack = 0
for i in range(n) :
	L = []
	for _ in range(n) :
		stack += 1
		L.append(stack)
	if i % 2 == 1 :
		L = L[::-1]
	for i in L :
		print('{:3d}'.format(i), and = '')
print()

#2
List = list(map(int, input('정수를 여러 개 입력하시오 : ').split()))
print('평균: {}'.format(sum(List) / len(List)))
print('최댓값: {}'.format(max(List)))
print('최솟값: {}'.format(min(List)))

#3
a = [2, 3, 4, 5, 6]
print('a =', a)
rev_a = []
for _ in range(len(a)):
	rev_a.append(a.pop())
print('rev_a =', rev_a)

#4
n = int(input('범위의 시작 정수 : '))
n = int(input('범위의 마지막 정수 : ')


#5


#6
s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
new_s_list = []
for i in s_list
    if not i in new_s_list:
	   new_s_list.append(i)
