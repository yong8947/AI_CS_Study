n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
arr = [[0]*n for _ in range(n)]

dxs = [0,1,0,-1]
dys = [1,0,-1,0] # 동남서북

def in_range(x,y):
    return 0<=x<n and 0<=y<n

for p,q in points:
    a = p-1
    b = q-1
    arr[a][b] = 1

    cnt = 0
    for dx,dy in zip(dxs,dys):
        nx,ny = a+dx, b+dy
        
        if in_range(nx,ny) and arr[nx][ny] == 1:
            cnt += 1
        
    if cnt == 3:
        print(1)
    else:
        print(0)