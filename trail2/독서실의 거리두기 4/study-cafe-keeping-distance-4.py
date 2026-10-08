n = int(input())
seat = input()
ans = 0

for i in range(n):
    for j in range(i+1, n): # 임의의 두 자리 선정
        s = list(map(int, seat)) # 문자열은 변경이 불가능하므로 리스트로 변환

        if s[i] == 0 and s[j] == 0: # 두 자리 다 빈자리인 경우 착석
            s[i],s[j] = 1,1
        else:
            continue # 빈자리가 아닌데 앉으면 그냥 건너뛰기

        pos_seat = [] # 앉은 자리 위치 배열
        for k in range(n): 
            if s[k] == 1:
                pos_seat.append(k) 

        min_dist = 100
        for l in range(len(pos_seat)-1):
            min_dist = min(min_dist, pos_seat[l+1]-pos_seat[l]) # 가장 가까운 사람 거리 구하기

        ans = max(ans, min_dist) # 그 중 최대 거리 구하기

print(ans)