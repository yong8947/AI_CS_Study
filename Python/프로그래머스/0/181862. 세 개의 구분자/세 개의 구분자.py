def solution(myStr):
    all_a = myStr.replace('b','a').replace('c','a')
    result = [x for x in all_a.split('a') if x]
    return result if result else ["EMPTY"]