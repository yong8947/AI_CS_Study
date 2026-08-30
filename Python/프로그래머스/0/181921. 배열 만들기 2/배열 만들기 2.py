def solution(l, r):
    arr = []
    for i in range(l,r+1):
        if set(str(i)).issubset({'0','5'}):
            arr.append(i)
    if not arr:
        arr.append(-1)
    return arr