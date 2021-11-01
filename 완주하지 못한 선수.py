# 방법1=> 시간 너무 오래걸림
def solution(participant, completion):
    for i in completion:
        if i in participant:
            participant.remove(i)
    return participant[0]

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))

# 방법2=> 간신히 통과인듯
def solution(participant, completion):
    a = sorted(participant)
    b = sorted(completion)
    c=''
    for i in list(range(len(completion))):
        if a[i] != b[i]:
            c=a[i]
            break

    if c == '':
        c=a[-1]
    return c

participant = ['b','b','b','a','ze']
completion = ['b','b','b','ze']
print(solution(participant, completion))

#방법3=> 엄청 빠른 방법
import collections

ans=collections.Counter(participant)-collections.Counter(completion)
print(list(ans.keys())[0])

# 방법4=> 정석 방법(# 방법1과 같은 방법이지만 hash가 훨씬 빠름)
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer

participant = ['b','b','b','a','ze']
completion = ['b','b','b','ze']
print(solution(participant, completion))