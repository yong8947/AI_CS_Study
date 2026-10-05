a,b,c = map(int, input().split())

max_val = 0

for i in range(1000):
    for j in range(1000):
        if a*i + b*j <= c:
            max_val = max(max_val, a*i + b*j)

print(max_val)