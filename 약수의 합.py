def solution(n):
    i = 1
    k = 0
    while i<=n:
        if n % i == 0:
            k += i
        i +=1       
    return k

n = 5
print(solution(n))
        