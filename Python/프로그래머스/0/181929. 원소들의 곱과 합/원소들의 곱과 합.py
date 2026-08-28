def solution(num_list):
    cnt_mul = 1
    cnt_sq = 0
    for i in num_list:
        cnt_mul *= i
        cnt_sq += i
    return int(cnt_mul < cnt_sq**2)