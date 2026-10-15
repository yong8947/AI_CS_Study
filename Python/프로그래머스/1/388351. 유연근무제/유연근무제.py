def solution(schedules, timelogs, startday):
    ans = 0
    
    for i in range(len(schedules)):
        get_present = True
        cur_day = startday
        
        for j in range(7):
            if cur_day == 6:
                cur_day += 1
                continue
                
            if cur_day == 7:
                cur_day = 1
                continue
                
            hope_hour = schedules[i] // 100
            hope_min = schedules[i] % 100
            hope_total = hope_hour * 60 + hope_min + 10  # 10분 여유 포함
            
            real_hour = timelogs[i][j] // 100
            real_min = timelogs[i][j] % 100
            real_total = real_hour * 60 + real_min
            
            if real_total > hope_total:
                get_present = False
                break
                
            cur_day += 1
                
        if get_present:
            ans += 1
    
    return ans