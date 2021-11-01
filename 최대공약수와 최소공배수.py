#방법1

def solution(n,m):
    a=[]
    b=[]
    for i in list(range(1,min(n,m)+1)):
        if n % i == 0 and m % i == 0:
            a.append(i)
    

    for j in list(range(min(n,m),1000000+1)):
        if j % n == 0 and j % m == 0:
            b.append(j)
    
    return [max(a), min(b)]

n =23
m= 46
print(solution(n,m))


#방법2

def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(gcdlcm(3,12))



