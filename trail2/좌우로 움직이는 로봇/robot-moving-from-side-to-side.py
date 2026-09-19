n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

# Please write your code here.
pos_A = []
pos_B = []
cnt_A,cnt_B = 0,0

for i in range(n):
    if d[i] == 'R':
        for j in range(t[i]):
            cnt_A += 1
            pos_A.append(cnt_A)
    else:
        for j in range(t[i]):
            cnt_A -= 1
            pos_A.append(cnt_A)

for i in range(m):
    if d_b[i] == 'R':
        for j in range(t_b[i]):
            cnt_B += 1
            pos_B.append(cnt_B)
    else:
        for j in range(t_b[i]):
            cnt_B -= 1
            pos_B.append(cnt_B)

# 어느 한 로봇이 멈춘 이후 상황
larger = max(len(pos_A), len(pos_B))

while len(pos_A) < larger:
    pos_A.append(pos_A[-1])
while len(pos_B) < larger:
    pos_B.append(pos_B[-1])

ans = 0
check = 'No' # 0에서 만나는 건 생각 안하기때문에 
for i,j in zip(pos_A,pos_B):
    if i==j:
        if check =='No':
            ans+=1
        check = 'Yes'
    else:
        check = 'No'
print(ans)