
# 홀수는 약수개수 더하기 +1(2개 무조건 됨)
# 짝수는 무조건 1개

def solution(n):
    t=0
    if n % 2 ==0:
        res = 1
    else:
        for i in range(1,n):
            if n % i == 0:
                t+=1
        res = t+1
    return res

for n in list(range(1,20)):
    print((n,solution(n)))
    