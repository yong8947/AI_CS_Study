n = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

# Please write your code here.
def min_dist(a,b):
    dist1 = abs(a-b)
    dist2 = n - dist1
    return min(dist1, dist2)

cnt = 0

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if min_dist(i,a1) <= 2 and min_dist(j,b1) <= 2 and min_dist(k,c1) <= 2:
                cnt += 1
            elif min_dist(i,a2) <= 2 and min_dist(j,b2) <= 2 and min_dist(k,c2) <= 2:
                cnt += 1

print(cnt)