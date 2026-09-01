def solution(my_string):
    l = [my_string[n:] for n in range(len(my_string))]
    return sorted(l)