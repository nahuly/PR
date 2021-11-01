# 재귀문(느림)
def solution(n):
    if n<=2:
        ans = 1
    else:
        ans = solution(n-1) + solution(n-2)
    return ans % 1234567

n = 5
print(solution(n))


# 반복문(더 빠름)
def solution(n):
    a = [0,1]
    for i in range(n-1):
        b = a[-1] + a[-2]
        a.append(b)
    return a[-1] % 1234567

n = 5
print(solution(n))