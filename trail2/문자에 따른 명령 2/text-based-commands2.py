dirs = input()

# Please write your code here.
x,y = 0,0
dir_num = 3
dx,dy = [1,0,-1,0],[0,-1,0,1] #동남서

for s in dirs:
    if s == 'L':
        dir_num = (dir_num+3)%4
    elif s== 'R':
        dir_num = (dir_num+1)%4
    elif s == 'F':
        x += dx[dir_num]
        y += dy[dir_num]

print(x,y)