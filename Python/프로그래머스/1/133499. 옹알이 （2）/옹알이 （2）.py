def solution(babbling):
    cnt = 0
    stack = ""
    # can_speak = ["aya", "ye", "woo", "ma"]
    
    for bab in babbling:
        before_word = ""
        
        for s in bab:
            stack += s
            if "aya" == stack and before_word != "aya":
                stack = stack[:-3]
                before_word = "aya"
            elif "woo" == stack and before_word != "woo":
                stack = stack[:-3]
                before_word = "woo"
            elif "ye" == stack and before_word != "ye":
                stack = stack[:-2]
                before_word = "ye"
            elif "ma" == stack and before_word != "ma":
                stack = stack[:-2]
                before_word = "ma"
                
        if stack == "":
            cnt += 1
        else:
            stack = ""
            
    return cnt