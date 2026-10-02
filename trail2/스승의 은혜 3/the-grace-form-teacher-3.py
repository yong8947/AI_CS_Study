N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]
P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]

ans = 0

for i in range(N):
    p = P[:]
    s = S[:]
    p[i] //= 2
    price = [p[k]+s[k] for k in range(N)]
    price.sort()

    cnt = 0
    sum_price = 0

    for j in range(N):
        sum_price += price[j]
        if B < sum_price:
            break
        cnt += 1

    ans = max(ans,cnt)

print(ans)