str = input()

print(str.swapcase()) #.swapcase = 대소문자 반전 메서드


"""
---- 또 다른 유용한 풀이들 ----


1. 알고리즘 좋은 풀이
print(''.join(x.upper() if x == x.lower() else x.lower() for x in input()))


2. 정석
str = input()
a = ''

for s in str :
    if(s.isupper()) :
        a = a + s.lower()
    else : 
        a = a + s.upper()

print(a)


"""
