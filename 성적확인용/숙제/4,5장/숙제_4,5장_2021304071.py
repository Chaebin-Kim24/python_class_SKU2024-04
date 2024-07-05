# 학번 2021304071
# 이름 장민혁

#4.1
def my_greet():
    print("환영합니다.")
my_greet()
my_greet()

#4.2
def square(n):
    return n*n
print('3의 제곱은 :', square(3))
print('4의 제곱은 :', square(4))

#4.24
import re

def extract_words(sentence):
    # 정규 표현식을 사용하여 단어를 찾고 구두점을 제거
    words = re.findall(r'\b\w+\b', sentence.lower())
    return words

def main():
    sentences = []  # 입력 문장을 저장할 목록

    # 빈 줄이 입력될 때까지 여러 문장을 입력으로 사용
    print("여러 단어로 이루어진 글을 입력하세요:")
    while True:
        sentence = input().strip()
        if not sentence:
            break
        sentences.append(sentence)

    # 각 문장에서 단어 추출, 구두점 제거 및 집합에 추가
    words_set = set()
    for sentence in sentences:
        words = extract_words(sentence)
        words_set.update(words)

    # 단어를 사전순으로 정렬
    sorted_words = sorted(words_set)

    # 정렬된 단어 출력
    print("\nSorted words:")
    for word in sorted_words:
        print(word)

if __name__ == "__main__":
    main()

#4.25
s1 = 'Kang Young Min'
s2 = " Kang Young-Min"
s3 = 'Park Dong Min'
s4 = ' Park Dong-Min'

s1 = s1.replace(' ', '').replace('-', '').upper()
s2 = s2.replace(' ', '').replace('-', '').upper()
s3 = s3.replace(' ', '').replace('-', '').upper()
s4 = s4.replace(' ', '').replace('-', '').upper()

n_count_s1 = s1.count('N')
n_count_s2 = s2.count('N')
n_count_s3 = s3.count('N')
n_count_s4 = s4.count('N')

print("Kang Young Min(은)는", s1, '(으)로 수정됨')
print(" Kang Young-Min(은)는", s2, '(으)로 수정됨')
print("Park Dong Min(은)는:", s3, '(으)로 수정됨')
print(" Park Dong-Min(은)는", s4, '(으)로 수정됨')
print("\nOccurrences of 'N':")
print(s1, ':', n_count_s1, '개의 N이 나타남')
print(s2, ':', n_count_s2, '개의 N이 나타남')
print(s3, ':', n_count_s3, '개의 N이 나타남')
print(s4, ':', n_count_s4, '개의 N이 나타남')

#4.26
string = "Park(Java city), Kim(C city), Kang(Bython city), Lee(Bython city), Hong(Ruby city), Cho(Bython city), Koo(C city), Ryu(C++ city)"
print('주어진 문자열 :\n', string)

count = string.count('Bython city')
string = string.replace('Bython city', 'Python city')

print("\n수정된 문자열 :\n", string)
print('Bython 문자열은 모두', count, '번 수정했습니다.')

#4.27
#모르겠습니다.

#5.17
#1
animals = ['dog', 'cat', 'tiger', 'lion']
print("animals =", animals)

#2
animals = ['dog', 'cat', 'tiger', 'lion']
animals = animals[1:] + [animals[0]]
print('animals = ', animals)

#3
animals = ['dog', 'cat', 'tiger', 'lion']
print('animals = ', animals)

for animal in animals:
    print("I love", animal + ".")

#5.18
