def solution(wallet, bill):
    ans = 0  
    w_hor, w_ver = wallet[0], wallet[1]
    b_hor, b_ver = bill[0], bill[1]
    
    while True: # 지폐가 지갑에 못 들어가는 동안 반복
        
        if (w_hor >= b_hor and w_ver >= b_ver) or (w_hor >= b_ver and w_ver >= b_hor):
            break # 지폐가 지갑에 들어가면 그만
            
        if b_hor > b_ver:
            b_hor //= 2 
        else:
            b_ver //= 2
        
        ans += 1
        
    return ans