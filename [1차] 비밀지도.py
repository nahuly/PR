def solution(n,arr1,arr2):

    def sum(a,b):
        c=[]
        i=0
        while i <=len(a)-1:
            c += [a[i]+b[i]]
            i +=1
        return c

    # 정수를 이진수로 바꾸기
    arr=[arr1,arr2]
    k = 2**(n-1)
    p=[[],[]]

    for j in list(range(len(arr))):
        for i in list(range(len(arr1))):
            k = 2**(n-1)
            a = arr[j][i]
            t = []
            while k>=1:
                if a >= k:
                    t.append(1)
                    a -= k
                else:
                    t.append(0)
                k /= 2
            p[j] += [t]

    # 이진수로 된 것을 #으로 바꾸기
    res=[]
    for k in list(range(len(arr1))):
        t=sum(p[0][k],p[1][k])
        ans=''
        for e in t:
            if e in [1,2]:
                ans += '#'
            else:
                ans += ' '
        res += [ans]
    return res

n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]

print(solution(n,arr1, arr2))




