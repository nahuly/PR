#방법1
def solution(ph):
    ph = sorted(ph)
    i=0
    while i<=len(ph)-2:
        if ph[i] in ph[i+1][0:len(ph[i])]:
            return False
        i +=1
    return True

ph = ['11','12','22','224']
print(solution(ph))

#방법2=>startswith
def solution(ph):
    ph1 = sorted(ph)

    for p1,p2 in zip(ph1, ph1[1:]):
        if p2.startswith(p1):
            return False
    return True

ph = ['11','12','22','224']
print(solution(ph))

