def solution(board, h, w):
    dx = [0,1,0,-1] #동남서북
    dy = [1,0,-1,0]
    ans = 0
    
    for i in range(4):
        nx, ny = h+dx[i], w+dy[i]
        if 0<=nx<len(board) and 0<=ny<len(board) and board[nx][ny] == board[h][w]:
            ans +=1
    
    return ans