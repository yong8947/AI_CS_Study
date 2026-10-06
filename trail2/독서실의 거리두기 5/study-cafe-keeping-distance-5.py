N = int(input())
seat = input()

ans = 0

for i in range(N):
    if seat[i] == '0': # 사람이 없는 자리에 넣어보자
        
        # 사람이 있는 자리의 인덱스 추출
        person = [j for j, elem in enumerate(seat) if elem == '1']

        dist = 20 # 자리가 있는 사람과의 최소 거리
        for p in person: 
            dist = min(dist, abs(p-i)) # 가장 가까운 사람 추출

        ans = max(ans, dist) # 가장 가까운 사람과의 최대 거리 업데이트

print(ans)