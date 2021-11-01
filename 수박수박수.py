#방법1
def solution(n):
    ans = ''
    if n % 2 == 0:
        ans = '수박' * int(n/2)
    else:
        ans = '수박' * int(n/2) + '수'
    return ans

for n in range(1,20):
    print(solution(n))
        


# 방법2
def water_melon(n):
    s = "수박" * n
    return s[:n]


# 실행을 위한 테스트코드입니다.
print("n이 3인 경우: " + water_melon(3));
print("n이 4인 경우: " + water_melon(4));

# 방법3
def water_melon(n):
    return "수박"*(n//2) + "수"*(n%2)


# 실행을 위한 테스트코드입니다.
print("n이 3인 경우: " + water_melon(3));
print("n이 4인 경우: " + water_melon(4));
