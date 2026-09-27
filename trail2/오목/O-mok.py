board = [list(map(int, input().split())) for _ in range(19)]

#오른쪽 아래쪽 오른쪽아래대각선 오른쪽 위 대각선
dx = [0,1,1,-1]
dy = [1,0,1,1]

def solution():
    for i in range(19):
        for j in range(19):
            if board[i][j] == 0:
                continue
            
            target = board[i][j]  # 1(검은돌) 2(흰돌)
            
            for d in range(4):
                cnt = 1
                for k in range(1, 5):
                    nx = i + dx[d] * k
                    ny = j + dy[d] * k
                    
                    # 배열 범위를 벗어나지 않고 연속된 돌의 색이 같으면 카운트
                    if 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == target:
                        cnt += 1
                    else:
                        break
                
                # 연속 5개가 완성된 경우
                if cnt == 5:
                    print(target)
                    # 가운데 좌표 
                    mid_x = i + dx[d] * 2 + 1
                    mid_y = j + dy[d] * 2 + 1
                    print(mid_x, mid_y)
                    return

    # 승부가 안 난 경우
    print(0)

solution()