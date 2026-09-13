def solution(n):
    arr = []
    for i in range(n):
        arr2 = [0] * n
        arr2[i] = 1
        arr.append(arr2)
    return arr
    