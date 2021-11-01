#방법1

def solution(num):
    num1=list(str(num))
    n=0
    for i in range(len(num1)):
        n +=int(num1[i])
    
    if num % n ==0:
        return True
    else:
        return False

num = 13
print(solution(num))

#방법2

def Harshad(n):
    # n은 하샤드 수 인가요?
    return n % sum([int(c) for c in str(n)]) == 0

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Harshad(18))

