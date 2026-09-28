n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.
arr = [0] * (max(x)+1)

for i in range(n):
    if c[i] == 'G':
        arr[x[i]] = 1
    else:
        arr[x[i]] = 2

ans = 0

for i in range(1,max(x)-k+1):
    cnt = 0
    for j in range(i,i+k+1):
        cnt += arr[j]
    ans = max(ans, cnt)

print(ans)