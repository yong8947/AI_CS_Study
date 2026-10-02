T, a, b = map(int, input().split())
c = []
x = []
for _ in range(T):
    char, pos = input().split()
    c.append(char)
    x.append(int(pos))

cnt = 0
for k in range(a,b+1):
    d1 = 10000
    d2 = 10000
    for i in range(T):

        if c[i] == 'S':
            d1 = min(d1, abs(k-x[i]))
        
        if c[i] == 'N':
            d2 = min(d2, abs(k-x[i]))

    if d1 <= d2:
        cnt += 1

print(cnt)