---
### 5, 6장 리스트 실습 문제 (시험 범위 아님)
[도넛과 막대 그래프](https://school.programmers.co.kr/learn/courses/30/lessons/258711)

그래프들에 대한 정보가 주어졌을 때 그래프들이 종류별로 몇개씩 있는지 계산하는 문제입니다.

```python
# 주어진 입력값은 그래프 간선의 시작점과 끝점 리스트입니다.
edges = [[1, 2], [2, 2], [1, 3], [3, 4], [4, 5], [5, 3], [1, 6], [7, 6]]

# 간선 리스트로부터 각 점과 연결된 다른 점들에 대한 정보를 딕셔너리로 만듭니다 (키: 점 번호, 값: 점 번호 리스트).
nexts = {}
prevs = {}

# 점들로부터 전체 점 집합을 만듭니다.
nodes = {}

# 앞에 연결된 점이 없는 점들을 찾아서 집합을 만듭니다. 그중 뒤에 연결된 점이 가장 많은 점이 모든 그래프의 시작점이 됩니다. 
heads = {}
max_head = -1

# 그래프 시작점에 연결된 모든 그래프에 대해서 종류를 파악하고 개수를 셉니다. 
graphs_count = {}

# 시작점과 그래프별 개수를 리스트로 만듭니다.
answer = []
```

---
### 4장 파이썬 프로그래밍 코딩 테스트 실습 문제 (시험 범위 아님)
[하노이의 탑](https://school.programmers.co.kr/learn/courses/30/lessons/12946)

원판을 쌓을 수 있는 기둥이 1번, 2번, 3번 세개가 있고, 1번 기둥에 n개의 원판에 쌓여있습니다.
모든 원판을 3번 기둥으로 이동시키는 과정을 리스트로 answer에 저장합니다.

n = 1일 때, 1번 기둥의 유일한 원판을 3번으로 이동하면 되므로, answer = [[1, 3]] 입니다.

n = 2일 때, 1번 기둥의 가장 작은 원판을 2번으로 이동하고, 이후 1번 기둥의 남은 원판을 3번으로 이동하고, 2번 기둥의 원판을 3번으로 이동하면 되므로, 
answer = [[1, 2], [1, 3], [2, 3]] 입니다.

---

교과서 4장까지 중에 나오지 않았지만 문제를 푸는데 쓸 문법은 리스트의 덧셈 연산입니다. 
```python
list_zeros = [[0, 0]]
list_ones = [[1, 1], [1, 1]]
list_concatenated = list_zeros + list_ones
print(list_concatenated)
# 출력: [[0, 0], [1, 1], [1, 1]]
```

---

```python
# 1번 기둥에 쌓여 있는 원판의 개수를 n개라고 합니다.
n = 3

# x번 기둥에 쌓여 있는 가장 작은 원판들 m개를 y번 기둥으로 이동하는 과정을 반환하는 함수를 정의합니다.
def sub_hannoi(x, y, m):
    if m == 1:
        return [[x, y]]
    elif m == 2:
        # tmp는 나머지 하나 남은 기둥의 번호입니다.
        tmp = 6 - x - y
        return [[x, tmp], [x, y], [tmp, y]]
    elif m > 2:
        tmp = 6 - x - y
        # m-1개를 임시로 빼놓고, 가장 큰 것을 이동한 후에, 나머지를 모두 이동합니다.
        return sub_hannoi(x, tmp, m-1) + [[x, y]] + sub_hannoi(tmp, y, m-1)

answer = sub_hannoi(1, 3, n)
print(answer)
```


---
### 3장 파이썬 프로그래밍 코딩 테스트 실습 문제 (시험 범위 아님)
[가장 많이 받은 선물](https://school.programmers.co.kr/learn/courses/30/lessons/258712?language=python3)

친구 리스트와 선물 리스트가 주어졌을 때, 각자 특정 규칙에 따라서 선물을 받습니다. 
가장 선물을 많이 받는 친구가 받는 선물 개수를 구하는 문제입니다.

---

**참고사항**

교과서 3장에서는 리스트를 만드는 방법과, 리스트 항목들에 대해서 반복문을 수행하는 방법과, 
리스트에 항목을 추가하는 방법이 나와있습니다.

리스트는 대괄호 `[ ]` 안에 쉼포 `,`로 구분된 항목들을 넣어서 만듭니다.

```python
list_test = [1, 2, 3]
print(list_test)
# 출력: [1, 2, 3]
```

비어있는 리스트는 대괄호 `[]` 안을 비워서 만듭니다.

```python
list_empty = []
print(list_empty)
# 출력: []
```

`list()` 함수로도 리스트를 만들 수 있습니다.

```python
list_str = list('str')
print(list_str)
# 출력: ['s', 't', 'r']
```

리스트 원소들에 대한 반복문은 for ~ in 구문으로 합니다.

```python
for item in [1, 2, 3]
    print item
# 출력:
# 1
# 2
# 3
```

리스트에 원소를 추가하는 것은 append() 메소드로 합니다.

```python
primes = []
primes.append(2)
primes.append(3)
print(primes)
# 출력: [2, 3]
```

문제를 풀기 위해 필요한 추가적인 내용으로 리스트의 원소가 리스트가 될 수 있습니다.

```python
list_2d = []
list_2d.append([1, 2, 3])
list_2d.append([4, 5, 6])
print(list_2d)
# 출력: [[1, 2, 3], [4, 5, 6]]
```

또한 추가적인 내용으로 리스트의 원소를 인덱스로 접근할 수 있습니다.
```python
list_digit = ['0', '1']
print(list_digit[0])
# 출력: 0
list_digit[1] = 'one'
print(list_digit[1])
# 출력: one
```

문자열 관련해서 교과서에서 3장까지 중에 하지 않은 내용은, `==`으로 비교할 수 있다는 것입니다.
```python
str1 = "string"
str2 = "string"
print(str1 == str2)
# 출력: True
```

---

**답안 예시1: 수업시간에 한 내용**
```python
# 주어진 입력값은 친구들 이름 문자열 리스트 friends와 선물을 주고받은 기록 문자열 리스트 gifts입니다.
friends = ["mark", "john", "johnson", "michael", "jim"]
# 선물 기록 문자열 양식: "준사람 받은사람"
gifts = ["mark michael", "mark johnson", "jim john", "john jim", "jim john", "johnson mark", "mark jim"]

# 친구이름을 키로 하고, 준 선물 개수 장부를 값으로 하는 딕셔너리를 만듭니다. 선물 장부도 딕셔너리입니다.
# 딕셔너리 형식: {준사람이름 : 준선물개수장부}
# 준선물개수장부 형식: {받은사람이름 : 받은선물개수}
give_take_amount = {}
print('-'*20, '\n각자가 선물을 준 장부 딕셔너리, 장부에는 선물 받은 사람 이름과 선물 개수가 적혀있음')
for gift_str in gifts:
    giver, taker = gift_str.split(' ')
    print("\n준사람:",giver,", 받은 사람:", taker)
    if giver in give_take_amount:
        giver_dict = give_take_amount[giver]
        print(' '*3, '딕셔너리에 있음:',giver, giver_dict)
        if taker in giver_dict:
            giver_dict[taker] += 1
            print(' '*6, "장부에 선물 하나 추가됨", giver_dict)
        else:
            giver_dict[taker] = 1
            print(' '*6, "장부에 이름이 추가됨", giver_dict)
    else:
        print(' '*3, '딕셔너리에 없음:', giver)
        give_take_amount[giver] = {taker:1}
        print(' '*6, "장부가 추가됨", give_take_amount[giver])
    
    print(' '*3, '현재 딕셔너리:', give_take_amount)

# 각자 친구들에게 준 총 선물 개수가 몇개씩인지 딕셔너리를 만듭니다. 
give_amount = {}
print('\n'*2, '-'*20, '\n각자가 선물을 준 총 개수 딕셔너리')
for giver in give_take_amount:
    giver_dict = give_take_amount[giver]
    print("\n준사람:", giver, ", 장부:", giver_dict)
    value = 0
    for taker in giver_dict:
        value += giver_dict[taker]
        print(' '*3, "계산된 항목:", taker, giver_dict[taker])
    print(" "*6, "총합:", value)
    give_amount[giver] = value
    print(" "*3, "현재 딕셔너리:", give_amount)

# 각자 친구들에게서 받은 선물의 총 개수가 몇개씩인지 딕셔너리를 만듭니다. 
take_amount = {}
print('\n'*2, '-'*20, '\n각자가 선물을 받은 총 개수 딕셔너리')
for giver in give_take_amount:
    giver_dict = give_take_amount[giver]
    print("\n준사람:", giver, ", 장부:", giver_dict)

    for taker in giver_dict:
        if taker in take_amount:
            take_amount[taker] += giver_dict[taker]
            print(' '*3, "항목 업데이트:", taker, giver_dict[taker])
        else:
            take_amount[taker] = giver_dict[taker]
            print(' '*3, "항목 추가:", taker, giver_dict[taker])

    print(' '*3, "현재 딕셔너리:", take_amount)

# 각자 친구들에게서 준 선물의 총 개수에 받은 선물의 총 개수가 몇개씩인지 딕셔너리를 만듭니다. 
value_amount = {}
print('\n'*2, '-'*20, '\n각자가 선물을 준 개수에서 받은 개수를 뺀 값 딕셔너리')
for friend in friends:
    print("\n현재 계산할 친구:", friend)    

    my_give_amount = 0
    if friend in give_amount:
        my_give_amount = give_amount[friend]
        print(' '*3, "준선물 개수:", my_give_amount)

    my_take_amount = 0
    if friend in take_amount:
        my_take_amount = take_amount[friend]
        print(' '*3, "받은선물 개수:", my_take_amount)

    value_amount[friend] = my_give_amount - my_take_amount
    print(' '*3, "준개수 - 받은개수:", value_amount[friend])

# 최종적으로 각자 이번달에 받을 선물 개수를 구합니다. 

will_take_amount = {}
for friend in friends:
    will_take_amount[friend] = 0
print('\n'*2, '-'*20, '\n각자가 이번달에 받을 선물 딕셔너리')

for friend in friends:
    print("\n현재 계산할 친구:", friend)    

    for another in friends:
        if friend == another:
            print(' '*3, "선물 없음: 본인")
        else:
            print(' '*3, "선물 받을지 확인할 친구:",another)
            give = 0
            if friend in give_take_amount and another in give_take_amount[friend]:
                give = give_take_amount.get(friend).get(another)
                print(' '*6, "준선물 개수:", give)
            take = 0
            if another in give_take_amount and friend in give_take_amount[another]:
                take = give_take_amount.get(another).get(friend)
                print(' '*6, "받은 선물 개수:", take)

            subtract = give - take   
            if subtract > 0:
                will_take_amount[friend] += 1
                print(' '*6, "선물 받을 예정: 더 많이 줬었음")
            elif subtract < 0:
                print(' '*6, "선물 없음: 더 적게 줬었음")
            else:
                print(' '*6, "주고받은 숫자가 같음")
                if value_amount[friend] > value_amount[another]:
                    will_take_amount[friend] += 1
                    print(' '*6, "선물 받을 예정: 모두에게 준 선물의 총 수가 더 많음")
                else:
                    print(" "*6, "선물 없음: 모두에게 준 선물의 총 수가 작거나 같음")
    
    print('현재까지 계산된 받을 선물 딕셔너리', will_take_amount)

# 받을 선물 개수의 최대값 출력
print('\n받을 선물 개수 중 최대값:', max(list(will_take_amount.values())))


```

**답안 예시2**

```python
# 주어진 입력값은 친구들 이름 문자열 리스트 friends와 선물을 주고받은 기록 문자열 리스트 gifts입니다.
friends = ["mark", "john", "johnson", "michael", "jim"]
gifts = ["mark michael", "mark johnson", "jim john", "john jim", "jim john", "johnson mark", "mark jim"]

# 친구들 간에 선물을 몇번씩 주고 받았는지 횟수를 세어보겠습니다.
# 횟수를 세기 전에 먼저 선물 기록 문자열 리스트 gifts에 저장된 문자열 형식에 따라
# 모든 친구들 조합에 대해서 다음과 같이 선물 기록 문자열을 만들어 리스트에 저장하겠습니다.
friends_combination = []
for giver in friends:
    for taker in friends:
        str = giver + " " + taker
        friends_combination.append(str)
print(friends_combination)
# 출력: ['mark mark', 'mark john', 'mark johnson', ... ]

# 모든 친구들 조합에 대해서 gifts에 몇번 기록되었는지를 세서 counts 리스트에 저장하겠습니다.
counts = []
for str in friends_combination:
    count = 0
    for gift in gifts:
        if str == gift:
            count = count + 1
    counts.append(count)        
# 출력: [0, 0, 1, 1, 1, ... ]

# 방금 전에 두 단계로 나눠서 횟수를 세던 작업을 한 단계의 삼중 중첩문으로 해보겠습니다.
# 결과는 친구들에게 몇개씩 선물은 줬는지의 리스트를 각자에 대해 나열한 이차원 리스트입니다. 
table = []
for giver in friends:
    give_counts = []
    for taker in friends:
        str = giver + " " + taker
        count = 0
        for gift in gifts:
            if str == gift:
                count = count + 1
        give_counts.append(count)
    table.append(give_counts)
print(table)
# 출력: [[0, 0, 1, 1, 1], ...]
    
# 방금 한 것과 비슷하게 각자의 친구들에게 준 선물 총 개수를 리스트로 만들어보겠습니다. 
give_counts = []
for giver in friends:
    give_count = 0
    for taker in friends:
        str = giver + " " + taker
        for gift in gifts:
            if str == gift:
                give_count = give_count + 1
    give_counts.append(give_count)
print(give_counts)
# 출력: [3, 1, 1, 0, 2]

# 방금 한 것에서 첫번째 반복문과 두번째 반복문 순서를 바꿔서
# 각자 친구들에게 받은 선물의 총 개수를 리스트로 만들어보겠습니다. 
take_counts = []
for taker in friends:
    take_count = 0
    for giver in friends:
        str = giver + " " + taker
        for gift in gifts:
            if str == gift:
                take_count = take_count + 1
    take_counts.append(take_count)
print(take_counts)
# 출력: [1, 2, 1, 1, 3]

# friends의 반복문에서 각자에 대한 give_count와 take_count를 구하고, 그 차이를 구해서 이를 원소로 갖는 
# points 리스트를 만듭니다.
points = []
for friend in friends:
    give_count = 0
    giver = friend
    for taker in friends:
        str = giver + " " + taker
        for gift in gifts:
            if str == gift:
                give_count = give_count + 1

    take_count = 0
    taker = friend
    for giver in friends:
        str = giver + " " + taker
        for gift in gifts:
            if str == gift:
                take_count = take_count + 1

    point = give_count - take_count
    points.append(point)
print(points)
# 출력: [2, -1, 0, -1, 0]
    
# friends의 반복문에서 각자가 다른 친구들 각각에 대해 서로 준 선물 수를 비교해서
# 받은 선물보다 준 선물이 많은지 여부를 이차원 리스트로 만듭니다.
given_more_table = []
for me in friends:
    i_gave_more = []
    for friend in friends:
        give_count = 0
        str = me + " " + friend
        for gift in gifts:
            if str == gift:
                give_count = give_count + 1

        take_count = 0
        str = friend + " " + me
        for gift in gifts:
            if str == gift:
                take_count = take_count + 1

        if give_count > take_count:
            i_gave_more.append(True)
        else:
            i_gave_more.append(False)

    given_more_table.append(i_gave_more)
print(given_more_table)
# 출력: [[False, False, False, True, True], ... ]

# friends의 반복문에서 각자가 다른 친구들 각각에 대해 서로 준 선물 수를 비교해서
# 받은 선물과 준 선물이 같은지 여부를 이차원 리스트로 만듭니다.
given_same_table = []
for me in friends:
    i_gave_same = []
    for friend in friends:
        give_count = 0
        str = me + " " + friend
        for gift in gifts:
            if str == gift:
                give_count = give_count + 1

        take_count = 0
        str = friend + " " + me
        for gift in gifts:
            if str == gift:
                take_count = take_count + 1

        if give_count == take_count:
            i_gave_same.append(True)
        else:
            i_gave_same.append(False)

    given_same_table.append(i_gave_same)
print(given_same_table)
# 출력: [[True, True, True, False, False], ... ]

# friends의 반복문에서 각자가 다른 친구들 각각에 대해 서로 준 선물 수를 비교해서
# 규칙에 따라 친구들 각각으로부터 받을 선물의 개수를 이차원 리스트로 만듭니다.
gift_to_get = []
for me in friends:
    my_gift_to_get = []
    for friend in friends:
        if me == friend:
            my_gift_to_get.append(0)
            continue

        give_count = 0
        str = me + " " + friend
        for gift in gifts:
            if str == gift:
                give_count = give_count + 1

        take_count = 0
        str = friend + " " + me
        for gift in gifts:
            if str == gift:
                take_count = take_count + 1

        if give_count > take_count:
            my_gift_to_get.append(1)
        elif give_count < take_count:
            my_gift_to_get.append(0)

        else:
            my_index = 0
            for name in friends:
                if me == name:
                    break
                my_index = my_index + 1

            my_give_point = points[my_index]

            friend_index = 0
            for name in friends:
                if friend == name:
                    break
                friend_index = friend_index + 1

            friend_give_point = points[friend_index]

            if my_give_point > friend_give_point:
                my_gift_to_get.append(1)
            else:
                my_gift_to_get.append(0)

    gift_to_get.append(my_gift_to_get)

print(gift_to_get)
# 출력: [[0, 1, 1, 1, 1], ... ]

# 각자 친구들 각각으로부터 받을 선물 개수 이차원 리스트로부터 친구들로부터 받을 선물 개수를 더해서
# 규칙에 따라 각자가 받을 선물의 총 개수를 리스트로 만듭니다.
gift_to_get_total = []
for my_gift_to_get in gift_to_get:
    my_gift_to_get_total = sum(my_gift_to_get)
    gift_to_get_total.append(my_gift_to_get_total)

print(gift_to_get_total)
# 출력: [4, 0, 2, 0, 2]

# 각자 받을 선물의 총 개수의 최대값을 구합니다.
answer = max(gift_to_get_total)
print(answer)
# 출력: 4

```
