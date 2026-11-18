def solution(X, Y):
    arr = []
    # 만들 수 있는 가장 큰 수로 만들기 위해 큰 수부터 체크
    for i in range(9,-1,-1): 
        # X, Y가 공통으로 가진 숫자의 개수 계산
        num = min(X.count(str(i)), Y.count(str(i)))
        # 그만큼 배열에 넣어두기
        for _ in range(num):
            arr.append(str(i))
    
    # 빈 배열이면 '-1'을 리턴
    if not arr:
        return "-1"
    
    # 배열이 '0'으로만 이루어져 있으면 '0'을 리턴 // '000'을 방지
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