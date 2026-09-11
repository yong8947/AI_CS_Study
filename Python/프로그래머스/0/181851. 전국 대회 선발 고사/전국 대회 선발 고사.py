def solution(rank, attendance):
    l = []
    for i, (r,f) in enumerate(zip(rank,attendance)):
        if f:
            l.append((r,i))
    l.sort()
    return 10000*l[0][1] + 100*l[1][1] + l[2][1]