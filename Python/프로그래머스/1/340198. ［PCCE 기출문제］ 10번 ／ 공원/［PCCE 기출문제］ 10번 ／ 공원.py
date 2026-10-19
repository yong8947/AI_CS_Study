def solution(mats, park):
    mats.sort(reverse=True)
    
    R = len(park)
    C = len(park[0])
    
    for mat in mats:
        
        # 모든 꼭짓점을 가정
        for r in range(R-mat+1): 
            for c in range(C-mat+1):
                
                # mat x mat 영역에 사람이 없는지 확인
                can_here = True                
                for i in range(mat):
                    for j in range(mat):
                        if park[r+i][c+j] != "-1":
                            can_here = False
                            break
                    if not can_here:
                        break
                
                # 깔 수 있다면 그 돗자리가 가장 큼. (내림차순 정렬을 했으니까)
                if can_here:
                    return mat
    
    return -1