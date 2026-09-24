n, m = map(int, input().split())

# Please write your code here.
arr = [[0]*m for _ in range(n)]

x,y = 0,0
dx = [0,1,0,-1]
dy = [1,0,-1,0] #동남서북

def in_range(x,y):
    return 0<=x<n and 0<=y<m

arr[0][0] = 1
dir_num = 1

for i in range(2,n*m+1):
    nx, ny = x + dx[dir_num], y + dy[dir_num]

    if in_range(nx,ny) and arr[nx][ny] == 0:
        x,y = nx,ny
    else:
        dir_num = (dir_num+3)%4
        x, y = x + dx[dir_num], y + dy[dir_num]

    arr[x][y] = i

for x in arr:
    for y in x:
        print(y, end=' ')
    print()