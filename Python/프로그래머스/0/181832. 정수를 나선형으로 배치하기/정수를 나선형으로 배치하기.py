def solution(n):
    answer = [[0]*n for _ in range(n)]
    
    dx = [0,1,0,-1] #행 (오 아래 왼 위)
    dy = [1,0,-1,0] #열
    x,y,d = 0,0,0
    
    for num in range(1,n*n+1):
        answer[x][y] = num
        
        nx, ny = x + dx[d], y + dy[d]
    
        if nx < 0 or nx >= n or ny < 0 or ny >= n or answer[nx][ny] != 0:
                d = (d + 1) % 4
                nx, ny = x + dx[d], y + dy[d]
            
        x, y = nx, ny
        
    return answer