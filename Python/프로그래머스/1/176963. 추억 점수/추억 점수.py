def solution(name, yearning, photo):
    score_dict = dict(zip(name,yearning))
    
    ans = []
    for p in photo:
        sum_score = 0 
        for n in p:
            if n in score_dict.keys():
                sum_score += score_dict[n]        
        ans.append(sum_score)
        
    return ans