N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

# Please write your code here.
arr1 = [0] * N # 개발자의 남은 악수 배열
arr2 = [0] * N # 감염자인지 아닌지 구분하는 배열 * 1=감염자

arr1[P-1] = K
arr2[P-1] = 1

handshakes = sorted(handshakes)

for a,b,c in handshakes:
    # 변수에 조건을 미리 저장해두어 b로인해 c가 감염되었을 떄 바로 c의 감염횟수가 차감되지 않도록 처리 ****
    b_can = arr2[b-1] == 1 and arr1[b-1] > 0
    c_can = arr2[c-1] == 1 and arr1[c-1] > 0 

    if b_can:
        arr1[b-1] -= 1
        if arr2[c-1] == 0:
            arr2[c-1] = 1
            arr1[c-1] = K

    if c_can:
        arr1[c-1] -= 1
        if arr2[b-1] == 0:
            arr2[b-1] = 1
            arr1[b-1] = K

for i in arr2:
    print(i,end='')