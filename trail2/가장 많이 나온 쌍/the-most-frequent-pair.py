n, m = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(m)]

ans = 0

for i in range(m):
    cnt = 0

    for j in range(m):
        if sorted(pairs[i]) == sorted(pairs[j]):
            cnt += 1
    
    ans = max(ans, cnt)

print(ans)