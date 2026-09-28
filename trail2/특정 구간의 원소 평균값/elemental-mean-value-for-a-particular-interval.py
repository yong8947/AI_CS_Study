n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
ans = 0

for i in range(n):
    for j in range(i,n):
        cnt = 0
        ch = []
        for k in range(i,j+1):
            cnt += arr[k]
            ch.append(arr[k])
        
        if cnt/(j-i+1) in ch:
            ans+=1

print(ans)