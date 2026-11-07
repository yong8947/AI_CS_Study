def solution(number, limit, power):
    div_cnt = [0] * (number+1)
    
    # 시간복잡도 관리 (j는 i의 배수 즉 i는 j의 약수임을 이용)
    # 기존 이중반복문은 100000 x 100000 = 100억 
    # 배수 카운팅 방식은 100000 x ln(100000) = 115만 정도로 시간복잡도 감소
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