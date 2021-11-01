def solution(numbers):
    answer =[]
    for l in range(len(numbers)):
        for t in range(len(numbers)):
            if l == t:
                answer = answer
            else:
                k = numbers[l] + numbers[t]
                if k in answer:
                    answer
                else:
                    answer.append(k)
    
    answer.sort()
    return answer

numbers1=[1,3,5]

print(solution(numbers1))

a = [1,2,3,1,1]
set(a)
