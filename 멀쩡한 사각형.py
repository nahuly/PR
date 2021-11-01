w = 499
h = 1000

def solution(w,h):
    if w==h:
        res = w*h - w
    else:
        if (w%2!=0) and (h%2!=0):
            res = w*h - (min(w,h)*2+1)
        else:
            res = w*h - min(w,h)*2
    return int(res)

print(solution(w,h))
