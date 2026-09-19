n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

# Please write your code here.
arr_A = []
arr_B = []
cnt_A, cnt_B = 0,0

for i in range(n):
    if d[i] == 'R':
        for j in range(t[i]):
            cnt_A += 1
            arr_A.append(cnt_A)
    else:
        for j in range(t[i]):
            cnt_A -= 1
            arr_A.append(cnt_A)

for i in range(m):
    if d2[i] == 'R':
        for j in range(t2[i]):
            cnt_B += 1
            arr_B.append(cnt_B)
    else:
        for j in range(t2[i]):
            cnt_B -= 1
            arr_B.append(cnt_B)

result = -1
for i in range(len(arr_A)):
    if arr_A[i] == arr_B[i]:
        result = i + 1
        break
print(result)