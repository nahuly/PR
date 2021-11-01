def solution(s):
    t=s.split(' ')
    p=[]
    for i in t:
        p.append(int(i))
    mi = min(p)
    ma = max(p)

    return str(mi)+' '+str(ma)


s = "-1 -2 -3 -4"
print(solution(s))