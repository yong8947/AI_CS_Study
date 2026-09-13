def solution(myString):
    answer = ['l' if x < 'l' else x for x in myString]
    return "".join(answer)