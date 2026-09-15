n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
arr = [0]*2001
crr = 1001
cnt = 0

for X,D in zip(x,dir):
    if D == 'L':
        for i in range(crr,crr-X,-1):
            arr[i] += 1
        crr -= X
    else:
        for j in range(crr,crr+X):
            arr[j] += 1
        crr += X

for s in range(2001):
    if arr[s] >= 2:
        cnt += 1

print(cnt)