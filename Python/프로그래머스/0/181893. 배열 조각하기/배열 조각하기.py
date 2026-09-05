def solution(arr, query):
    for i in range(len(query)):
        if i%2: 
            del arr[:query[i]]
        else:
            del arr[query[i]+1:]
    return arr