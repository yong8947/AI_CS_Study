def solution(q, r, code):
    a = ''
    for i in range(len(code)):
        s = i % q
        if s == r:
            a += code[i]
    return a