N, M, D, S = map(int, input().split())

p, m, t = [], [], []
for _ in range(D):
    person, milk, time = map(int, input().split())
    p.append(person) #몇 번쨰 사람
    m.append(milk) # 몇 번쨰 치즈
    t.append(time) # 언제 먹었나

sick_p, sick_t = [], []
for _ in range(S):
    person, time = map(int, input().split())
    sick_p.append(person) # 몇 번쨰 사람
    sick_t.append(time) # 언제 아팠나

ans = 0

for cheese in range(1,M+1): # M개의 치즈를 하나씩 상한 치즈라고 가정 1~M까자
    is_out = True # 상했음 = True라고 가정

    for i in range(S): # 아픈 사람의 기록
        sp = sick_p[i]
        st = sick_t[i]

        ate = False 
        
        for j in range(D):
            if p[j] == sp and m[j] == cheese and t[j] < st: 
            # 먹은 사람과 아픈 사람이 같고 먹은 치즈가 상한 치즈이며 먹은 시간이 아픈 시간보다 이전이면
                ate = True # 아픈 사람은 상한 치즈를 먹은거네
                break

        if not ate: # 만약 아픈 사람중 한명이라도 안먹었으면
            is_out = False # 상한치즈가 아님
            break # 다시 다른 치즈를 상했다고 가정

    if is_out: # 상한치즈가 맞다면
        ate_people = set() # 중복방지

        for k in range(D):
            if m[k] == cheese: # 상한치즈라면 사람 추가
                ate_people.add(p[k])

        ans = max(ans, len(ate_people)) # 상한치즈를 먹은 최대 사람 수 체크

print(ans)