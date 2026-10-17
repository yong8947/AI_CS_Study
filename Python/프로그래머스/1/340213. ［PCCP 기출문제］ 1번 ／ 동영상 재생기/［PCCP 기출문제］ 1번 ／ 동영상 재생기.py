def cal(time):
    mm,ss = time.split(':')
    t = int(mm) * 60 + int(ss) # 분을 초로 변환해서 계산하기 쉽게 만들기
    return t

def to_str(t):
    # 초를 다시 "mm:ss" 형식의 문자열로 변환 (두 자리 고정)
    mm = t // 60
    ss = t % 60
    return f"{mm:02d}:{ss:02d}"

def solution(video_len, pos, op_start, op_end, commands):  
    v_len = cal(video_len)
    p = cal(pos)
    os = cal(op_start)
    oe = cal(op_end)
    
    for command in commands:
        if os <= p <= oe:
            p = oe
            
        if command == 'prev':
            p -= 10
            if p<0:
                p = 0
                
        else:
            p+=10
            if p>v_len:
                p = v_len
                
        if os <= p <= oe:
            p = oe
                
    return to_str(p)