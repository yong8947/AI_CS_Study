n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
import sys
ans = -sys.maxsize
cnt = 0

for i in range(n-2):
    for j in range(i+2,n):
        cnt = numbers[i] + numbers[j]
        ans = max(ans,cnt)

print(ans)