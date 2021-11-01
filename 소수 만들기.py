def sosu(numbers):
    answer=[]

    if 1 in numbers:
        numbers.remove(1)

    if 0 in numbers:
        numbers.remove(0)

    for i in list(range(2, max(numbers))):
        for j in numbers:
        
            if i < j and j % i == 0:
                k = j
                if k in numbers:
                    numbers.remove(k)
                else:
                    numbers
            print(numbers)
    return numbers

numbers = [6,6,7,7,7,9,10,12,12]
print(sosu(numbers))





