#Chapter02-2
#파이썬 완전 기초
#파이썬 변수

# 기본 선언
n = 700

# 출력
print(n)
print(type(n))
print()

# 동시 선언
x=y=z=700
print(x,y,z)

# 선언
var =75

# 재선언
var= 'change value'

# 출력
print(var)
print(type(var)) # string(문자열)


# Object References
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# 예1)
print(300)
print(int(300)) #위에것은 아래것을 간단하게 알아서 해준 것

# 예2)
# n -> 777
n=777

print(n, type(n))
print()

m=n

# m -> 777 <- n

print(m, n)
print(type(m), type(n))
print()

m = 400
print(m, n)
print(type(m), type(n))
print()

#!!!id(identity)확인 : 객체의 고유값 확인!!!

m = 800
n = 655

print(id(m))
print(id(n))
print(id(m) == id(n)) # 두개의 수가 다름
print()

# 같은 오브젝트 참조
m = 800
n = 800
z = 800
i = 800

print(id(m))
print(id(n))
print(id(m) == id(n)) # 두개의 수가 같음 (오브젝트(id)는 1개다!!!)
# => 굳이 여러개로 오브젝트(id가 같음) 지정안하려는 파이썬의 효율을 보여줌
print()

# 다양한 변수 선언(회사에서 판단하는 기준이 될 수도 있다)
# Camel Case : numberOfCollegeGraduates -> Method 선언
# Pascal Case : NumberOfCollegeGraduates -> Class 선언
# Snake Case : number_of_college_gruaduates -> 변수 선언
# 위에 것이 가장 많이 쓰임

student_grade = 3
studentGrade =3

# 허용하는 변수 선언 법
age = 1
Age =2
aGe=3
AGE=4
a_g_e=5
_age=6
age_=7
_AGE_=8
# 다 된다(밑줄을 허용한다)
#1AGE =7 는 에러가 난다(숫자로 시작하면 에러남)

# 예약어는 변수명으로 불가능

# ex) for =3, class=4
# python reserved words를 구글로 검색하면 예약어 정리 가능
# 강의자료에도 정리해놓았음












