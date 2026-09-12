import sys

# 자릿수 제한을 200,000자리로 확장
sys.set_int_max_str_digits(200000)


def solution(a, b):
    return str(int(a) + int(b))