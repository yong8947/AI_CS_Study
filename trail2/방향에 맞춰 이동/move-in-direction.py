n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
dx = [1,0,-1,0] # 오 아래 왼 위
dy = [0,-1,0,1]

x,y=0,0 # 초기 위치 지

for i in range(n):
    d = dir[i]
    s = dist[i]

    # 각 문자를 숫자로 변환하여 저장 **
    if d == 'E':
        dir_num = 0
    elif d == 'S':
        dir_num = 1
    elif d == 'W':
        dir_num = 2
    elif d == 'N':
        dir_num = 3

    # 주어진 방향과 값만큼 이동한 위치 저장 **
    x += dx[dir_num] * s
    y += dy[dir_num] * s

print(x, y)