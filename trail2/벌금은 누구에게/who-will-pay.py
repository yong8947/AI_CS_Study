N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.
arr = []
for i in student:
    arr.append(i)
    if arr.count(i) >= K:
        print(i)
        break