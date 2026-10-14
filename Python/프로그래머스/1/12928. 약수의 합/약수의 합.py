def solution(n):
    s = [num for num in range(1,n+1) if n % num == 0]
    return sum(s)