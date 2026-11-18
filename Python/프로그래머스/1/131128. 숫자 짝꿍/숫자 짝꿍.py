def solution(X, Y):
    arr = []
    for i in range(9,-1,-1):
        num = min(X.count(str(i)), Y.count(str(i)))
        for _ in range(num):
            arr.append(str(i))
            
    if not arr:
        return "-1"
    
    if len(set(arr)) == 1 and ('0' in arr):
        return "0"
        
    ans = "".join(arr)
    
    return ans
    
    
    """
    arr = []
    x = list(X)
    y = list(Y)
    
    for num in x:
        if num in y:
            arr.append(num)
            y.remove(num)
    
    if not arr:
        return "-1"
    
    if len(set(arr)) == 1 and ('0' in arr):
        return "0"
        
    arr.sort(reverse=True)
    ans = "".join(arr)
    
    return ans
    """