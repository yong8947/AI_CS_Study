n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
arr = [[0]*201 for _ in range(201)]

for i in range(n):
    for x1 in range(x[i], x[i]+8):
        for y1 in range(y[i], y[i]+8):
            arr[x1][y1] += 1

ans = 0
for p in arr:
    for q in p:
        if q > 0:
            ans += 1

print(ans)