def solution(t, p):
    target = int(p)
    ans = 0
    
    for i in range(len(t)-len(p)+1):
        if int(t[i:i+len(p)]) <= target:
            ans += 1
            
    return ans