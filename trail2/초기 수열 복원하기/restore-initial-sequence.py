n = int(input())

if n == 1:
    print(1)
else:
    s = list(map(int, input().split()))

    # 첫 번째 원소 A[0]을 1부터 N까지 시도
    for first in range(1, n + 1):
        a = [0] * n
        a[0] = first
        visited = [False] * (n + 1)  # 방문 체크 배열 (1~N)
        visited[first] = True
        
        is_possible = True
        
        # A[1]부터 A[n-1]까지 순차적으로 복원
        for i in range(n - 1):
            next_val = s[i] - a[i]
            
            # 조건 체크: 1~N 범위 내이고, 아직 사용하지 않은 숫자여야 함
            if 1 <= next_val <= n and not visited[next_val]:
                a[i + 1] = next_val
                visited[next_val] = True
            else:
                is_possible = False
                break
        
        # 성공적으로 수열을 만들었다면 출력 후 종료 (사전순 최우선)
        if is_possible:
            print(*(a))
            break