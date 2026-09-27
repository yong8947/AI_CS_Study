A = input()

# Please write your code here.
cnt = 0
n = len(A)

for i in range(n-2):
    for j in range(i+2,n-1):
        if A[i] == '(' and A[i+1] == '(':
            if A[j] == ')' and A[j+1] == ')':
                cnt += 1
print(cnt)