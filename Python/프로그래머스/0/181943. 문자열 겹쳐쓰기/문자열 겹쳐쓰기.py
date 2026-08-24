def solution(my_string, overwrite_string, s):
    return my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]

"""


def solution(my_string, overwrite_string, s):
    answer = ''
    k = 0
    for i in range(len(my_string)):
        if i >= s and i < s+len(overwrite_string):
            answer += overwrite_string[k]
            k += 1
        else: answer += my_string[i]
    return answer


"""