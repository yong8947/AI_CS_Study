def solution(a, b, c, d):
    score = 0
    arr = sorted([a,b,c,d])
    
    if len(set(arr)) == 1:
        score +=1111 * a
        
    elif len(set(arr)) == 2:
        if arr[1] == arr[2]:
            if arr[0] == arr[2]:
                score += (10 * arr[0] + arr[3])**2
            elif arr[1] == arr[3]:
                score += (10 * arr[1] + arr[0])**2
        else:
            score +=(arr[1] + arr[2]) * abs(arr[1] - arr[2])
    
    elif len(set(arr)) == 3:
        arr_qr = [i for i in arr if arr.count(i) == 1]
        score+= arr_qr[0] * arr_qr[1]
        
    else:
        score += min(arr)
        
    return score
            