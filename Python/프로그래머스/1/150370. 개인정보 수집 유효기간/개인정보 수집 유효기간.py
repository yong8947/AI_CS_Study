def solution(today, terms, privacies):
    
    # 날짜 정보를 비교하기 쉽게 정수로 변환
    def str_to_int(s):
        y,m,d = map(int, s.split('.'))
        return y * 12 * 28 + m * 28 + d
        
    term = dict(i.split() for i in terms) # 약관종류 : 보관기간
    now = str_to_int(today) # 현재날짜 정수화
    pri_days = [] # 보관날짜
    pri_kinds = [] # 약관종류
    for pri in privacies:
        d,kind = pri.split()
        day = str_to_int(d)
        pri_days.append(day)
        pri_kinds.append(kind)
    
    ans = []
    
    for i,kind in enumerate(pri_kinds):
        ex_term = int(term[kind]) 
            
        if now - pri_days[i] >= 28 * ex_term:
            ans.append(i+1)
            
    return ans