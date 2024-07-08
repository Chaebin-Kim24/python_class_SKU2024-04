# 학번 2023218011
# 이름 김동희

1번
n = int(input('n을 입력하시오 : '))
c = 0
while c < n:
    for i in range(1,n+1):
        if(i==1):
            for k in range(i,n+1):
                print(k, end=' ')
            print()
        else:
            for k in range(i,n+1):
                print(k+n*2, end=' ')
            print()
        c += 2
    for j in range(n+1,1,-1):
        if(j==n+1):
            for k in range(j,n+1):
                print(k, end=' ')
            print()
        else:
            for k in range(j,n+1):
                print(k+n*2, end=' ')
            print()

2번
def mean_of_n(nums):
    avg = sum(nums)/len(nums)
    return avg
def max_of_n(nums):
    nmax = max(nums)
def  min_of_n(nums):
    nmin = min(nums)
nums = []
while None in nums:
    nums = int(input('정수를 여러 개 입력하시오 : '))
print('평균값은 ', mean_of_n(nums))
print('최댓값은 ', max_of_n(nums))
print('최솟값은 ', min_of_n(nums))

3번
a = [2, 3, 4, 5, 6]
rev_a = []
for i in range(len(a), 0, -1):
    rev_a=a.pop(i)

5번
num = int(input('주민등록번호 첫 6숫자 형식 입력 : '))
if num >= 250000:
    num = char(num)
    print('19{}{}년 {}{}월 {}{}일'.format(num[0],num[1],num[2],num[3],num[4],num[5]))
else:
    num = char(num)
    print('20{}{}년 {}{}월 {}{}일'.format(num[0],num[1],num[2],num[3],num[4],num[5]))