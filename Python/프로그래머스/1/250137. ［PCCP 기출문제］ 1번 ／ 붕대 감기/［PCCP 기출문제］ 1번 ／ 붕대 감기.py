def solution(bandage, health, attacks):
    ans = health
    time, heal, plus_heal = bandage
    last_attack = attacks[-1][0]
    attack_time = [i for i,j in attacks]
    series_time = 0
    
    for t in range(1,last_attack+1):
        if t in attack_time:
            i = attack_time.index(t)
            ans -= attacks[i][1]
            series_time = 0
            
            if ans <= 0:
                return -1
        
        else:
            ans += heal
            series_time += 1
            
            if series_time == time:
                series_time = 0
                ans += plus_heal
            
            if health <= ans:
                ans = health
                
    return ans