n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
arr = [[0]*201 for _ in range(201)]

# 1=빨간색 / 2=파란색
for i in range(n):
    for x in range(x1[i]+100,x2[i]+100):
        for y in range(y1[i]+100,y2[i]+100):
            if i%2==0:
                arr[x][y] = 1
            else:
                arr[x][y] = 2

b = sum(i.count(2) for i in arr)

print(b)
