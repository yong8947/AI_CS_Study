
# 새로운 배열을 만드는 것이 아닌 어차피 사람이 양쪽끝에서 들고있어야하니까 사람 기준으로 위치랑 알파벳을 탐색해서 하는 방법
 
n = int(input())
people = []

for _ in range(n):
    num, p = input().split()
    people.append((int(num),p))

ans = 0
arr = sorted(people)

for i in range(n):
    for j in range(i,n):
        cntG = 0
        cntH = 0
        for k in range(i,j+1):
            if arr[k][1] == 'G':
                cntG += 1
            else:
                cntH += 1
        if cntG == 0 or cntH == 0 or cntG == cntH:
            s = arr[j][0] - arr[i][0]
            ans = max(ans,s)
        
print(ans)

"""
# 새로운 배열을 만들어서 사람을 찾고 그 사이의 팻말을 비교하는 알고리즘

n = int(input())
people = [tuple(input().split()) for _ in range(n)]
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

arr = ['X'] * (max(pos) + 1)

for i in range(n):
    arr[pos[i]] = alpha[i]

ans = 0

for i in range(max(pos)+1):
    for j in range(i, max(pos)+1):
        
        # 양 끝점 i와 j에 사람이 서 있는 경우에만 사진을 찍음
        if arr[i] == 'X' or arr[j] == 'X':
            continue
            
        cnt_G = 0
        cnt_H = 0

        for k in range(i, j + 1):
            if arr[k] == 'G':
                cnt_G += 1
            elif arr[k] == 'H':
                cnt_H += 1
        
        if cnt_G == 0 or cnt_H == 0 or cnt_G == cnt_H:
            ans = max(ans, j - i)

print(ans)

"""