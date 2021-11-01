# 방법1
import string

def solution(s, n):

    low = string.ascii_lowercase
    up = string.ascii_uppercase

    s1=''   
    k = len(list(up))-1
    for j in range(len(list(s))):
        if s[j] == ' ':
                s1 += ' '
        
        else:
            for i in range(k+1):
                if s[j] == up[i]:
                    if i + n > k:
                        s1 += up[i+n-k-1]
                    else:
                        s1 += up[i+n]
    
                if s[j] == low[i]:
                    if i + n > k:
                        s1 += low[i+n-k-1]
                    else:
                        s1 += low[i+n]
    
    return s1


s = 'a B z'
n = 4
print(solution(s , n))




# 방법2
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)
    # 주어진 문장을 암호화하여 반환하세요.


# 실행을 위한 테스트코드입니다.
print('s는 "a B z", n은 4인 경우: ' + caesar("a B z", 4))



