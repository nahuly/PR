sco=[1,2,3,9,10,12]
k=7

sco1=sorted(sco)
ans=[]


if min(sco1) < k:
    new=sorted(sco1)[0] + sorted(sco1)[1]*2
    sco1.append(new)
    sco1+=sco1[2:]
print(sco1)

