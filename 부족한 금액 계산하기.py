def solution(price, money, count):
    all = (count * (count + 1) / 2) * price
    result = all - money

    if result <= 0:
        result = 0
    
    return result

price = 3
money = 20
count = 4
print(solution(price, money, count))

