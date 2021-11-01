
from itertools import combinations


def solution(nums):
    # 세 개의 수 고를 때 경우의 수 구하기
    idx = list(combinations(nums,3))

    # 각 경우의 수의 합 구하기(중복값 허용)
    def sum(n):
        
        suma =[]
        for j in range(len(idx)):
            a = list(idx)[j]
            answer = 0
            for i in range(len(a)):
                answer += a[i]
            suma.append(answer)
        return suma

    numbers = list((sum(idx)))
    

    # 소수 구하기(중복값 허용)

    def sosu(numbers):

        if 1 in numbers:
            numbers.remove(1)

        if 0 in numbers:
            numbers.remove(0)

        for i in list(range(2, max(numbers))):
            for j in numbers:
            
                if i < j and j % i == 0:
                    k = j
                    if k in numbers:
                        numbers.remove(k)
                    else:
                        numbers
        return numbers
    return len(sosu(numbers))





























