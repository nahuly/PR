info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

def solution(info, query):
    a=[]
    b=[]
    c=[]
    e=[]
    for i in range(len(query)):
        a.append(query[i])
        e.append(str(a[i]).replace('and','').split('  ')[:-1]+str(a[i]).replace('and','').split('  ')[-1].split(' '))
    for i in range(len(info)):
        b.append(info[i])
        c.append(b[i].split(' '))

    f=[]
    for i in range(len(e)):
        n=0
        for j in range(len(c)):
            if (e[i][0] in [c[j][0],'-']) \
            and (e[i][1] in [c[j][1],'-']) \
            and (e[i][2] in [c[j][2],'-']) \
            and (e[i][3] in [c[j][3],'-']) \
            and (int(c[j][-1]) >= int(e[i][-1])):
                n+=1
        f.append(n)    
    return f

print(solution(info, query))


    
    