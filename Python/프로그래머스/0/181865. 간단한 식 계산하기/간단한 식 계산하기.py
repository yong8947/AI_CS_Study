def solution(binomial):
    a,op,b = binomial.split()
    if op == '+':
        return int(a) + int(b)
    elif op =='-':
        return int(a) - int(b)
    else:
        return int(a) * int(b)