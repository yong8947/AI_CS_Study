n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

ans = 100

for i in range(2,101,2):
    for j in range(2,101,2):
        cnt1 = 0
        cnt2 = 0
        cnt3 = 0
        cnt4 = 0
        cnt_max = 0

        for s in range(n):
            x,y = points[s]

            if x>i and y>j: # 1사분면
                cnt1 += 1
            
            elif x>i and y<j: # 4사분면
                cnt2 += 1

            elif x<i and y<j: # 3사분면
                cnt3 += 1

            elif x<i and y>j: # 2사분면
                cnt4 += 1

        cnt_max = max(cnt1, cnt2, cnt3, cnt4)
        ans = min(ans, cnt_max)

print(ans)