n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
import sys
min_sum = sys.maxsize

for i in range(n):
    check_sum = 0
    for j in range(n):
        check_sum += abs(j - i) * A[j]

    min_sum = min(min_sum,check_sum)

print(min_sum)