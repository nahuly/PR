def solution(array, commands):
    ans = []
    for n in list(range(len(commands))):
        slice = array[commands[n][0]-1:commands[n][1]]
        slice = sorted(slice)
        num = slice[commands[n][2]-1]
        ans.append(num)
    return ans


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))
    
