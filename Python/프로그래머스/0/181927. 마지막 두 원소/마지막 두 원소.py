def solution(n):
    if n[-1] > n[-2]:
        n.append(n[-1] - n[-2])
    else:
        n.append(n[-1]*2)
    return n