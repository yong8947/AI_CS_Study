n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
import sys

ans = sys.maxsize

for i in range(n):
    xi = x[:i] + x[i+1:]
    yi = y[:i] + y[i+1:]

    min_sq = (max(xi) - min(xi)) * (max(yi) - min(yi))
    ans = min(ans, min_sq)

print(ans)