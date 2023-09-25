def solution(num):
    a = [int(a) for a in list(str(num))]
    return sum(a)

num = 987
print(solution(num))