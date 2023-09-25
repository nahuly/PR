# 방법1 => 오래걸림
from itertools import combinations


def solution(d, budget):
    for j in list(range(len(d),1,-1)):
        a=[]
        for i in list(combinations(d,j)):
            a.append(sum(i))
        mi = min(a)
        if mi <= budget:
            res = j
            break
    return res

d=[2,2,3,3]
budget = 10
print(solution(d, budget))

# 방법2=> 오래걸림
d=[2,2,3,3]
budget = 10

for j in list(range(len(d),1,-1)):
        a=[]
        for i in list(combinations(d,j)):
            a.append(sum(i))
        mi = min(a)
        if mi <= budget:
            res = j
            break
print(res)

# 방법3=> 통과!
def solution(d, budget):
    res = 0
    d=sorted(d)
    for i in list(range(len(d)+1)):
        all = sum(d[:i])
        if all <= budget:
            res = i
    return res

d=[1,3,2,4,5]
budget = 9
print(solution(d, budget))



