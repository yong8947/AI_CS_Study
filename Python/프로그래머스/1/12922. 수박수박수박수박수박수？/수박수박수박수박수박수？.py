def solution(n):
    ans = ""
    for i in range(n):
        if not i % 2:
            ans += '수'
        else:
            ans += '박'
    return ans