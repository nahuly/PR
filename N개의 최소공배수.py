
# def mul(arr):
#     ans = 1
#     for i in arr:
#         ans *=i
#     return ans

def solution(arr):
    for i in range(max(arr),(max(arr)*sorted(arr)[-2]+1),max(arr)):
        ans = []
        res = i
        for j in arr:
            ans += [i%j]
            if ans == [0]*len(arr):
                res = i
            break
    return res

arr = [2,6,8,14]
print(solution(arr))

