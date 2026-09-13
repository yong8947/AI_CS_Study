def solution(myString):
    alpha_before_l = ['a','b','c','d','e','f','g','h','i','j','k']
    new_str = ''
    for i in myString:
        if i in alpha_before_l:
            new_str += 'l'
        else: new_str += i
    return new_str
    