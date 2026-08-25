def solution(a, b):
    ab = str(a)+str(b)
    ba = str(b)+str(a)
    return int(ab) if int(ab)>=int(ba) else int(ba)
