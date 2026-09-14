def solution(arr):
    n1 = len(arr)
    n2 = len(arr[0])
    if n2 < n1:
        for i in range(n1):
            arr[i].extend([0]*(n1-n2))
    elif n1 < n2:
        for _ in range(n2-n1):
            arr.append([0]*n2)
    return arr