def solution(s, skip, index):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alpha_skip = ''
    
    for i in alphabet:
        if i not in skip:
            alpha_skip += i
    
    ans = ""
    for j in s:
        a = alpha_skip.index(j)
        ans += alpha_skip[(a+index) % len(alpha_skip)]
    
    return ans