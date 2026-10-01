n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]

max_time = 0

for i in range(n):
    work_time = [0] * 1001
    sum_time = 0
    for j in range(n):
        if j == i:
            continue

        s,e = times[j]

        for k in range(s,e):
            work_time[k] = 1

    sum_time = work_time.count(1)
    max_time = max(max_time, sum_time)

print(max_time)