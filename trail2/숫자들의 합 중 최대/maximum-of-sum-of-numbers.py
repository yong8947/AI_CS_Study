X, Y = map(int, input().split())

# Please write your code here.
ans = 0
for num in range(X,Y+1):
    arr = tuple(map(int, list(str(num))))
    sum_num = sum(arr)
    ans = max(ans, sum_num)

print(ans)