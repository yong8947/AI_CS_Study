n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(n):
    a,b = lines[i]
    is_meet = False
    
    for j in range(n):
        if j == i:
            continue
        
        c,d = lines[j]
        
        if (a-c) * (b-d) < 0:
            is_meet = True
            break
        
    if not is_meet:
        ans+=1

print(ans)