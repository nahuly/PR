def solution(s):
    a=[]
    for i in list(s):
        a.append(ord(i))
    t = sorted(a, reverse=True)
    b=[]
    for j in t:
        b.append(chr(j))
    return ''.join(b)

s = "Zbcdefg"
print(solution(s))

