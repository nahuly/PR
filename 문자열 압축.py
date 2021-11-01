#1. 문자열 자르는 함수
#2. 반복되는 문자열 찾아내는 함수

s="acacacbacacac"
def solution(s):
    if len(s)==1:
        res=1
    else:
        d=[]
        for j in range(1,len(s)):
            a=[]
            for i in list(range(0,len(s),j)):
                if i+j<=len(s):
                    a.append(s[i:i+j])
                else:
                    a.append(s[i:])
            
            b=[a[0]]
            n=0
            for k in range(1,len(a)):
                if a[k]==a[k-1]:
                    n +=1
                    if len(b)>=1:
                        b.pop()
                    b.append(str(n+1)+a[k])
                else:
                    n=0
                    b.append(a[k])
            c=''
            for h in b:
                c += h
            
            d.append(len(c))
        res=min(d)

    return res

print(solution(s))



    
