def solution(strArr):
    for i,s in enumerate(strArr):
        if i%2:
            strArr[i] = strArr[i].upper()
        else:
            strArr[i] = strArr[i].lower()
    return strArr

# enumerate() 기억해두기