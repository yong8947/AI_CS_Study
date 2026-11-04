def solution(numbers):
    ans = [num for num in range(10) if num not in numbers]
    return sum(ans)