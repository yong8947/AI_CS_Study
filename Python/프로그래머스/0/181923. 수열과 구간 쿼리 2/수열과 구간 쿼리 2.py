def solution(arr, queries):
    result = []
    for s,e,k in queries:
        list = []
        for i in range(s,e+1):
            if arr[i] > k:
                list.append(arr[i])
        if list:
            result.append(min(list))
        else:
            result.append(-1)
    return result