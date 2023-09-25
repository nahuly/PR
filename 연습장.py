
def solution(L,x):
    answer = []
    if x > L[-1]:
        L.append(x)
    else:
        for i in range(len(L)):
            if x < L[i] :
             L.insert(i,x)
             break
        else:
            L
            
            
    
    answer =L
    return answer
            
            

        
def solution(L, x):

    answer =[]
    if x in L:
        for i in range(len(L)):
            if x == L[i]:
                answer = answer + [i]
        print(answer)
    else:
        answer.append(-1)
        print(answer)




def solution(L, x):
    answer = 0
    lower=0
    upper=len(L) - 1
    

    while lower <= upper:
        mid= (lower + upper) //2
        if x == L[mid]:
            return mid           
        elif x > L[mid]:
            lower = mid + 1            
        else:
            upper = mid - 1
    
    return -1


L = [2, 3, 5, 6, 9, 11, 15]
x = 5

solution(L,x)

