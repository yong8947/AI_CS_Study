n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# Please write your code here.
x,y = 0,0
dxs = [0,1,0,-1] #동남서북
dys = [1,0,-1,0]
dir = 0 #동쪽
arr[x][y] = 1 #첫번째 칸은 반복문으로 채우지 않기 때문에 미리 지정하기 

def in_range(x,y):
    return 0<=x<n and 0<=y<m

for i in range(2,n*m+1):
    nx,ny = x + dxs[dir], y + dys[dir]

    if not in_range(nx,ny) or arr[nx][ny] != 0:
        dir = (dir+1)%4

    x,y =  x + dxs[dir], y + dys[dir]
    arr[x][y] = i

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()