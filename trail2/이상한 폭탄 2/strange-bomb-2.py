N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

ans = -1

for i in range(N):
    for j in range(i+1,N):

        Ai = num[i]
        Aj = num[j]
        cnt = -1

        if Ai == Aj and abs(i-j) <= K:
            cnt = Ai
        
        ans = max(ans, cnt)

print(ans)