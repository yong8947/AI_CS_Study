import sys
abilities = list(map(int, input().split()))

# Please write your code here.
def get_diff(i,j,k):
    sum1 = abilities[i] + abilities[j] + abilities[k]
    sum2 = sum(abilities) - sum1
    return abs(sum1 - sum2)

min_diff = sys.maxsize

for i in range(6):
    for j in range(i+1,6):
        for k in range(j+1,6):
            min_diff = min(min_diff, get_diff(i,j,k))

print(min_diff)