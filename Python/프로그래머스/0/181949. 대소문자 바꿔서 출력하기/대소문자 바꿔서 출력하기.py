str = input()

# print(str.swapcase()) 

#.swapcase = 대소문자 반전 메서드

for i in str:
    if i == i.upper():
        print(i.lower(), end='')
    else:
        print(i.upper(), end='')
        
