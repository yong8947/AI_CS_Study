N = int(input())
str = input()

ans = 0

for L in range(1,N+1): # L의 길이
    possible = True
    s = set()
    for i in range(N-L+1): # 탐색 시작위치 {i+L-1 <= N-1 -> i <= N-L}
    #""AAA"에서 길이 2인 부분문자열 "AA"는 12번째 글자와 23번째 글자에서 두 번 나타납니다" 
    # 위에 이 문장을 집합을 통해 해결 ** 원래 .count()썼다가 그건 중복겹칩을 해결 못하드라
        if str[i:i+L] in s:
            possible = False
            break
        s.add(str[i:i+L])
    
    if possible:
        ans = L
        break

print(ans)