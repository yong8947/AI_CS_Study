def solution(myString, pat):
    n = myString.rindex(pat)
    return myString[:n+len(pat)]