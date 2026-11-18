def solution(n, m):
    ans = []
    k = max(n,m)

    for i in range(k,0,-1):
        if n%i == 0 and m%i==0:
            ans.append(i)
            ans.append(n*m // i)
            break
            
    return ans