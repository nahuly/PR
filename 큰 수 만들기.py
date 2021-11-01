# from itertools import combinations

# num="4177252841"
# print(list(num).remove(str(4)))
# num1 = num
# sorted(list(num1),reverse=True)
# num2 = num1[-4:]
# num2

# for i in list(num):
#     if i in list(num2):
#         print(i)
#         t=list(num)
#     print(t)
        

        
a = "4177252841"
k = 4

# def solution(a,k):
#     a1=list(a)
#     a2 = sorted(a1)
#     b = a2[:k]
#     for i in b:
#         if i in a1:
#             a1.remove(i)
#     return ''.join(a1),b

# print(solution(a,k))

a1=list(a)
a2 = sorted(a1)
b = a2[:len(a1)-k]
for i in b:
    if i in a1:
        a1.remove(i)