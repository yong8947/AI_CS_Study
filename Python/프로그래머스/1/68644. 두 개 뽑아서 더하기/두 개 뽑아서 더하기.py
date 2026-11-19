def solution(numbers):
    pre_set = set()
    
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            pre_set.add(numbers[i] + numbers[j])
    
    return sorted(list(pre_set))