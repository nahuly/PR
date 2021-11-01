
def solution(n):
    s = list(range(2,n+1))
    while n >=1:
        for i in list(range(2,n)):
            if n in s:
                if n % i == 0:
                    s.remove(n)
        n -= 1
    return len(s)

n = 5
print(solution(n))


# 시간 너무 오래걸림

