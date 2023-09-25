def solution(nums):
    k=int(len(nums)/2)
    t=list(set(nums))
    if len(t) < k:
        ans = len(t)
    else:
        ans = k
    return ans

nums = [3,3,3,2,2,4]
print(solution(nums))

