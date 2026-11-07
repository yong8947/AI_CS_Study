def solution(number, limit, power):
    div_cnt = [0] * (number+1)
    
    for i in range(1,number+1):
        for j in range(i,number+1,i):
            div_cnt[j] += 1
            
    ans = 0
    for i in range(1,number+1):
        if div_cnt[i] <= limit:
            ans += div_cnt[i]
        else:
            ans += power
    
    return ans