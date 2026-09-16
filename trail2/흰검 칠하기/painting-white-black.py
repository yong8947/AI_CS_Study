n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
arr = ['']*200001 #OFFSET
arr_white = [0]*200001
arr_black = [0]*200001

pos = 100000

for i in range(n):
    if dir[i] == 'R':
        for j in range(pos, pos+x[i]):
            if arr[j] == 'G':
                continue

            arr_black[j] += 1

            if arr_white[j] >= 2 and arr_black[j] >= 2:
                arr[j] = 'G'
            else:
                arr[j] = 'B'

        pos = pos + x[i] -1

    elif dir[i] == 'L':
        for j in range(pos-x[i]+1,pos+1):
            if arr[j] =='G':
                continue
            
            arr_white[j] += 1

            if arr_white[j] >= 2 and arr_black[j] >= 2:
                arr[j] = 'G'
            else:
                arr[j] = 'W'
           
        pos = pos - x[i] + 1

cnt_white = arr.count('W')
cnt_black = arr.count('B')
cnt_gray = arr.count('G')

print(cnt_white, cnt_black, cnt_gray)
