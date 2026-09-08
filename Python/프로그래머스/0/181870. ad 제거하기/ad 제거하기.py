def solution(strArr):
#   for i in strArr:
#       if 'ad' in i: del i >>> 이렇게 하면 인덱스 밀림 문제 발생
#   return strArr"""

    return [x for x in strArr if 'ad' not in x]
# ad를 포함하는 것들을 제거하는 것보다 포함하지 않는 것들을 가져오는게 파이썬스러운 방식이다.