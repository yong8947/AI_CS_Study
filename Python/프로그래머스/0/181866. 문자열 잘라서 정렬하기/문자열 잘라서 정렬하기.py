def solution(myString):
    result = []
    for value in (myString.split('x')) :
        if value: result.append(value)
    return sorted(result)
            