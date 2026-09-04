def solution(arr):
    local_2 = []
    for i in range(len(arr)):
        if arr[i] == 2:
            local_2.append(i)
    return arr[min(local_2):max(local_2)+1] if local_2 else [-1]