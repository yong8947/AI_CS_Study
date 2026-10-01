k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

ans = 0

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        
        cnt = 0

        for s in range(k):
            if arr[s][i] < arr[s][j]:
                cnt += 1

        if cnt == k:
            ans += 1

print(ans)