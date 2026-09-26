n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
import sys

min_dist = sys.maxsize

for i in range(1,n-1):
    x1 = x[:i]+x[i+1:]
    y1 = y[:i]+y[i+1:]
    test_dist = 0

    for j in range(n-2):
        test_dist += abs(x1[j] - x1[j+1]) + abs(y1[j] - y1[j+1]) 

    min_dist = min(min_dist, test_dist)

print(min_dist)