def solution(babbling):
    cnt = 0
    can_speak = ["aya", "ye", "woo", "ma"]
    
    for bab in babbling:
        stack = ""
        before_word = ""
        
        for ch in bab:
            stack += ch
            for word in can_speak:
                n = len(word)
                if word == stack and before_word != word:
                    stack = stack[:-n]
                    before_word = word
                
        if stack == "":
            cnt += 1
            
    return cnt