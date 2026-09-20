n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r)-1, int(c)-1 #배열 인덱스를 위해 -1 

# Please write your code here.
dx = [0,1,-1,0] # 동남북서 - 서로 반대방향끼라 묶기
dy = [1,0,0,-1]

# 딕셔너리 활용
dic = {
    "R":0,
    "D":1,
    "U":2,
    "L":3
}

dir = dic[d] # 방향 인덱스 설정

def in_range(x,y):
    return 0<=x<n and 0<=y<n # 배열의 범위를 넘는지 확인하는 함수

# t초동안 설정하고 방향 바꾸는데 1초 걸리는걸 생각하여 if-else로 묶기
for _ in range(t):
    nx, ny = r + dx[dir], c + dy[dir] 
    if in_range(nx,ny):
        r,c = nx, ny
    else:
        dir = 3 - dir 

print(r+1,c+1) # 다시 +1 해주어 행열 정상화