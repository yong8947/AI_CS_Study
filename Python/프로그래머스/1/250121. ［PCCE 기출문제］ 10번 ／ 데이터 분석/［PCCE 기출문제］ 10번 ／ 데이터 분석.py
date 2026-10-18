def solution(data, ext, val_ext, sort_by):
    dict_data = {
        "code" : 0,
        "date" : 1,
        "maximum" : 2,
        "remain" : 3
    }
    
    ans = []
    
    for arr in data:
        if arr[dict_data[ext]] < val_ext:  
            ans.append(arr)
            
    ans.sort(key=lambda x: x[dict_data[sort_by]])
    
    return ans