n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
ans,cnt = 1,1

for i in range(1,n):
    if arr[i] > arr[i-1]:
        cnt += 1
    else:
        cnt =1
    ans = max(ans, cnt)

print(ans)