def solution(num):
    num1=[]

    while num !=1:
        if num % 2 == 0:
            num1.append(num/2)
            num /=2
        else:
            num1.append(num*3+1)
            num = num*3+1
    
    if len(num1) >=500:
        return -1
    else:
        return len(num1)


num=626331
print(solution(num))
