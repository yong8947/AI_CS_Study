def solution(num_list):
    s = 0
    for i in range(len(num_list)):
        if num_list[i] < 0:
            s = i
            return s
    return -1