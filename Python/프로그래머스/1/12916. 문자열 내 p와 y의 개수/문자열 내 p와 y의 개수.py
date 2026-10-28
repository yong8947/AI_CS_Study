def solution(s):
    S = s.upper()
    if S.count('Y') == S.count('P'):
        return True
    return False