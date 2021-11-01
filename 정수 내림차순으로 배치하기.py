# 방법1
def solution(num):

    b=list(str(num))
    c=[int(c) for c in b]
    c=sorted(c, reverse=False)
    i = len(c)-1
    k=0
    while i >=0:
        t= 10**i*c[i]
        i -=1
        k +=t
    return k

num = 478920
print(solution(num))

# 방법2
def solution(num):
    a = list(str(num))
    a.sort(reverse=True)
    return int(''.join(a))

num = 478920
print(solution(num))

