x,y = map(int, input().split())

ans = 0

for num in range(x,y+1):
    if num == int(str(num)[::-1]):
        ans += 1

print(ans)