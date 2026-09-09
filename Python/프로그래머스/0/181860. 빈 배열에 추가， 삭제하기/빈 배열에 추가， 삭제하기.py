def solution(arr, flag):
    X = []
    for num,ox in zip(arr,flag):
        if ox:
            X += [num] * (num*2)
        else:
            X = X[:-num]
    return X
        