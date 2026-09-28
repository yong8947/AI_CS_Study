n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.
arr = [0] * (max(x)+k+1)  # 기존 max(x)+1

for i in range(n):
    if c[i] == 'G':
        arr[x[i]] = 1
    else:
        arr[x[i]] = 2

ans = 0

for i in range(1,max(x)+1): # 내가 기존에 잡았던 len(arr)-k+1로 하면  K>max(x)의 경우를 배제하고 하는거라 틀렸던 것 !!
    cnt = 0
    for j in range(i,i+k+1):
        cnt += arr[j]
    ans = max(ans, cnt)

print(ans)