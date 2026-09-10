def solution(arr):
    pow2 = 1
    while pow2 < len(arr):
        pow2*=2
    return arr + [0] * (pow2 - len(arr))    