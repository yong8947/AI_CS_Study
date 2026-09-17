n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
arr = [[0]*2001 for _ in range(2001)]

for i in range(n):
    for x in range(x1[i]+1000,x2[i]+1000):
        for y in range(y1[i]+1000,y2[i]+1000):
            arr[x][y] += 1

area = 0
for p in arr:
    for q in p:
        if q > 0:
            area +=1
    
print(area)