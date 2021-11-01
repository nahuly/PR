num = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'
res = ''

for n in num:
    if n in [1,4,7]:
        L = n
        ans = 'L'
    elif n in [3,6,9]:
        R = n
        ans = 'R'
    else:
        if abs(L - n) > abs(n- (R - 2)):
            ans = 'R'
        elif abs(L - n) < abs(n - (R - 2)):
            ans = 'L'
        else:
            ans = hand[0].upper()
    res += ans
print(res)

