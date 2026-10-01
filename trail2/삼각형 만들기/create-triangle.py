n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
ans = 0

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            xx = [x[i], x[j], x[k]]
            yy = [y[i], y[j] ,y[k]]

            if len(set(xx)) != 2 or len(set(yy)) != 2:
                continue
            
            tr_x2 = (max(xx) - min(xx)) * (max(yy) - min(yy))
            ans = max(ans, tr_x2)

print(ans)