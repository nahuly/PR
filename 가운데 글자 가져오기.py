def solution(s):
    k = len(s) / 2
    if len(s) % 2 == 0:
        ans = s[int(k)-1] + s[int(k)]
    else:
        ans = s[int(k)]
    return ans

s='qwer'
print(solution(s))