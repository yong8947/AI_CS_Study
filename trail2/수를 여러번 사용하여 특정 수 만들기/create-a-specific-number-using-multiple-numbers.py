a,b,c = map(int, input().split())

max_val = 0
A = c//a + 1
B = c//b + 1

for i in range(A):
    for j in range(B):
        if a*i + b*j <= c:
            max_val = max(max_val, a*i + b*j)

print(max_val)