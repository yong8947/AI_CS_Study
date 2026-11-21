def solution(k, m, score):
    score.sort(reverse=True)
    ans = 0
    i = 0
    
    for _ in range(len(score)//m):
        ans += m * min(score[i:i+m])
        i += m
        
    return ans