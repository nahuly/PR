priorities = [2,1,3,2]
location = 2

def solution(priorities, location):
    num = list(range(len(priorities)))
    j=0
    while j < len(priorities):
        k = max(priorities[j:])
        if priorities[j] < k:
            priorities.append(priorities[j])
            priorities.remove(priorities[j])
            num.append(num[j])
            num.remove(num[j])
        else:
            j +=1
    return num.index(location)+1

print(solution(priorities,location))

        



