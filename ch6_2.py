#Chapter06-2
# 파이썬 모듈
# Module : 함수, 변수, 클래스 등 파이썬 구성 요소 등을 모아놓은 파일

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def devide(x, y):
    return x / y

def power(x, y):
    return x ** y


# print('-' * 15)
# print('called! inner!')
# print(add(5, 5))
# print(subtract(15, 5))
# print(multiply(5, 5))
# print(devide(10, 2))
# print(power(5,3))
# print('-' * 15)

# __name__ 사용
if __name__ == "__main__": # 실행되는 대상이라는 뜻
    print('-' * 15)
    print('called! __main__')
    print(add(5, 5))
    print(subtract(15, 5))
    print(multiply(5, 5))
    print(devide(10, 2))
    print(power(5,3))
    print('-' * 15)


# 모듈을 만들고 외부에서 사용할 때는 위의 것이 실행되지 않는다.










