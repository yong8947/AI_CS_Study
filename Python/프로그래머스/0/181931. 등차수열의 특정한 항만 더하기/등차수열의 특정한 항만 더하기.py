def solution(a, d, included):
    cnt=0
    for i in range(len(included)):
        if included[i] == True:
            cnt+=a
        a+=d
    return cnt
            