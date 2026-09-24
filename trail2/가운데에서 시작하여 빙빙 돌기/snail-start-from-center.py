n = int(input())
grid = [[0] * n for _ in range(n)]

# Please write your code here.
dx = [0,-1,0,1] #서북동남
dy = [-1,0,1,0]

x,y = (n-1),(n-1)
dir_num = 0
grid[x][y] = n*n

def in_range(x,y):
    return 0<=x<n and 0<=y<n

for i in range(n*n-1,0,-1): # 역발상으로 거꾸로 거슬러올라가기 !! 이야
    nx,ny = x+dx[dir_num],y+dy[dir_num]
    if in_range(nx,ny) and grid[nx][ny] == 0:
        x,y = nx,ny
    else:
        dir_num = (dir_num+1)%4
        x,y = x+dx[dir_num],y+dy[dir_num]
    grid[x][y] = i
    
for x in grid:
    for y in x:
        print(y, end=' ')
    print()