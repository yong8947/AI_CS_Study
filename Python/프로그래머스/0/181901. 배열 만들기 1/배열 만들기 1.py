def solution(n, k):
    return [i for i in range(1,n+1) if not i%k]