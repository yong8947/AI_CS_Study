def solution(a, b):
    arr = [i*j for i,j in zip(a,b)]
    return sum(arr)