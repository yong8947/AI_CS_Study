n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(1,4): # i번 위치에 돌을 넣는다고 생각
    score = 0 
    arr = [0,1,2,3]

    for j in range(n):  # n번의 연산 과정
        a,b,c = moves[j]    
        arr[a],arr[b] = arr[b],arr[a]
        
        if arr[c] == i:
            score += 1
    
    ans = max(ans, score)

print(ans)