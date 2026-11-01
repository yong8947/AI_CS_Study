def solution(s):
    ans = 1
    same_s = 1
    diff_s = 0
    x = s[0]
    
    for i in range(1,len(s)):
        if same_s == diff_s: # 문자열을 분리 후 초기화 및 x위치 업데이트
            ans += 1
            same_s = 1
            diff_s = 0
            x = s[i]
            continue
            
        if x == s[i]:
            same_s += 1
        else:
            diff_s += 1
            
    return ans