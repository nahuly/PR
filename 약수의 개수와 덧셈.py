# 방법1
def solution(left, right):
    mid = list(range(left,right+1))

    num=[]
    for a in mid:
        n = a
        t=[]
        while n>=1:
            if a % n == 0:
                t.append(n)
            n -= 1
        num.append(len(t))
       

    res = 0
    for i in list(range(len(num))):
        if num[i] % 2 == 0:
            res += mid[i]
        else:
            res -= mid[i]
    return res


left = 24
right = 27
print(solution(left,right))

# 방법2
# [제곱수만 약수의 개수가 홀수이고 
# 나머지는 약수의 개수가 짝수이다.]

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer

left = 24
right = 27
print(solution(left,right))
