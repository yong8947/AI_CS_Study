arr = list(map(int, input().split()))

# Please write your code here.
def get_diff(i,j,k):
    sum1 = arr[i] + arr[j]
    sum2 = sum(arr) - sum1 - arr[k]
    sum3 = arr[k]
    
    if sum1 == sum2 or sum2 == sum3 or sum1 == sum3:
        return -1

    max_sum = max(sum1, sum2, sum3)
    min_sum = min(sum1, sum2, sum3)
    return abs(max_sum - min_sum) 

min_diff = 100000

for i in range(5):
    for j in range(i+1,5):
        for k in range(5):
            if i==k or j == k:
                continue
            if get_diff(i,j,k) != -1:
                min_diff = min(min_diff, get_diff(i,j,k))

if min_diff == 100000: print(-1)
else: print(min_diff)