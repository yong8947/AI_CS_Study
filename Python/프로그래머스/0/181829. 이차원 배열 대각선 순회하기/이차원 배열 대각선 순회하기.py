def solution(board, k):
    cnt = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i + j <= k:
                cnt += board[i][j]
    return cnt