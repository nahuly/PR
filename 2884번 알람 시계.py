h, m = input().split()


if int(m) < 45:
    if int(h)>=1:
        res=str(int(h)-1) + ' ' + str(int(m)+15)
    else:
        res='23 ' + str(int(m)+15)
else:
    res=str(int(h))+ ' ' + str(int(m)-45)

print(res)

