def solution(num_list):
    list = num_list
    if list[-1] > list[-2]:
        list.append(list[-1] - list[-2])
    else:
        list.append(list[-1]*2)
    return list