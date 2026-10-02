x,y = map(int, input().split())

cnt = 0

def one_diff(n):
    if len(set(n)) != 2:
        return False

    arr = [n.count(i) for i in set(n)]
    if 1 in arr:
        return True

    return False

for num in range(x,y+1):
    if one_diff(str(num)):  #한자리만 다른 조건
        cnt += 1

print(cnt)