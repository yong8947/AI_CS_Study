def solution(price, money, count):
    ans = 0
    for i in range(1,count+1):
        ans += price * i
    return ans-money if money < ans else 0