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


"""

def solution(today, terms, privacies):
    # 약관 정보를 딕셔너리로 변환 (예: {'A': 6, ...})
    term_dict = {}
    for t in terms:
        kind, month = t.split()
        term_dict[kind] = int(month)
        
    # 오늘 날짜를 [연, 월, 일] 리스트로 분해
    t_y, t_m, t_d = map(int, today.split('.'))
    today_total = t_y * 12 * 28 + t_m * 28 + t_d
    
    answer = []
    
    for i, privacy in enumerate(privacies):
        date_str, kind = privacy.split()
        p_y, p_m, p_d = map(int, date_str.split('.'))
        
        # 1. 수집일 총 일수 구하기
        privacy_total = p_y * 12 * 28 + p_m * 28 + p_d
        
        # 2. 유효기간(달)을 일수로 환산하여 더함 (1달 = 28일)
        # 유효기간 만료일의 '다음 날'부터 파기해야 하므로, 
        # 파기 시작일은 (수집일 + 유효기간 * 28)이 됩니다.
        expire_total = privacy_total + (term_dict[kind] * 28)
        
        # 오늘 날짜가 파기 시작일 이상이면 파기 대상
        if today_total >= expire_total:
            answer.append(i + 1)
            
    return answer


"""