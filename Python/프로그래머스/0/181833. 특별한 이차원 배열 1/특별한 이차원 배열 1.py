def solution(n):
    arr = []
    for i in range(n):
        arr2 = [0] * n
        arr2[i] = 1
        arr.append(arr2)
    return arr

"""

def solution(n):
    answer=[[0]*n for i in range(n)]
    for i in range(n): answer[i][i]=1
    return answer

"""