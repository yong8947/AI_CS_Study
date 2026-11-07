def solution(k, score):
    ans = []
    
    for i in range(len(score)):
        if i <= k-1:
            ans.append(min(score[:i+1]))
        else:
            arr = score[:i+1]
            arr.sort(reverse=True)
            ans.append(arr[k-1])
                
    return ans