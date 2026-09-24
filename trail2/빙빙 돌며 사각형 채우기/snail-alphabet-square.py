n, m = map(int, input().split())

# Please write your code here.
alphas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

arr = [['']*m for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0] #동남서북

x,y = 0,0
arr[0][0] = 'A'
dir_num = 0

def in_range(x,y):
    return 0<=x<n and 0<=y<m

for i in range(1,n*m):
    alpha = alphas[i % 26]

    nx,ny = x + dx[dir_num], y + dy[dir_num]

    if in_range(nx,ny) and arr[nx][ny] == '':
        x,y = nx,ny
    else:
        dir_num = (dir_num+1)%4
        x,y = x + dx[dir_num], y + dy[dir_num]

    arr[x][y] = alpha

for x in arr:
    for y in x:
        print(y, end=' ')
    print()