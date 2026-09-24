N, T = map(int, input().split())
commands = input()
board = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
dx = [0,1,0,-1] #동남서북
dy = [1,0,-1,0]
dir_num = 3
x,y = (N-1)//2,(N-1)//2
cnt = board[x][y]

def in_range(x,y):
    return 0<=x<N and 0<=y<N

for s in commands:
    if s == 'R':
        dir_num = (dir_num+1)%4
    elif s == 'L':
        dir_num = (dir_num+3)%4
    elif s == 'F':
        nx,ny = x+dx[dir_num],y+dy[dir_num]
        if in_range(nx,ny):
            x,y = nx,ny
            cnt += board[x][y]
        else:
            continue
    
print(cnt)