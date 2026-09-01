def solution(number):
    n = 0
    for i in number:
        n += int(i)
    return n % 9