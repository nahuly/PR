#방법1
def solution(n):
    i=1
    while i<=n:
        if i**2 == n:
            ans= (i+1)**2
            break
        else:
            ans = -1
        i +=1
    return ans

n = 36
print(solution(n))

#방법2

def solution(n):
    sqrt = n**(1/2)

    if sqrt % 1 ==0:
        ans = (sqrt+1)**2
    else:
        ans = -1
    return int(ans)

n = 36
print(solution(n))



