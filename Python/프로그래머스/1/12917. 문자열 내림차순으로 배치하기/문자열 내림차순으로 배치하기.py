def solution(s):
    arr = [i for i in s]
    arr.sort(reverse=True)
    return "".join(arr)