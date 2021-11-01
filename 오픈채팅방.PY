record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

def solution(record):
    id=[]
    for k in range(len(record)):
        id.append(record[k].split(' ')[1])

    b=[]
    for i in range(len(record)):
        a=[]
        for j in range(len(record)):
            if record[j].split(' ')[1] not in id[:i]:
                if record[j].split(' ')[1] in record[i]:
                    a.append(record[j])
        if a != []:
            b.append(a)

    c=[]
    for t in range(len(b)):
        c.append(b[t][-1])

    pre=[]
    for u in range(len(record)):
        for i in range(len(c)):
            if record[u].split(' ')[1] == c[i].split(' ')[1]:
                pre.append(record[u].replace(str(record[u].split(' ')[-1]),str(c[i].split(' ')[-1])))

    res=[]

    for j in range(len(pre)):
        if pre[j].split(' ')[0] == "Enter":
            res.append(pre[j].split(' ')[-1]+'님이 들어왔습니다.')

        elif pre[j].split(' ')[0] == "Leave":
            res.append(pre[j].split(' ')[-1]+'님이 나갔습니다.')

    return res

print(solution(record))










