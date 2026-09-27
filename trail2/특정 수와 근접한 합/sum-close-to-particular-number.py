import sys
N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
min_diff = sys.maxsize
total = sum(arr)

for i in range(N-1):
    for j in range(i+1,N):
        diff = total - arr[i] - arr[j]
        ans = abs(diff - S)
        min_diff = min(min_diff, ans)

print(min_diff)