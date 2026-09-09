def solution(arr):
    X = []
    for i in arr:
        for x in range(i):
            X.append(i)
    return X