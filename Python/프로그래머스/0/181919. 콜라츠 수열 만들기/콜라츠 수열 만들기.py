def solution(n):
    arr = []
    while True:
        if n==1:
            arr.append(n)
            break
        if n%2:
            arr.append(n)
            n = 3*n+1
        else:
            arr.append(n)
            n //= 2
    return arr
        