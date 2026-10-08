n, k = map(int, input().split())
arr = list(map(int, input().split()))

def is_possible(max_val):
    pos = 0 #시작위치

    while pos < n-1:
        next_pos = -1

        for j in range(pos+1, min(pos+k+1, n)): # 배열의 끝까지 점프
            if arr[j] <= max_val:
                next_pos = j # 가능한 값 중 가장 멀리 가기
            
        if next_pos == -1: # 안되면 아웃
            return False

        pos = next_pos # 위치 업데이트
    
    return True

ans = 0

for i in range(max(arr[0],arr[-1]), 101): # 첫번째값과 마지막값은 무조건 포함이므로 이것보다는 최댓값이 크거나 같아야함
    if is_possible(i):
        ans = i
        break # 가능한 최댓값 중 최소값이므로 가장먼저 발견한 값이 곧 답임

print(ans)