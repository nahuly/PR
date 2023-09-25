# 방법1
def solution(s):
    k=0
    j=0
    ans=0
    ans1=0
    for i in list(range(len(s))):
        if 'p' == list(s)[i] or 'P' == list(s)[i]:
            k +=1
        elif 'Y' == list(s)[i] or 'y' == list(s)[i]:
            j +=1

        if k == j:
            ans = True
        else:
            ans = False
    return ans

s = "avd"
print(solution(s))

# 방법2
def numPY(s):
    # 함수를 완성하세요
    return s.lower().count('p') == s.lower().count('y')

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( numPY("pPoooyY") )
print( numPY("Pyy") )



