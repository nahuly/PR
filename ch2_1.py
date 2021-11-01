#Chapther02-1
#파이썬 완전 기초
#Print 사용법

#기본 출력
print('Python Start!')
print("Python Start!")
print()
print()
print('''Python Start! ''')
print("""Python Start!""")

print()


# separator 옵션
print('p','y','t','h','o','n', sep='')
print('010','7777','1234', sep='-')
print('python', 'google.com', sep='@')


print()


#end 옵션

print('Welcome to', end=' ')
print('IT News', end=' ')
print('Web Site')

print()

#file 옵션
import sys

print('Learn Python', file=sys.stdout)

print()


#!!!외!!! format 사용(d :3 , s :python, f : 3.14) 정수, 문자열, 실수
print('%s %s' % ('one', 'two'))
print('{} {}' .format('one', 2))
print('{1} {0}' .format('one','two'))
print()

# %s
print('%10s' % ('nice')) #자릿수
print('{:>10}' .format('nice')) #왼쪽이라는 뜻


print('%-10s' % ('nice')) 
print('{:10}' .format('nice'))


print('{:_>10}' .format('nice'))
print('{:$>10}' .format('nice'))
print('{:^10}' .format('nice')) # 중앙 정렬

print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy')) # 원하는 자릿수로 잘라줌(공간 5개)
print('%5s' % ('pythonstudy'))
print('{:10.5}' .format('pythonstudy')) #10개중 5개만 나와라(공간 10개)

print()


# %d
print('%d %d' % (1,2))
print('{} {}' .format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42)) #정수,실수일때는 d,f를 붙여야한다

print()

# %f
print('%f' % (3.1432432433443))
print('%1.18f' % (3.1432432433443)) #정수.소수
print('{:f}' .format(3.1432432433443))

print('%06.2f' % (3.14159239849343943989384))
print('{:06.2f}'.format(3.14159239849343943989384))

 #003.14 총 6자리에서 정수부 3개 소수부 2개 . 1개 정수부 나머지는 0




