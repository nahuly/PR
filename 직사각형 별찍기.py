#방법1
a, b = map(int, input().strip().split(' '))
for j in range(b):
    for i in range(a):
        c= '*'*a
    print(c)

#방법2
a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)