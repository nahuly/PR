import sys

inp=int(sys.stdin.readline())

for _ in range(inp):
    a,b=map(int,sys.stdin.readline().rsplit())
    print(a+b)