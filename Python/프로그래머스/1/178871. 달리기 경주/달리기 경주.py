def solution(players, callings):
    p = {name:i for i,name in enumerate(players)} # .index()로 찾기엔 배열길이때문에 시간초과될 수 있어서 딕셔너리 사용 ** 이 문제의 핵심 시간관리
    
    for name in callings:
        rank_now = p[name] # 현재 위치 
        update_rank = rank_now - 1 # 갱신 위치
        
        front_p = players[update_rank] # 현재 갱신위치에 있는 플레이어 이름 저장
        
        players[rank_now], players[update_rank] = front_p, players[rank_now] # 리스트에서 위치 교환
        
        p[name] = update_rank # 딕셔너리에서 이름불린 선수를 갱신위치로 업데이트
        p[front_p] = rank_now # 원래 갱신위치에 있던 플레이어의 위치를 한 칸뒤로 업데이트
        
    return players