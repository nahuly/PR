def solution(a,b):
    n=[a,b]
    return sum(list(range(min(n),max(n)+1)))

a = 5
b = 3
print(solution(a,b))