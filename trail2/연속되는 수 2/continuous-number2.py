n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
arr2 = []
cnt = 1
for i in range(n):
    if i==0 or arr[i]==arr[i-1]:
        cnt+=1
    else:
        arr2.append(cnt)
        cnt = 1
print(max(arr2))