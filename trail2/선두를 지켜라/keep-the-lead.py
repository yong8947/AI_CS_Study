n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.
pos_A = []
pos_B = []
cnt_A,cnt_B = 0,0

for i in range(n):
    for j in range(t[i]):
        cnt_A += v[i]
        pos_A.append(cnt_A)

for i in range(m):
    for j in range(t2[i]):
        cnt_B += v2[i]
        pos_B.append(cnt_B)

ans = 0
leader = ''
for i,j in zip(pos_A, pos_B):
    if i > j:
        if leader == 'B':
            ans += 1
        leader = 'A'
    elif i < j:
        if leader == 'A':
            ans += 1
        leader = 'B'
    else:
        continue

print(ans)