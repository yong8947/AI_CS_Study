n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
ans = -1

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            a = str(arr[i])
            b = str(arr[j])
            c = str(arr[k]) # 고른 세 정수를 문자열로 변환

            p = max(len(a),len(b),len(c)) # 각 정수 중 가장 큰 자릿 수 구하기

            a1 = a.zfill(p)
            b1 = b.zfill(p)            
            c1 = c.zfill(p) # 가장 큰 자릿 수 만큼 앞에 0을 채워줌 ex) 9 >> 009

            check = True # True = carry 없음
            for a2,b2,c2 in zip(a1,b1,c1): # 각 자리 수로 튜플 리스트 생성
                if int(a2)+int(b2)+int(c2) >= 10: # 각자리 수가 10 이상이면 즉시 반복문 종료
                    check = False # carry 발생
                    break
            
            if check: # True 상태가 유지되면 ans값 업데이트
                ans = max(ans, arr[i]+arr[j]+arr[k])

print(ans)