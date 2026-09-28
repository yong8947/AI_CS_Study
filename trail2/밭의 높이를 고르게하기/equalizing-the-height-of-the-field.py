N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
min_price = 10000000000000

for i in range(N-T+1):
    price = 0
    for j in range(i,i+T):
        price += abs(arr[j] - H)

    min_price = min(min_price,price)

print(min_price)