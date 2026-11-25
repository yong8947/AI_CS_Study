def solution(ingredient):
    check = []
    cnt = 0
    
    for i in ingredient:
        check.append(i)
        if check[-4:] == [1,2,3,1]:
            cnt += 1
            del check[-4:]
    
    return cnt 