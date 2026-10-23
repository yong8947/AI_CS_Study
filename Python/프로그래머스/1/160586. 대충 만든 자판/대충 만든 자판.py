def solution(keymap, targets):
    ans = []
    
    for target in targets: 
        cnt = 0 # 몇 번 누르는 지
        
        for t in target:
            check = [] # 누를 문자가 있는 곳을 다 찾아 넣을 배열
            for key in keymap:
                if t in key: # 문자가 자판에 있으면
                    check.append(key.index(t)+1) # 몇 번 눌러야 그 문자가 나오는지 
            
            if check: # 문자가 있으면
                cnt += min(check) # 가장 적게 누르는 경우를 cnt에 더함
            else:
                cnt = -1 # 없으면 -1 할당하고 바로 반복문 종료
                break
                
        ans.append(cnt) # 총 몇 번인지 정답에 저장
        
    return ans