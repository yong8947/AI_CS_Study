n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = 0
cnt = 0

for i in range(n):
    for j in range(n-2):

        for k in range(n):
            for l in range(n-2): # 그냥 range(j+2,n-2) 해버리면 다른 행일 떄 건너뛰는 구간이 발생

                if i == k and abs(j-l)<3: # 같은 행이고 둘이 겹칠 때만 건너뜀
                    continue 

                cnt = (arr[i][j] + arr[i][j+1] + arr[i][j+2] +
                        arr[k][l] + arr[k][l+1] + arr[k][l+2])
                ans = max(ans, cnt)

print(ans)