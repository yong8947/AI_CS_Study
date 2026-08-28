def solution(a, d, included):
    cnt=0
    for i in range(len(included)):
        if included[i] == True:
            cnt+=a
        a+=d
    return cnt
            
"""

def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        answer += (a + d * i) * int(included[i])
    return answer

"""