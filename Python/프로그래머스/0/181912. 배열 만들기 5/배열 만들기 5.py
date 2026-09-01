def solution(intStrs, k, s, l):
    list = []
    for i in intStrs:
        m = ''
        m += i[s:s+l]
        if int(m) > k:
            list.append(int(m))
    return list