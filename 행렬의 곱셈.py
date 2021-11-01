
#방법1
arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]

def solution(arr1,arr2):
    col=len(arr1)
    row=len(arr2[0])
    d=[[0 for row in range(row)]for col in range(col)]
    
    def summul(arr1,arr2,j,k):
        c=0
        for i in range(len(arr1[0])):
            c+=arr1[j][i]*arr2[i][k]

        return c

    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            c=summul(arr1,arr2,i,j)
            d[i][j]=c
    return d

print(solution(arr1,arr2))


#방법2
X = [ [ 1, 2 ], [ 2, 3 ]]
Y= [[ 3, 4], [5, 6]]
def productMatrix(X, Y):
    answer = [[sum(a*b for a, b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
    return answer

print(productMatrix(X,Y))


    








        
