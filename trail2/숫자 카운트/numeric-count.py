n = int(input())
a, b, c = [], [], []
for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    a.append(num)
    b.append(cnt1)
    c.append(cnt2)

# Please write your code here.
ans = 0

for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
        
            if i != j and j != k and k != i:

                is_possible = True

                for idx in range(n):
                    target_num = a[idx]
                    target_cnt1 = b[idx]
                    target_cnt2 = c[idx]

                    a1 = target_num // 100
                    b1 = (target_num // 10) % 10
                    c1 = target_num % 10

                    cnt11 = 0
                    cnt22 = 0

                    if i == a1: cnt11 += 1
                    if j == b1: cnt11 += 1
                    if k == c1: cnt11 += 1 

                    if i == b1 or i == c1: cnt22 += 1
                    if i == b1 or i == c1: cnt22 += 1
                    