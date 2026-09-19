N, M = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.
posA = []
posB = []
cntA,cntB = 0,0

for i in range(N):
    for j in range(t[i]):
        cntA += v[i]
        posA.append(cntA)
         
for i in range(M):
    for j in range(t2[i]):
        cntB += v2[i]
        posB.append(cntB)

fame = ''
ans = 0

for i in range(len(posA)):

    fame_A = posA[i] > posB[i]
    fame_B = posA[i] < posB[i]
    fame_AB = posA[i] == posB[i]

    if fame_A:
        if fame != 'A':
            ans+=1
        fame = 'A'
    
    if fame_B:
        if fame != 'B':
            ans+=1
        fame = 'B'

    if fame_AB:
        if fame != 'AB':
            ans+=1
        fame = 'AB'

print(ans)