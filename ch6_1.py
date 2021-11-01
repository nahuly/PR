#Chapter06-1
# 파이썬 클래스
# OOP(객체 지향 프로그래밍), Self, 인스턴스 메소드, 인스턴스 변수

# !!!클래스(붕어빵틀) and 인스턴스(코드에서 사용하는 객체) 차이 이해
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능, 공유 (공용)
# 인스턴스 변수 : 객체마다 별도 존재 (개인)

# 예제1

class Dog(object): # object 상속
    # 클래스 속성
    species = 'firstdog' # 공유하는 공간

    # 초기화/인스턴스 속성
    def __init__(self, name, age): # 나만의 속성
        self.name = name
        self.age = age

# 클래스 정보
print(Dog)

# 인스턴스화
a = Dog("mikky", 2)
b = Dog("baby", 3)
c = Dog("mikky", 2) # a랑 다름(인스턴스화 시키면 달라짐)

# 비교
print(a == b, id(a), id(b), id(c))

# 네임스페이스
print('dog1', a.__dict__)
print('dog2', b.__dict__)

# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))

print(Dog.species)
print(a.species)
print(b.species)
print()

# 예제2
# self의 이해
class SelfTest:
    def func1(): # self가 없다 -> 클래스 메소드 -> 바로 클래스로 호출 (줄63)
        print('Func1 called')
    def func2(self): #self가 있다 -> 인스턴스 메소드
        print(id(self))
        print('Func2 called')

f = SelfTest() # 인스턴스 변수

# print(dir(f))
print(id(f))
# f.func1() # 예외
f.func2()

SelfTest.func1()
# self 유무의 차이 -> 클래스라서 매개변수가 없으니까 클래스로 호출
SelfTest.func2(f)
# 인스턴스를 직접 넣어주거나 아니면 줄 61 처럼 인스턴스로 호출
# SelfTest.func2(f) 예외
print()

# 예제3
# 클래스 변수, 인스턴스 변수
class Warehouse:
    # 클래스 변수
    stock_num = 0 # 재고

    def __init__(self, name): # 생성자
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self): # 소멸자
        Warehouse.stock_num -= 1

user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)
# Warehouse.stock_num = 50

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print('before', Warehouse.__dict__)
print('>>>', user1.stock_num)

# 인스턴스 네임클래스에 없으면 클래스 네임클래스에서 찾아보고 없으면 에러남

del user1
print('after', Warehouse.__dict__)

# 예제4

class Dog(object): # object 상속
    # 클래스 속성
    species = 'firstdog' # 공유하는 공간

    # 초기화/인스턴스 속성
    def __init__(self, name, age): # 나만의 속성
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound):
        return '{} says {}!'.format(self.name, sound)

# 인스턴스 생성
c = Dog('july', 4)
d = Dog('Marry', 10)

# 메소드 호출
print(c.info())
print(d.info())

# 메소드 호출
print(c.speak('Wal Wal'))
print(d.speak('Mung Mung'))











