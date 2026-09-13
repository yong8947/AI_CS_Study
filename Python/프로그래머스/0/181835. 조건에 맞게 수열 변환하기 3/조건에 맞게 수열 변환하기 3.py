def solution(arr, k):
    return [arr[i]*k if k%2 else arr[i]+k for i in range(len(arr))]