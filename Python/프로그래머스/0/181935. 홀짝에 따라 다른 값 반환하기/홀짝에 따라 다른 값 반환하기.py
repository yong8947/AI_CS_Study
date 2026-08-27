def solution(n):
    cnt=0
    if n%2==1:
        for i in range(1,n+1,2):
            cnt+=i
        return cnt
    else:
        for j in range(2,n+1,2):
            cnt+=j**2
        return cnt
            