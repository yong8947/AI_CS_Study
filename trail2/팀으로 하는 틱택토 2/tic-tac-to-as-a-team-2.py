inp = [input() for _ in range(3)]

ans = set()

for i in range(3):
    if len(set(inp[i])) == 2:
        a = min(set(inp[i]))
        b = max(set(inp[i]))
        ans.add((a,b))
    
    k = [inp[l][i] for l in range(3)]
    if len(set(k)) == 2:
        c = min(set(k))
        d = max(set(k))
        ans.add((c,d))

if len(set(inp[0][0] + inp[1][1] + inp[2][2])) == 2:
    q = min(inp[0][0] + inp[1][1] + inp[2][2])
    w = max(inp[0][0] + inp[1][1] + inp[2][2])
    ans.add((q,w))

if len(set(inp[0][2] + inp[1][1] + inp[2][0])) == 2:
    e = min(inp[0][2] + inp[1][1] + inp[2][0])
    r = max(inp[0][2] + inp[1][1] + inp[2][0])
    ans.add((e,r))

print(len(ans))