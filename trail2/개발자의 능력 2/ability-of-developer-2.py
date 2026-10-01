ab = list(map(int, input().split()))

# Please write your code here.
def get_diff(i,j,k,l):
    sum1 = ab[i] + ab[j]
    sum2 = ab[k] + ab[l]
    sum3 = sum(ab) - sum1 - sum2
    max_sum = max(sum1, sum2, sum3)
    min_sum = min(sum1, sum2, sum3)
    return abs(max_sum - min_sum)

min_diff = 10000000

for i in range(6):
    for j in range(6):
        for k in range(6):
            for l in range(6):
                if i !=j and k != j and k != l and l != i and i != k and j != l:
                    min_diff = min(min_diff, get_diff(i,j,k,l))

print(min_diff)