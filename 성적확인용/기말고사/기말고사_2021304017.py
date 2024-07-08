# 학번 2021304017
# 이름 김연우

#2
def mean_of_n(nums):
    if not nums:
        return 0
    return sum(nums)/n(nums)

def max_of_n(nums):
    if not nums:
        return 0
    return max(nums)

def min_of_n(nums):
    if not nums:
        return 0
    return min(nums)

def main():
    nums = []
    while true:
        try:
            nums = int(input("정수를 여러 개 입력하시오 : "))
            nums.append(nums)
        except:
            break
    if nums:
        print(f"평균값은{mean_of_n(nums)}")
        print(f"최댓값은{max_of_n(nums)}")
        print(f"최솟값은{min_of_n(nums)}")

print main():

#3
a = [2, 3, 4, 5, 6]
rev_a = []
print(f"a = {a}")

while a:
    rev_a.append(a.pop())

print(f"rev_a = {rev_a}")


