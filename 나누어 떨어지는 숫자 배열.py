def solution(arr, div):
    t=[]
    for i in list(range(len(arr))):
        if arr[i] % div == 0:
            t.append(arr[i])
            ans = sorted(t)
    if len(t) == 0:
        ans = [-1]
    return ans

arr = [5,9,7,5,10,15,5]
div = 5
print(solution(arr, div))
