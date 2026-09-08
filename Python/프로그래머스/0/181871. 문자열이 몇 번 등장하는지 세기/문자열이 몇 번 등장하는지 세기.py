def solution(myString, pat):
    cnt=0
    for i in range(len(myString)-len(pat)+1):
        if myString[i:i+len(pat)] == pat:
            cnt+=1
    return cnt