#방법1
def solution(num):
    num = [int(num) for num in list(str(num))]
    num1=[]
    k = len(num)-1
    while k>=0:
        num1.append(num[k])
        k -=1
    return num1


num = 1270234
print(solution(num))

#방법2
def solution(num):
    return [int(num) for num in str(num)][::-1]

num = 1270234
print(solution(num))

