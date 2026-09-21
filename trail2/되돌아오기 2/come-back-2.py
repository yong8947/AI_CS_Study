commands = input()

# Please write your code here.
x,y = 0,0
dir_num = 3
ans = -1

dx = [1,0,-1,0]
dy = [0,-1,0,1]

for i, s in enumerate(commands):
    if s == 'L':
        dir_num = (dir_num + 3) % 4
    elif s == 'R':
        dir_num = (dir_num + 1) % 4
    elif s== 'F':
        x = x + dx[dir_num]
        y = y + dy[dir_num]

        if x == 0  and y == 0:
            ans = i + 1
            break
            
print(ans)