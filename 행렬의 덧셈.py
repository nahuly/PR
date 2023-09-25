# def solution(arr1, arr2):
#     arr = [list(range(len(arr1[0]))),list(range(len(arr2[0])))]
#     for i in list(range(len(arr1))):
#         for j in list(range(len(arr1[0]))):
#             arr[i][j]= arr1[i][j] + arr2[i][j]
#     return arr



# arr1 = [[1],[2]]
# arr2 = [[3],[5]]

# print(solution(arr1, arr2))

#방법2
# import numpy as np

# def solution(arr1, arr2):
#     return np.array(arr1) + np.array(arr2)


# arr1 = [[1,2],[2,3]]
# arr2 = [[3,4],[5,6]]

# print(solution(arr1, arr2))

# arr=[[],[]]
# for i in [0,1]:
#     for j in [0,1]:
#         arr[i][j] = arr1[i][j] + arr2[i][j]
    
# print(arr)

# arr=[list(range(len(arr1[0]))),list(range(len(arr2[0])))]
# print(arr)


# for i in range(len(arr1[0])):
#     for j in range(len(arr2[0])):
#         arr[i][j] = arr1[i][j] + arr2[i][j]
    
# print(arr)


# 정답

def solution(arr):
    answer = []
    for i in arr:
        if len(answer) == 0:
            answer.append(i)
            continue
        if answer[-1] != i:
            answer.append(i)
    return answer

arr = [1,1,3,3,0,1,1]
print(solution(arr))

