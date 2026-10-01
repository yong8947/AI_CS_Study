N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

ans = 0

for i in range(N):
    p = P[:]
    p[i] //= 2
    p.sort() # 싼 가격부터 많이 줘야 최대한 많이 주기 떄문에 싼 가격 순으로 정렬

    sum_price = 0
    cnt = 0

    for j in range(N):
        sum_price += p[j]
        if sum_price > B:
            break
        cnt += 1

    ans = max(ans, cnt)

print(ans)