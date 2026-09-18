n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
arr2 = []
cnt = 1
for i in range(1,n):
    if arr[i] == arr[i-1]:
        cnt+=1
    else:
        arr2.append(cnt)
        cnt = 1
arr2.append(cnt)
print(max(arr2))