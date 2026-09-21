N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
x,y =0,0
dx = [1,0,-1,0] # 동남서북
dy = [0,-1,0,1]

ans = -1
cnt = 0
for i in range(N):
    d = dir[i]
    s = dist[i]

    if d == 'E':
        dir_num = 0
    elif d == 'S':
        dir_num = 1
    elif d == 'W':
        dir_num = 2
    elif d == 'N':
        dir_num = 3
    
    for _ in range(s):
        nx,ny = (x + dx[dir_num]), (y + dy[dir_num])
        x,y = nx,ny
        cnt += 1

        if x == 0 and y == 0:
            ans = cnt
            break
    if ans != -1:
        break
print(ans)