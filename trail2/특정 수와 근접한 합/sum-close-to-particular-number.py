import sys
N, S = map(int, input().split())
arr = list(map(int, input().split()))

# 리스트에서 요소를 뺴서 합하는 것 보다 그냥 전체 합에서 각 요소값을 빼는게 훨씬 효율적임 ㅇㅇ
min_diff = sys.maxsize
total = sum(arr)

for i in range(N-1):
    for j in range(i+1,N):
        diff = total - arr[i] - arr[j]
        ans = abs(diff - S)
        min_diff = min(min_diff, ans) 

print(min_diff)