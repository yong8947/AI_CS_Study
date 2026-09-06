def solution(num_list):
    cnt = 0
    for i in num_list:
        while i>1:
            if i%2:
                i = (i-1)//2
                cnt+=1
            else:
                i = i//2
                cnt+=1
    return cnt