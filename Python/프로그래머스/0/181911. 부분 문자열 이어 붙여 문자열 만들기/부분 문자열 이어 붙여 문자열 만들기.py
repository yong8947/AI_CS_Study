def solution(my_strings, parts):
    a = ''
    for i in range(len(parts)):
        s,e = parts[i]
        a += my_strings[i][s:e+1]
    return a