def solution(s):
    ans = []
    
    for i in range(len(s)):
        for j in range(i-1,-1,-1):
            if s[i] == s[j]:
                ans.append(i-j)
                break
        else:
            ans.append(-1)
            
    return ans                