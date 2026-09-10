def solution(strArr):
    cnt_len = [0]*30
    for i in strArr:
        cnt_len[len(i)-1] += 1
    return max(cnt_len)