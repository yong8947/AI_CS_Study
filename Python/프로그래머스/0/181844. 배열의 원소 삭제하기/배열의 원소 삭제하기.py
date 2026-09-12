def solution(arr, delete_list):
    arr2 = []
    for i,num in enumerate(arr):
        arr2.append((i,num))
        if num in delete_list:
            arr2.remove((i,num))
    return [sorted(arr2)[n][1] for n in range(len(arr2))]