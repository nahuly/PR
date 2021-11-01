# 방법1
def solution(s):
    return (len(s) == 4 or len(s) == 6 ) and s.isnumeric()

s='123456'
print(solution(s))

# 방법2
def alpha_string46(s):
    try:
        int(s)
    except:
        return False
    return len(s) == 4 or len(s) == 6 

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( alpha_string46("a234") )
print( alpha_string46("1234") )