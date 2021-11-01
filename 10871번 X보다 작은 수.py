import sys

n,m=map(int,sys.stdin.readline().rsplit())

t=list(map(int,sys.stdin.readline().rsplit()))
for i in range(n):
    if t[i] < m:
        print(t[i],end=' ')