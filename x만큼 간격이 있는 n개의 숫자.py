# 방법1
def solution(x,n):
    ans=[x]
    k=x
    for i in range(n-1):
        x +=k
        ans.append(x)
    return ans

x=4
n=3
print(solution(x,n))

# 방법2
def solution(x,n):
    return [i*x + x for i in range(n)]

x=4
n=3
print(solution(x,n))