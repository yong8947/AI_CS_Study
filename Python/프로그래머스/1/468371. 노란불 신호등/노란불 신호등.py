import math

def solution(signals):
    T = [sum(s) for s in signals] # 모든 신호등의 주기 저장
    
    # 신호등 주기의 최소공배수 구하기(모든 신호등이 노란색인 경우가 있는지 판단하기위함)
    # 최소공배수까지 노란불이 안겹치면 겹치는 일이 없음
    limit_num = math.lcm(*T) 

    for time in range(1,limit_num+1):
        all_yellow = True
        
        for sig, t in zip(signals, T):
            G,Y,R = sig
            
            # 각 시간대에 신호등 색깔 확인
            t_mod = (time-1) % t + 1 
            
            # 노란불이 아니면 반복문 종료
            if not G < t_mod <= G+Y:
                all_yellow = False
                break
        
        # 모두 노란불이면 그 시간 return
        if all_yellow:
            return time
        
    return -1
        