def solution(food):
    ans = ""
    for i in range(1,len(food)):
        n = food[i] // 2
        ans += str(i) * n
    return ans + '0' + ans[::-1]