def solution(n, m, section):
    ans = 0
    last_painted = 0  

    for s in section:
        if s > last_painted:
            ans += 1
            last_painted = s + m - 1  

    return ans

# greedy 접근방식