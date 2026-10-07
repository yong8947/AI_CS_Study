n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

ans = 0

for i in range(n): # 최솟값 하나 뽑아
    arr2 = []

    for elem in arr:
        if elem > arr[i] or abs(elem - arr[i]) > k:
            continue
        
        arr2.append(elem)
    
    ans = max(ans, len(arr2))

print(ans)