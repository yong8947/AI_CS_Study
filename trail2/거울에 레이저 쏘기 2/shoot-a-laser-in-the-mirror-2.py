n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Please write your code here.
dx = [0,1,0,-1] #동남서북
dy = [1,0,-1,0]

if 1<=k<=n:
    dir_num = 1 
    x,y = 0,k-1
elif n<k<=2*n:
    dir_num = 2 
    x,y = k-n-1,n-1
elif 2*n<k<=3*n:
    dir_num = 3
    x,y = n-1,3*n-k
elif 3*n<k<=4*n:
    dir_num = 0
    x,y = 4*n-k,0

def in_range(x,y):
    return 0<=x<n and 0<=y<n

cnt = 0
# for 보단 while로 하는게 편함 >> 너무 for만 고집하지 말기 !!
while in_range(x,y):
    if grid[x][y] == '/':
        dir_num = 3 - dir_num
    else:
        # dir_num = dir_num ^ 1 >> 비트연산자로 하면 편함 근데 난 몰랐으니 패스
        if dir_num == 1:
            dir_num = 0
        elif dir_num == 2:
            dir_num = 3
        elif dir_num == 0:
            dir_num = 1
        else:
            dir_num = 2

    cnt+=1

    x += dx[dir_num]
    y += dy[dir_num]

print(cnt)