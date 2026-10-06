N = int(input())
seat = input()

ans = 0

for i in range(N):
    if seat[i] == '0': # 사람이 없는 자리에 넣어보자
        
        # 사람이 있는 자리의 인덱스 추출 (i포함)
        person = [j for j, elem in enumerate(seat) if elem == '1' or j == i]

        dist = N # 앉아있는 사람들의 최소 거리
        for p in range(len(person)-1): 
            dist = min(dist, person[p+1]-person[p]) # 가장 가까운 사람의 최소 추출

        ans = max(ans, dist) # 가장 가까운 사람과의 최소거리의 최댓값 업데이트

print(ans)