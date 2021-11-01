def solution(answers):
    n=len(answers)
    a= ([1,2,3,4,5]*2000)[0:n]
    b=([2,1,2,3,2,4,2,5]*1250)[0:n]
    c=([3,3,1,1,2,2,4,4,5,5]*1000)[0:n]

    ans1=[0,0,0]
    all = [a for a in zip(a,b,c)]
    for i in list(range(n)):
        for j in [0,1,2]:
            if all[i][j]==answers[i]:
                ans1[j] +=1
    t=2
    ans2=[]
    for t in [0,1,2]:
        if ans1[t] == max(ans1):
            ans2.append(t+1)
    return ans2

answers=[1,2,3,4,5]
print(solution(answers))



