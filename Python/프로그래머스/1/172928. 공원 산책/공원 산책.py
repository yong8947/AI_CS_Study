def solution(park, routes):
    dx = [0,1,0,-1] #E S W N
    dy = [1,0,-1,0] 
    arr = [tuple(route.split()) for route in routes] # 튜플로 방향,거리 입력을 저장
    
    # 딕셔너리로 방향값 바로 지정할 수 있도록
    dict_xy = {
        'E': 0,
        'S': 1,
        'W': 2,
        'N': 3
    } 
    
    def find_first_pos(): # 시작위치 찾는 함수
        for i in range(len(park)):
            for j in range(len(park[0])):
                if park[i][j] == 'S':
                    return i,j
                
    x,y = find_first_pos() # 시작위치 지정
    
    def out_range(x,y):
        return x<0 or x>=len(park) or y<0 or y>=len(park[0]) # 범위 밖으로 나갔는지 확인하는 함수
    
    for direction, dist in arr: # 방향 거리를 하나 받음
        dir_num = dict_xy[direction] # 방향 인덱스를 저장
        can_go = True # 갈 수 있는지 확인하는 boolen값
        x1,y1 = x,y # for s 문이 작동했을 때 x,y값을 갱신하기 위한 변수
        
        for s in range(int(dist)): # 한 칸씩 점검
            nx,ny = x1 + dx[dir_num], y1 + dy[dir_num] 
            
            if out_range(nx,ny) or park[nx][ny] == 'X':
                can_go = False
                break
            
            x1,y1 = nx, ny
            
        if can_go:
            x,y = x1, y1
            
    return [x,y]


"""


def solution(park, routes):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direction = {
        'E': 0, 'S': 1,
        'W': 2, 'N': 3
    }

    h, w = len(park), len(park[0])

    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                x, y = i, j

    for route in routes:
        d, dist = route.split()
        dist = int(dist)
        nx, ny = x, y

        for _ in range(dist):
            nx += dx[direction[d]]
            ny += dy[direction[d]]

            if not (0 <= nx < h and 0 <= ny < w):
                break
            if park[nx][ny] == 'X':
                break
        else:
            x, y = nx, ny

    return [x, y]
    
>>> GPT한테 물어본 내 코드를 개선한 코드

"""