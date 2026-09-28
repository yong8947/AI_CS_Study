N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
if N<M:
    print(0)
    
ans = 0

for i in range(N-M+1):
    arr = []
    for j in range(i,i+M):
        arr.append(A[j])
    if sorted(arr) == sorted(B):
        ans += 1

print(ans)