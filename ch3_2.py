#Chapter03-1
# 파이썬 문자형
# 문자형 중요

# !!! 슬라이싱

# 문자열 생성
str1 = " I am Python"
str2 = 'Python'
str3 = """ How are you?"""
str4 = ''' Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))

# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))


# 이스케이프 문자 사용
# I'm Boy

print("I'm Boy") # ' ' 이라면 에러 뜸
print('I\'m Boy')
print('I\\m Boy')

print('a \t b') # 탭만큼 띄움
print('a \n b') # 엔터침
print('a \"\" b')

# 참고 자료용 수업 자료용으로 더 정리해서 올려주심

excape_str1 = "Do you have a \"retro games\"?"
print(excape_str1)
excape_str2 = 'What\'s on TV?'
print(excape_str2)

# 탭, 줄 바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)
print()

# Raw String
raw_s = r'D:\python\test' # 나중에 파일 불러올때나 경로 지정에 사용
#escape를 사용하지 않기 위해 r(raw string)을 사용했구나로 인식하면됨
print(raw_s)
print()

# 멀티라인 입력
# 역슬래시 사용
multi_str = """
문자열
멀티라인 입력
테스트
"""

print(multi_str)

asdf = \
'dfdfdf' \
    'af' \

print(asdf)

#!!! 문자열 연산 !!!
str_o1 = "Python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Deajeon Busan Jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
# 시퀀스는 in 연산자를 사용할 수 있다 ex) str, list, tuple
print('z' in str_o1)
print('n' in str_o1)
print('P' not in str_o2)

# 문자열 형 변환
print(str(66), type(str(66))) # 66은 문자다!
print(str(10.1))
print(str(True), type(str(True))) # bool 이 아니라 문자다!

# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha...)
print("Capitalize: ", str_o1.capitalize())
print("endswith?:", str_o2.endswith("s"))
print("replace:", str_o1.replace("thon", ' Good')) #!!!!!!!!!!
print("sorted:", sorted(str_o1)) #리스트 형태로 반환(정렬도 해줌)
print("split:", str_o4.split(' ')) #리스트 배열형태로 반환!!!
#특정 단어나 문장 분리할 때 많이 쓴다.

# 반복(시퀀스) 버스 줄 서있는 사람
im_str = "Good Boy!"

print(dir(im_str)) # __iter__ 이게 있으면 반복할 수 있다는 말이다!

# 출력
for i in im_str:
    print(i)
 # 슬라이스(자르는 처리 가능!)

#!!!!! 슬라이싱 
str_sl = "Nice Python"

print(len(str_sl))

# 슬라이싱 연습
print(str_sl[0:3]) # 0 1 2 만 나옴
print(str_sl[5:]) # [5:11]
print(str_sl[:len(str_sl)]) # str_sl[:11]
print(str_sl[:len(str_sl)-1]) # str_sl[:10]
print(str_sl[1:9:2])
print(str_sl[-5:])
print(str_sl[1:-2])
print(str_sl[::2])
print(str_sl[::-1]) # 역으로 출력

# 아스키 코드(또는 유니코드)
a = 'z'

print(ord(a)) # 아스키 코드로
print(chr(122)) # 문자로

 



















