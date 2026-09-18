N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
ans,cnt = 0,1

for i in range(1,N):
    if arr[i] > 0 and arr[i-1] > 0:
        cnt+=1
    elif arr[i] < 0 and arr[i-1] < 0:
        cnt+=1
    else:
        cnt = 1

    ans = max(ans, cnt)

print(ans)