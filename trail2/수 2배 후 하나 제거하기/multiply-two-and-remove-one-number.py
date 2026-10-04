n = int(input())
arr = list(map(int, input().split()))

ans = 1000000000000000

for i in range(n):
    arr[i] *= 2
    for j in range(n):
        arr2 = [elem for k,elem in enumerate(arr) if k != j]

        sum_diff = 0
        for s in range(n-2):
            sum_diff += abs(arr2[s+1] - arr2[s])
            
        ans = min(ans, sum_diff)
    
    arr[i] //= 2

print(ans)