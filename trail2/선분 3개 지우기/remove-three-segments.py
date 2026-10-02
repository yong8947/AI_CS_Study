n = int(input())
lines = []
for _ in range(n):
    l, r = map(int, input().split())
    lines.append((l,r))

def get_overlapped(a,b,c):
    cnt = [0] * 101
    for i in range(n):
        if i in [a,b,c]:
            continue
        
        x1,x2 = lines[i]
        
        for j in range(x1,x2+1):
            cnt[j] += 1

    return max(cnt)

ans = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if get_overlapped(i,j,k) <= 1:
                ans+=1

print(ans)