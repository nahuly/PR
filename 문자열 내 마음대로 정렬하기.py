

def solution(s,n):
    s=sorted(s)
    p=[]
    for j in list(range(len(s))):
        p += s[j][n]

    idx=[]
    for k in list(range(len(s))):
        t=p.index(sorted(p)[k])
        idx.append(t)
        
    a=[]
    for i in list(range(len(s))):
        for j in list(range(len(s))):
            if i==idx[j]:
                a.append(s[j])
        
    return s, p,sorted(p), idx, a

s = ["sun", "bed", "car",'dev','gir','boy']
n=1
print(solution(s,n))
