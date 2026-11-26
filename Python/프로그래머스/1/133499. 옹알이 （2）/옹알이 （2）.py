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


"""
제미나이피셜 : 가장 이상적인 코드

def solution(babbling):
    sounds = ("aya", "ye", "woo", "ma")
    count = 0

    for word in babbling:
        idx = 0
        prev = ""
        n = len(word)

        while idx < n:
            matched = ""
            for s in sounds:
                if s != prev and word.startswith(s, idx):
                    matched = s
                    break

            if not matched:
                break

            prev = matched
            idx += len(matched)

        if idx == n:
            count += 1

    return count

"""