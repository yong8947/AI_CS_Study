def solution(n):
    num = n**0.5
    if num.is_integer():
        return (int(num)+1)**2
    else:
        return -1