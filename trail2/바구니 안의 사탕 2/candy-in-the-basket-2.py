N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

# Please write your code here.
arr = [0] * (max(pos)+2*K+1)
max_cnt = 0

for i in range(N): 
    arr[pos[i]] += candy[i]

for i in range(max(pos)+K+1): # max(pos)+K가 i 값이면 그래도 이건 max(pos)의 값을 포함하기 때문에 여기까지 볼 필요가 있다.
    cnt = 0
    for j in range(i-K,i+K+1):
        if j>= 0:
            cnt += arr[j]
    max_cnt = max(max_cnt, cnt)

print(max_cnt)