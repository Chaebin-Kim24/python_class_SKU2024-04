# 학번 2023218113
# 이름 주현우


# 문제1
n = int(input('n을 입력하시오 :'))
n_list = []
for i in range(1, n ** 2 + 1):
    n_list.append(i)
for k in n_list:
    if k == 1:
        n_list_f = n_list[0:n]
        for f in n_list_f:
            print(f, end='')
        print()
    if k % n == 0 and (k // n) % 2 != 0:
        n_list_r = n[k:k + n]
        n_list_r.sort(reverse=True)
        for r in n_list_r:
            print(r, end='')
        print()
    if k & n == 0 and (k // n) % 2 == 0:
        n_list_a = n_list[k:k + n]
        for a in n_list_a:
            print(a, end='')
        print()

#문제2
print('정수를 여러 개 입력하시오')

#문제3
print('a=[2,3,4,5,6]')
print('rev_a=[6,5,4,3,2]')

#문제4

#문제5

#문제6