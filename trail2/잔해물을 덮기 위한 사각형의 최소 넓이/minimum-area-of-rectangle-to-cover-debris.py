x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.
arr = [[0]*2001 for _ in range(2001)] #offset을 이용하여 배열을 만든다

# 첫 번째 직사각형의 넓이
for x in range(x1[0]+1000,x2[0]+1000):
    for y in range(y1[0]+1000,y2[0]+1000):
        arr[x][y] += 1

# 첫 번째 직사각형에서 두 번째 직사각형이 겹치는 부분을 뺀다
for x in range(x1[1]+1000,x2[1]+1000):
    for y in range(y1[1]+1000,y2[1]+1000):
        arr[x][y] = 0

arr_x = []
arr_y = []
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 1:
            arr_x.append(i)
            arr_y.append(j)

if not arr_x:
    print(0)
else:
    square_min = (max(arr_x) - min(arr_x)+1) * (max(arr_y) - min(arr_y)+1) # arr이 칸 인덱스이므로 선분을 계산할 때는 +1을 해주어야함  
    print(square_min)