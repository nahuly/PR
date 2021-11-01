#Chapter03-1
# 파이썬 리스트
# 자료구조에서 중요
# 리스트 자료형(순서O, 중복O, 수정O, 삭제O)

# 선언
a =[]
print(type(a))
b = list()
c = [70, 75, 80, 85] # Len
print(len(c))
d = [1000, 10000, 'Ace', 'Base', 'Captain']
# 다른 자료형을 한번에 담을 수 있음! 좋음!
e = [1000,10000,['Ace', 'Base', 'Captain']]
f = [21.42, 'foobar', 3, 4, False, 3.14159] 

# 인덱싱
print('>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1]))

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[-1][1:3])

# 리스트 연산
print('>>>>>')
print('c + d', c + d )
print('c * 3', c * 3)
print("'Test + c[0] :", 'Test' + str(c[0]))

# 값 비교
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])
print()

# Identity(id)
temp = c
print(temp,c)
print(id(temp))
print(id(c)) 
# 변수 할당시 쾌적한 환경(효율성)을 위해 둘이 같다!

# 리스트 수정, 삭제
print('>>>>>')
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c'] #[['a', 'b', 'c']]
print('c - ', c) # 원소 첨가
c[1] = ['a', 'b', 'c']
print('c - ', c) # 리스트 첨가 위의 #과 같다
# 차이!

c[1:3] = []
print('c - ', c)

del c[2] # 삭제
print('c - ', c)
print()

# 리스트 함수
a = [5, 2, 3, 1, 4]
print('a - ', a)
a.append(10) # 끝에 삽입
print('a - ', a)
a.sort()
print('a - ', a)
a.reverse()
print('a - ', a)
print('a - ', a.index(3), a[3])
a.insert(2, 7) #위치, 추가
print('a - ', a)
a.reverse()
print('a - ', a)
# del a[6]
a.remove(10)
print('a - ', a)
print('a - ', a.pop())
print('a - ', a) # 마지막거 꺼내고 나머지 보여줌
print('a - ', a.pop()) #last in , first out (마지막애가 먼저 나간다 ex) 뒤로가기)
print('a - ', a)
print('a - ', a.count(4)) # 4가 몇개 있다
ex = [8, 9]
a.extend(ex)
print('a - ', a)

# 삭제 : remove, pop, del

# 반복문 활용
while a:
    data = a.pop()
    print(data)












