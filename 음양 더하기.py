def solution(absolutes, signs):
    ans=0
    for i in list(range(len(absolutes))):
        if signs[i] == True:
            ans +=absolutes[i]
        else:
            ans -=absolutes[i]
    return ans

absolutes = [4,7,12]
signs = [True,False,True]
print(solution(absolutes,signs))
