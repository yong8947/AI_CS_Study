N = int(input())
A = list(map(int, input().split()))

# Please write your code here.
cnt = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if A[i] <= A[j] and A[j]<=A[k]:
                cnt += 1

print(cnt)