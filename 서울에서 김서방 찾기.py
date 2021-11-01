# 방법1
def solution(seoul):
    for i in list(range(len(seoul))):
        if seoul[i] == "Kim":
            return "김서방은 {}에 있다".format(i)

seoul= ["Jane", "Kim"]
print(solution(seoul))


# 방법2
def solution(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))

seoul= ["Jane", "Kim"]
print(solution(seoul))