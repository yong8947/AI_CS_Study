def solution(str_list, ex):
    result = ''
    for s in str_list:
        if ex in s:
            continue
        result += s
    return result