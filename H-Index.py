cit=[3,0,6,1,5]


cit1=sorted(cit)
ans=[]
n=0
for i in range(1,len(cit1)):
    if 4 <= cit1[i]:
        n+=1
        ans.append(n)
print(ans)
            
            


# print(solution(cit))


