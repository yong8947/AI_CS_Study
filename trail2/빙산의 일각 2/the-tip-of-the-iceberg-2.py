n = int(input())
h = [int(input()) for _ in range(n)]

ans = 0

for s in range(1,1001):
    cnt = []
    for i in range(n):
        if h[i] > s:
            cnt.append(i)
    
    cnt2 = 1 # 갯수를 새는 시점부터 이미 한 덩어리 위에 있기 떄문에 하나 카운트하고 시작
    for j in range(len(cnt)-1):
        if cnt[j+1] - cnt[j] != 1:
            cnt2 += 1
            
    ans = max(ans,cnt2)

print(ans)