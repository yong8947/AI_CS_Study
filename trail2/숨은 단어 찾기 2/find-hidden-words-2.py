N, M = map(int, input().split())
arr = [input() for _ in range(N)]

# 동 동남 남 남서 서 북서 북 북동 
dx = [0,1,1,1,0,-1,-1,-1]
dy = [1,1,0,-1,-1,-1,0,1]

cnt = 0

for x in range(N):
    for y in range(M):
        if not arr[x][y] == 'L':
            continue 

        for d in range(8):
            check = True
            for s in range(1,3):
                nx,ny = x + dx[d] * s, y + dy[d] * s
                if 0<=nx<N and 0<=ny<M and arr[nx][ny] == 'E':
                    pass
                else:
                    check = False
                    break

            if check:
                cnt += 1

print(cnt)