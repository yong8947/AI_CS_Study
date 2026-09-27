import sys
n = int(input())
a = [int(input()) for _ in range(n)]

# Please write your code here.
ans = sys.maxsize

for i in range(n):
    cnt = 0
    for j in range(i, i+n):
        cnt += (abs(j-i)) * a[j%n] # 이거 a인덱스의 범위를 벗어나지 않기위해 나머지 활용 **********

    ans = min(ans, cnt)

print(ans)