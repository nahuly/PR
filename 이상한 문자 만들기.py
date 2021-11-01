
def solution(s):
    idx=[]
    for i in range(len(list(s))):
        if list(s)[i] == ' ':
            idx += [i]
    print(idx)

    s1 = s.split(' ')
    k1=''
    for i in range(len(s1)):
        k= list(s1[i])
        for j in range(len(k)):
            if j % 2 == 0:
                k[j]=k[j].upper()
            else:
                k[j]=k[j].lower()
        
        k1 +=''.join(k)

    kk = list(k1)
    for j in idx:
        t=0
        if j != idx[0]:
            
            kk.insert(j+t,' ')
            t +=1
            
        else:
            kk.insert(j,' ')
            
    print(kk)

    return ''.join(kk)


s = "try hello world every girl"
print(solution(s))

