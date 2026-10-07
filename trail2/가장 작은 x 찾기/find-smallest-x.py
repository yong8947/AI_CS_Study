n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]


for x in range(1,10001):
    can = True
    for i in range(n):
        ai,bi = ranges[i]
        if not ai <= 2**(i+1) * x <= bi:
            can = False
            break
    if can:
        print(x)
        break