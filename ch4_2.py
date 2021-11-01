#Chapter04-2
# 파이썬 반복문
# FOR 실습

# 코딩의 핵심
# for in <collection>
#   <Loop body>

for v1 in range(10): # 0 ~ 9
    print('v1 is :' , v1)
print()

for v2 in range(1, 11): # 1 ~ 10
    print('v2 is :' , v2)
print()

for v3 in range(1, 11, 2):
    print('v3 is :', v3)
print()

# 1 ~ 1000 합

sum1 = 0

for v in range(1, 1001):
    sum1 += v

print('1 ~ 1000 sum :', sum1)

print('1 ~ 1000 sum :', sum(range(1, 1001)))

print(type(range(1,11))) #리스트 생성해주기 때문에 sum안에 넣어도 됨!

print('1 ~ 1000 4의 배수의 합 :', sum(range(4,1001,4)))

print()

# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제1
names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']

for n in names:
    print('You are : ', n)
print()

# 예제2
lotto_numbers = [11,19,21,28,36,37]

for n in lotto_numbers:
    print("Current number :", n)
print()

# 예제3
word = "Beautiful"

for s in word:
    print('word :', s)
print()

# 예제4
my_info = {
    "name" : "Lee",
    "Age" : 33,
    "City" : "Seoul"
}

for k in my_info:
    print('key :', my_info[k])

for v in my_info.values():
    print('value :', v)

for v in my_info.items():
    print('value :', v)

print()

# 예제5
name = 'PineAppLE'

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())
print()

# !!!break

numbers = [14,3,4,7,10,24,17,2,33,15,34,36,38]

for num in numbers:
    if num ==34:
        print('Found : 34!')
        break
    else:
        print('Not found : ', num)

print()

# continue

lt = ["1", 2,5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is bool:
        continue # 아래구문이 실행되지 않게됨!
    print("current type:", v, type(v))
    print("multiply by 2 :", v*3)
    print(True*3)
print()

# for - else #파이썬에만 있음

numbers = [14,3,4,7,10,24,17,2,33,15,34,36,38]

for num in numbers:
    if num == 49:
        print("Found : 49")
        break
else: # 위의 것 다 끝내고 없으면 밑에 실행
    print('Not Found : 49')
print()

# 구구단 출력

for i in range(2, 10):
    for j in range(1,10):
        print('{:4d}'.format(i*j), end='') # 줄바꿈(end)
    print()

print()

# 변환 예제
name2 = 'Aceman'

print('Reversed', reversed(name2))
print('List', list(reversed(name2)))
print('Tuple', tuple(reversed(name2)))
print('Set', set(reversed(name2))) # 순서x -> 실행할 때마다 위치 바뀜





