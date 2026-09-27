n = int(input())
S = input()

# Please write your code here.
cnt = 0

for c in range(n):
    for o in range(c+1,n):
        for w in range(o+1,n):
            if S[c]=='C' and S[o]=='O' and S[w]=='W':
                cnt+=1
print(cnt)