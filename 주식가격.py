prices=[3,1]

def solution(prices):
    ans=[]
    for i in range(len(prices)):
        n=0
        for j in range(len(prices)):
            if i <j:
                if prices[i] <= prices[j]:
                    n+=1
                else:
                    n+=1
                    break
        ans.append(n)
    return ans

print(solution(prices))
