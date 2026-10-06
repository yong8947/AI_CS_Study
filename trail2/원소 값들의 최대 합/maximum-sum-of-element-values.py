n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

ans = 0

for i in range(1,n+1): #시작위치 완전탐색
    cnt = 0
    s = i

    for j in range(m): # m번 반복
        cnt += arr[s]
        s = arr[s]

    ans = max(ans, cnt)

print(ans)