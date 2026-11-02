def solution(arr, divisor):
    ans = []
    for num in sorted(arr):
        if num % divisor == 0:
            ans.append(num)
    return ans if ans else [-1]