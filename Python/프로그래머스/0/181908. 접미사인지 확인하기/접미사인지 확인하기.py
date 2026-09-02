def solution(my_string, is_suffix):
    list = []
    for i in range(len(my_string)):
         list.append(my_string[i:])
    return int(is_suffix in list)