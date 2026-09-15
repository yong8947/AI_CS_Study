n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
arr = [0]*101
for a,b in segments:
    for i in range(a,b):
        arr[i] += 1
print(max(arr))
