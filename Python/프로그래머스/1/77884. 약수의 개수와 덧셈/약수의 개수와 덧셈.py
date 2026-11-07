def solution(left, right):
    ans = 0
    for i in range(left, right+1):
        if int(i**0.5) == i**0.5:
            ans -= i
        else:
            ans += i
            
    return ans