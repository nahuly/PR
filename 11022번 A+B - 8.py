import sys

inp = int(sys.stdin.readline())

for i in range(inp):
    a,b=map(int,sys.stdin.readline().rsplit())
    print('Case #'+str(i+1) + ': ' + str(a)+ ' + ' + str(b) + ' = ' + str(a+b))