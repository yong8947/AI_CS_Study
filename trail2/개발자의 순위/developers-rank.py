k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

ans = 0

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            continue
        
        cnt = 0

        for s in range(k):
            rank_a = arr[s].index(i)
            rank_b = arr[s].index(j)
            if rank_a < rank_b:
                cnt += 1

        if cnt == k:
            ans += 1

print(ans)