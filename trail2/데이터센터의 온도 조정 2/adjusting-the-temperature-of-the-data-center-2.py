n,c,g,h = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(n)]

def temp_select(t):
    cnt = 0
    for i in range(n):
        ta,tb = ranges[i]
    
        if t < ta:
            cnt += c
        elif ta <= t <= tb:
            cnt += g
        else:
            cnt += h
    
    return cnt

ans = 0

for i in range(1,1001):
    ans = max(ans, temp_select(i))

print(ans)