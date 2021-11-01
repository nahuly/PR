# 방법1
def solution(a,b):
    c=0
    for i in list(range(len(a))):
        c += a[i] * b[i]
    return c

a = [1,2,3,4]
b = [-3,-1,0,2]
print(solution(a,b))

# 방법2
def solution(a,b):
    return sum([x*y for x , y in zip(a,b)])

a = [1,2,3,4]
b = [-3,-1,0,2]
print(solution(a,b))