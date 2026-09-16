n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
arr = [''] * 200001 # offset: 100000
pos = 100000

for i in range(n):
    if dir[i] == 'R':
        for j in range(pos, pos+x[i]):
            arr[j] = 'B'
        pos = pos + x[i]-1

    elif dir[i] == 'L':
        for j in range(pos-x[i]+1, pos+1):
            arr[j] = 'W'
        pos = pos - x[i]+1

cnt_w = arr.count('W')
cnt_b = arr.count('B')

print(cnt_w, cnt_b)