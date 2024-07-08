# 학번 2023218090
# 이름 임상환

# 1
def create_snake_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    num = 1

    for i in range(n):
        if i % 2 == 0:
            for j in range(n):
                matrix[i][j] = num
                num += 1
        else:
            for j in range(n - 1, -1, -1):
                matrix[i][j] = num
                num += 1

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(*row)

n = int(input("n 입력: "))
snake_matrix = create_snake_matrix(n)
print_matrix(snake_matrix)

# 2
def mean_of_n(nums):
    return sum(nums) / len(nums)


def max_of_n(nums):
    return max(nums)


def min_of_n(nums):
    return min(nums)


user_input = input("정수 여러개 입력: ")
numbers = [float(num) for num in user_input.split()]

print(f"Mean: {mean_of_n(numbers)}")
print(f"Maximum: {max_of_n(numbers)}")
print(f"Minimum: {min_of_n(numbers)}")

# 3
a = [2, 3, 4, 5, 6]
rev_a = []
print(a)
while a:
    rev_a.append(a.pop())

print(rev_a)
