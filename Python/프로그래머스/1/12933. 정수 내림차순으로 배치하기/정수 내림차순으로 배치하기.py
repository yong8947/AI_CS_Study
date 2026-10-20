def solution(n):
    arr = [i for i in str(n)]
    arr.sort(reverse=True)
    ans = "".join(arr)
    return int(ans)