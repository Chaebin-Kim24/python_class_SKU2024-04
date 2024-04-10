### LAB 7-1
```python
from datetime import datetime
# LAB 7-1
today = datetime.now()
print('오늘의 날짜 : {}년 {}월 {}일'.format(today.year, today.month, today.day))

ojunohu = '오후' if today.hour >= 12 else  '오전'
h = today.hour if today.hour <= 12 else today.hour - 12
print('현재시간 : {} {}시 {}분 {}초'.format(ojunohu, h, today.minute, today.second))
```

### LAB 7-2
```python
# LAB 7-2
# 1.
to = datetime(2025, 12, 25)
left = to - today
print('오늘은 {}년 {}월 {}일입니다.'.format(today.year, today.month, today.day))
print('2025년 크리스마스까지는 {}일 {}시간 남았습니다.'.format(left.days, left.seconds // 3600))

# 2.
to = datetime(2036, 1, 1)
left = to - today
print('오늘은 {}년 {}월 {}일입니다.'.format(today.year, today.month, today.day))
print('2036년 새해까지는 {}일 {}시간 남았습니다.'.format(left.days, left.seconds // 3600))

# 3.
to = datetime(2024, 7, 3)
left = to - today
print('오늘은 {}년 {}월 {}일입니다.'.format(today.year, today.month, today.day))
print('2024년 저자 생일까지는 {}일 {}시간 남았습니다.'.format(left.days, left.seconds // 3600))
```

### LAB 7-3
```python
from datetime import timedelta
# LAB 7-3
# 1.
to = today + timedelta(1000)
print('{}년 {}월 {}일'.format(to.year, to.month, to.day))

#2.
couple_day = input("처음으로 사귄 연도와 월, 일을 입력하시오 : ")
year, month, day = couple_day.split(' ')
couple_date = datetime(int(year), int(month), int(day))
hundred_date = couple_date + timedelta(100)
print('100일 기념일은 : {}년 {}월 {}일입니다.'.format(hundred_date.year, hundred_date.month, hundred_date.day))
```
### LAB 7-4
```python
import math as m
# LAB 7-4
# 1.
for i in range(2, 11):
    print("4**{:2} = {:9.1f}".format(i, m.pow(4,i)))

# 2.
for angle in range(0, 190, 10):
    print("{:3} degree = {:5.3f} radian".format(angle, m.radians(angle)))

# 3.
for angle in range(0, 190, 10):
    print("sin( {:3}) = {:4.2f}".format(angle, m.sin(m.radians(angle))))
```
### LAB 7-5
```python
import random as rd
# LAB 7-5
# 1.
print("0에서 100 이하의 정수 중에서 5의 배수")
print([rd.randrange(0, 100, 5),rd.randrange(0, 100, 5),rd.randrange(0, 100, 5)])

# 2.
print("1에서 10 사이의 임의의 정수 :", rd.sample(list(range(1, 11)), 3))
```

### LAB 7-6
```python
# LAB 7-6
# 1.
print("이번 주의 추천 로또번호")
for i in range(5):
    print(rd.sample(list(range(1, 46)), 6))

# 2.
print("이번 주의 당첨 로또번호 + 보너스 ")
print(rd.sample(list(range(1, 46)), 6), "+", rd.sample(list(range(1, 46)), 1))

```
### LAB 7-7
```python
# 1.
t.setup(600, 600)
t.delay(1)
t.shape("turtle")
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)

# 2.
t.clearscreen()
t.setup(600, 600)
t.shape("turtle")
for _ in range(3):
    t.forward(100)
    t.left(120)
for _ in range(3):
    t.forward(200)
    t.left(120)

# 3.
t.clearscreen()
t.setup(600, 600)
t.shape("turtle")
for i in range(100, 400, 100):
    for _ in range(3):
        t.forward(i)
        t.left(120)

# 4.
t.clearscreen()
t.setup(600, 600)
t.shape("turtle")
for _ in range(4):
    t.forward(100)
    t.left(90)
```

### LAB 7-8
```python
# LAB 7-8
# 1.
t.clearscreen()
t.setup(600, 600)
t.color('blue')
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

t.color('red')
t.left(90)
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

t.color('yellow')
t.left(90)
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

t.color('green')
t.left(90)
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

# 2.
colors = ['blue', 'red', 'yellow', 'green']
t.clearscreen()
t.setup(600, 600)
for i in range(4):
    t.setheading(i * 90)
    t.color(colors[i])
    t.begin_fill()
    for _ in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()

# 3.
colors = ['blue', 'red', 'yellow', 'green']
t.clearscreen()
t.setup(600, 600)
for i in range(4):
    t.setheading(i * 90)
    t.color(colors[i])
    t.circle(100)
```

### LAB 7-9
```python
# LAB 7-9
# 1.
t.clearscreen()
t.setup(600, 600)
t.penup()
t.shape("turtle")
for _ in range(15):
    t.goto(rd.randint(-300, 300), rd.randint(-300, 300))
    t.stamp()

# 2.
t.clearscreen()
t.setup(600, 600)
t.penup()
t.shape("turtle")
for _ in range(15):
    t.goto(rd.randint(-300, 300), rd.randint(-300, 300))
    t.color(colors[rd.randint(0,3)])
    t.stamp()
```

### LAB 7-10
```python


# LAB 7-10
# 1.
from tkinter import *

window = Tk()

input_entry = Entry(window, width=50)
input_entry.pack()

button = Button(window, text='처리')
button.pack()

label = Label(window, text=' ')
label.pack()

window.mainloop()

#2.

def entry_to_label():
    str = input_entry.get()
    label.config(text=str)

window = Tk()

input_entry = Entry(window, width=50)
input_entry.pack()

button = Button(window, text='처리', command = entry_to_label)
button.pack()

label = Label(window, text=' ')
label.pack()

window.mainloop()

t.done()
```
