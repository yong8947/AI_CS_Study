n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dxs,dys = [0,1,0,-1],[1,0,-1,0] #행,열

def in_range(x,y):
    return x >= 0 and x < n and y >=0 and y < n

ans = 0
for x in range(n):
    for y in range(n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx,ny) and grid[nx][ny] == 1:
                cnt+=1
        if cnt >= 3:
            ans += 1

print(ans)