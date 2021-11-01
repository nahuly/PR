# 방법1
def solution(n):

    #필요한 숫자 자르기
    l = 3**16

    while l>n:
        l /= 3

    # 10진법 3진법으로 바꾸기
    th1=0
    th2=[]

    while l >=1:
        
        if n >=l:
            th1 = n // l
            n -= l*th1
            th2.append(int(th1))
        else:
            th2.append(0)
        l /= 3
    # 3진법 10진법으로 바꾸기
    th10 =0
    i= 0
    while i <= len(th2)-1:
        th10 += th2[i]*(3**i)
        i +=1

    return th10

for n in list(range(1,10)):
    print(solution(n))
 

# 방법2
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3) # 3진법을 10진법으로 바꿈
    return answer

for n in list(range(1,10)):
    print(solution(n))